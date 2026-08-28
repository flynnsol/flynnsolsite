"""Blog post preview card, shared by the blog index and the home page's
latest-post section.

`post` is a PostSummary (see states/blog_state.py) — either a plain dict
(index.py, resolved at compile time) or a State-backed dict Var (blog.py's
BlogListState.filtered_posts), so it's accessed with bracket notation
throughout to work for both.
"""

import reflex as rx

from ..styles import TEXT, TEXT_77, TEXT_CC, card_style, gold_soft_style


def post_preview(post) -> rx.Component:
    return rx.link(
        rx.box(
            rx.hstack(
                rx.heading(post["title"], size="5", color=TEXT),
                rx.spacer(),
                rx.text(post["display_date"], size="2", color=TEXT_77),
                width="100%",
                align="baseline",
            ),
            rx.text(post["summary"], color=TEXT_CC, size="3", margin_top="0.5em"),
            rx.hstack(
                rx.foreach(post["tags"], lambda t: rx.badge(t, style=gold_soft_style)),
                spacing="2",
                margin_top="0.75em",
                wrap="wrap",
            ),
            style=card_style,
            width="100%",
        ),
        href=f"/blog/{post['slug']}",
        underline="none",
        width="100%",
    )
