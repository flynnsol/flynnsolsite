"""GitHub project fetch for the Projects page.

Loading/error/empty states are handled explicitly so a network hiccup (or the
fact that this repo is currently the only public GitHub project) never
crashes the page.
"""

from datetime import datetime, timezone
from typing import TypedDict

import httpx
import reflex as rx

GITHUB_USERNAME = "flynnsol"
GITHUB_API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
GITHUB_PROFILE_URL = f"https://github.com/{GITHUB_USERNAME}"


class ProjectDict(TypedDict):
    """Normalized shape stored in state — a concrete type (not plain `dict`)
    so `rx.foreach` can resolve the `topics` list's element type."""

    name: str
    description: str
    url: str
    stars: int
    updated: str
    topics: list[str]


def _relative_time(iso_timestamp: str) -> str:
    try:
        then = datetime.fromisoformat(iso_timestamp.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return "recently"
    days = (datetime.now(timezone.utc) - then).days
    if days < 1:
        return "today"
    if days < 30:
        return f"{days}d ago"
    if days < 365:
        return f"{days // 30}mo ago"
    return f"{days // 365}y ago"


class ProjectsState(rx.State):
    """Public GitHub repos, fetched live on page load."""

    projects: list[ProjectDict] = []
    is_loading: bool = True
    has_error: bool = False

    @rx.event
    async def load_projects(self):
        self.is_loading = True
        self.has_error = False
        yield
        try:
            async with httpx.AsyncClient(timeout=8.0) as client:
                resp = await client.get(
                    GITHUB_API_URL,
                    params={"type": "owner", "sort": "pushed", "per_page": 100},
                    headers={"Accept": "application/vnd.github+json"},
                )
                resp.raise_for_status()
                raw_projects = resp.json()
        except (httpx.HTTPError, ValueError):
            self.has_error = True
            self.projects = []
        else:
            self.projects = [
                {
                    "name": p.get("name", "Untitled"),
                    "description": p.get("description") or "No description yet.",
                    "url": p.get("html_url", GITHUB_PROFILE_URL),
                    "stars": p.get("stargazers_count", 0),
                    "updated": _relative_time(p.get("pushed_at", "")),
                    "topics": p.get("topics") or [],
                }
                for p in raw_projects
                if not p.get("fork") and not p.get("archived")
            ]
        finally:
            self.is_loading = False
