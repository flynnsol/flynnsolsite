# Single-container Reflex deployment: Caddy serves the static frontend and
# reverse-proxies backend routes to the Reflex/Granian backend on :8000.
# Both run in one container behind Fly.io's edge TLS termination.

ARG PORT=8080
ARG API_URL

FROM python:3.13 AS builder

RUN mkdir -p /app/.web
RUN python -m venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY rxconfig.py ./
RUN reflex init

# Pre-seed the locked frontend dependency versions so bun install is reproducible.
COPY reflex.lock/bun.lock reflex.lock/package.json .web/
RUN cd .web && ~/.local/share/reflex/bun/bin/bun install --frozen-lockfile

COPY . .

ARG PORT API_URL
RUN REFLEX_API_URL=${API_URL:-http://localhost:$PORT} reflex export --loglevel debug --frontend-only --no-zip && mv .web/build/client/* /srv/ && rm -rf .web

FROM python:3.13-slim

RUN apt-get update -y && apt-get install -y caddy redis-server && rm -rf /var/lib/apt/lists/*

ARG PORT API_URL
ENV PATH="/app/.venv/bin:$PATH" PORT=$PORT REFLEX_API_URL=${API_URL:-http://localhost:$PORT} REFLEX_REDIS_URL=redis://localhost PYTHONUNBUFFERED=1

WORKDIR /app
COPY --from=builder /app /app
COPY --from=builder /srv /srv
COPY Caddyfile /app/Caddyfile

STOPSIGNAL SIGKILL

EXPOSE $PORT

CMD caddy start --config /app/Caddyfile && \
    redis-server --daemonize yes && \
    exec reflex run --env prod --backend-only
