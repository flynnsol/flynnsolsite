"""Blog post loading.

Posts are markdown files with frontmatter, committed to the repo — content is
static at deploy time, so all posts are parsed once at import time rather than
per-request. BlogState only resolves the current /blog/[slug] route param
against that pre-parsed index.
"""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import TypedDict

import frontmatter
import reflex as rx

POSTS_DIR = Path(__file__).resolve().parent.parent.parent / "posts"


def _format_date(iso_date: str) -> str:
    """"2026-08-24" -> "August 24th, 2026"."""
    try:
        dt = datetime.strptime(iso_date, "%Y-%m-%d")
    except ValueError:
        return iso_date
    day = dt.day
    suffix = "th" if 11 <= day % 100 <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    return f"{dt.strftime('%B')} {day}{suffix}, {dt.year}"


@dataclass(frozen=True)
class Post:
    slug: str
    title: str
    date: str  # raw ISO (e.g. "2026-08-24") — used for sorting
    display_date: str  # human-readable (e.g. "August 24th, 2026")
    summary: str
    tags: list[str]
    content: str


def _load_all_posts() -> list[Post]:
    if not POSTS_DIR.exists():
        return []
    posts = []
    for path in sorted(POSTS_DIR.glob("*.md")):
        fm = frontmatter.load(path)
        raw_date = str(fm.get("date", ""))
        posts.append(
            Post(
                slug=fm.get("slug", path.stem),
                title=fm.get("title", path.stem),
                date=raw_date,
                display_date=_format_date(raw_date),
                summary=fm.get("summary", ""),
                tags=list(fm.get("tags", [])),
                content=fm.content,
            )
        )
    posts.sort(key=lambda p: p.date, reverse=True)
    return posts


ALL_POSTS: list[Post] = _load_all_posts()
POSTS_BY_SLUG: dict[str, Post] = {p.slug: p for p in ALL_POSTS}


class PostSummary(TypedDict):
    """Normalized shape for anything that renders a post preview — a concrete
    type (not plain `dict`) so `rx.foreach` can resolve the `tags` list's
    element type, matching the ProjectDict pattern in projects_state.py."""

    slug: str
    title: str
    display_date: str
    summary: str
    tags: list[str]


def _summarize(post: Post) -> PostSummary:
    return {
        "slug": post.slug,
        "title": post.title,
        "display_date": post.display_date,
        "summary": post.summary,
        "tags": post.tags,
    }


ALL_POST_SUMMARIES: list[PostSummary] = [_summarize(p) for p in ALL_POSTS]
ALL_TAGS: list[str] = sorted({tag for post in ALL_POSTS for tag in post.tags})


class BlogListState(rx.State):
    """Tag filter for the /blog index. Posts are static (parsed at import
    time above), so filtering just narrows ALL_POST_SUMMARIES in-memory —
    no fetch/loading state needed."""

    selected_tag: str = ""

    @rx.event
    def set_tag(self, tag: str):
        self.selected_tag = tag

    @rx.var
    def filtered_posts(self) -> list[PostSummary]:
        if not self.selected_tag:
            return ALL_POST_SUMMARIES
        return [p for p in ALL_POST_SUMMARIES if self.selected_tag in p["tags"]]


class BlogState(rx.State):
    """Resolves the current /blog/[slug] route param to post fields.

    `slug` itself is not declared here — Reflex auto-populates a var of that
    name on this state because the page route is /blog/[slug].
    """

    @rx.var
    def post_found(self) -> bool:
        return self.slug in POSTS_BY_SLUG

    @rx.var
    def post_title(self) -> str:
        post = POSTS_BY_SLUG.get(self.slug)
        return post.title if post else "Post not found"

    @rx.var
    def post_date(self) -> str:
        post = POSTS_BY_SLUG.get(self.slug)
        return post.display_date if post else ""

    @rx.var
    def post_tags(self) -> list[str]:
        post = POSTS_BY_SLUG.get(self.slug)
        return post.tags if post else []

    @rx.var
    def post_content(self) -> str:
        post = POSTS_BY_SLUG.get(self.slug)
        return post.content if post else ""
