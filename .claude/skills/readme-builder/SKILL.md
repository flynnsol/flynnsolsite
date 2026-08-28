---
name: readme-builder
description: >
  Write or update the README.md for a GitLab project, and set the GitLab project's
  Description and Topics so the project shows up correctly on the flynnsol.com Projects
  page (which pulls name, description, topics, stars, and last-activity live from the
  GitLab API). Use this whenever the user is publishing a new project to GitLab, asks
  to "make a README", "write up this project", "add topics/tags" or "tag this with the
  language", wants a project's card to look right on the website, or is preparing a
  repo to be public-facing. Covers both the README content and the glab commands to
  set metadata.
---

# README Builder

Every public GitLab project under the `flynnsol` account is meant to double as a
card on the flynnsol.com Projects page. `flynnsol/states/projects_state.py` fetches
the GitLab API directly and reads exactly these fields:

| Website shows        | GitLab API field       | Where it comes from                  |
| --------------------- | ----------------------- | ------------------------------------- |
| Card title             | `name`                  | Project name                          |
| Card blurb             | `description`           | Project **Description** setting       |
| Badges under the blurb | `topics` (or `tag_list`) | Project **Topics** setting            |
| Star count             | `star_count`            | GitLab stars                          |
| "Updated Xd ago"       | `last_activity_at`      | Automatic                             |
| Card link              | `web_url`               | Automatic                             |

None of that comes from the README file itself — the README is what a visitor
reads *after* clicking through from the card. So this skill has two jobs, and
both need to happen for a project to look right: set the GitLab metadata, and
write the README. Don't do one without the other.

## 1. Set the GitLab Description and Topics

Gather real facts about the repo first — don't guess. Check for a language
manifest (`pyproject.toml`, `package.json`, `Cargo.toml`, `go.mod`, ...), an
entry point, and what the project actually does. Then:

**Description** — one plain sentence, no markdown, no trailing period fluff.
This is the card blurb, so it should read like a tagline, not a README intro.

```bash
glab repo update <path/to/project> --description "One-sentence tagline."
```

**Topics** — these render as the badge row on the card, so they're the
"tag with programming languages" mechanism. `glab repo update` has no topics
flag, so set them through the API directly:

```bash
glab api -X PUT "projects/:id" -f "topics=python,reflex,cli"
```

Run that from inside the project's repo (`:id` resolves to the current repo),
or substitute the numeric/URL-encoded project ID.

Topic conventions — keep it to 3-6, most-specific-first:
- Always lead with the primary language(s) actually used (`python`, `typescript`, `rust`) — lowercase, exactly as the language is normally written.
- Follow with the framework or notable library (`reflex`, `fastapi`, `react`).
- Optionally close with a category tag if it clarifies what the thing *is* (`cli`, `discord-bot`, `api`, `chrome-extension`).
- Hyphenate multi-word tags (`discord-bot`, not `discord bot`).
- Don't add a topic you can't justify by pointing at a file in the repo.

Confirm the description and topic list with the user before running the
`glab` commands if there's any ambiguity about what the project actually is —
this is public-facing metadata, not a private convention.

## 2. Write the README

The structure below is adapted from the widely-used
[kopino4-templates/readme-template](https://gitlab.com/kopino4-templates/readme-template),
trimmed down: that template is intentionally exhaustive and written as a
teaching example, but shipping every one of its sections in a real repo is
usually padding. Use `assets/README.template.md` as the starting skeleton, and
delete any section that wouldn't earn its place — a small script doesn't need
a Testing section it doesn't have tests for, and a personal tool doesn't need
a Contributing section if outside contributions aren't wanted.

Sections, in order:

1. **Title + one-line tagline** — the tagline can mirror the GitLab
   Description almost verbatim; it's fine for them to overlap.
2. **Badges** — shields.io badges for license and primary language at
   minimum; add a pipeline/CI badge if the project has one. Don't invent a
   badge for something the repo doesn't actually have (no fake "build:
   passing" badge if there's no CI).
3. **Description** — a short paragraph of *why this exists*, not just what
   it does. One or two sentences past the tagline is usually enough.
4. **Features** — only if there's a genuinely useful short list to give;
   skip it for simple projects rather than padding with obvious bullets.
5. **Getting Started** (Requirements / Install / Usage) — every command here
   must be a real command that works in this repo. Pull it from the actual
   manifest (`pyproject.toml` scripts, `package.json` scripts, `Makefile`,
   `Cargo.toml`) — never invent an install or run command.
6. **Tech Stack** — only include this if the stack isn't obvious from the
   badges/title, or if it's a heterogeneous project worth explaining.
7. **Testing** — only if tests exist; give the actual command to run them.
8. **Contributing** — short, only for projects meant to accept outside
   contributions. Skip it for personal/portfolio projects.
9. **License** — mirror whatever `LICENSE` file is actually in the repo. If
   there isn't one, ask the user whether to add one (MIT is the common
   default for this account's public projects) rather than assuming.

Don't reintroduce the template's own meta sections ("Here is where it's your
turn", "Don't forget anything", "Conclusion") — those are the upstream
template talking about itself, not real README content.

## Workflow

1. Read the repo: language/framework, entry point, actual install/run/test
   commands, existing LICENSE.
2. Confirm the Description tagline and Topics list with the user if not
   obvious.
3. Apply the GitLab metadata (`glab repo update` + `glab api` topics call).
4. Write `README.md` from `assets/README.template.md`, keeping only the
   sections that earn their place, with every command verified against the
   repo.
5. Show the user the resulting README and the topics/description you set —
   this is public-facing, so a quick confirm before considering it done is
   worth it.
