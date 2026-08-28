"""Individual blog post page: /blog/[slug]."""

import reflex as rx

from ..states.blog_state import BlogState
from ..styles import GOLD, TEXT, TEXT_77, TEXT_99, gold_soft_style, outline_button_hover
from ..template import template


def _not_found() -> rx.Component:
    return rx.vstack(
        rx.heading("Post not found", size="7", color=TEXT),
        rx.text(
            "That one doesn't exist — maybe it moved, or maybe it was never here.",
            color=TEXT_99,
        ),
        rx.link(
            rx.button(
                "Back",
                variant="surface",
                style=outline_button_hover,
            ),
            href="/blog",
        ),
        spacing="3",
        align="center",
        padding="4em 0",
        width="100%",
    )


def _post_view() -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.text("← Back", color=GOLD), href="/blog", margin_bottom="1em"
        ),
        rx.heading(BlogState.post_title, size="8", color=TEXT),
        rx.text(BlogState.post_date, color=TEXT_77, size="3", margin_bottom="0.5em"),
        rx.hstack(
            rx.foreach(
                BlogState.post_tags,
                lambda t: rx.badge(t, style=gold_soft_style),
            ),
            spacing="2",
            margin_bottom="1.5em",
        ),
        rx.box(rx.markdown(BlogState.post_content), width="100%"),
        align="start",
        width="100%",
    )


@rx.page(route="/blog/[slug]", title="Blog — Flynn Sol")
@template
def blog_post() -> rx.Component:
    return rx.cond(BlogState.post_found, _post_view(), _not_found())
