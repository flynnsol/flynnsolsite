"""Blog index: lists posts newest-first, filterable by tag. Posts themselves
are static data parsed at import time in states/blog_state.py; BlogListState
only tracks which tag chip is selected and narrows that static list.
"""

import reflex as rx

from ..components.post_preview import post_preview
from ..states.blog_state import ALL_TAGS, BlogListState
from ..styles import GOLD, NAVY, TEXT, TEXT_99, skill_chip_style
from ..template import template


def _tag_chip(tag: str, label: str | None = None) -> rx.Component:
    is_active = BlogListState.selected_tag == tag
    return rx.badge(
        label or tag,
        on_click=BlogListState.set_tag(tag),
        style={
            **skill_chip_style,
            "cursor": "pointer",
            "background": rx.cond(is_active, GOLD, skill_chip_style["background"]),
            "color": rx.cond(is_active, NAVY, GOLD),
        },
    )


@rx.page(route="/blog", title="Blog — Flynn Sol")
@template
def blog() -> rx.Component:
    return rx.vstack(
        rx.heading("Blog", size="8", color=TEXT, margin_bottom="0.25em"),
        rx.text(
            "My thoughts on engineering, tech, and life.",
            color=TEXT_99,
            margin_bottom="1.5em",
        ),
        rx.hstack(
            _tag_chip("", label="All"),
            *[_tag_chip(tag) for tag in ALL_TAGS],
            spacing="2",
            wrap="wrap",
            margin_bottom="1em",
        ),
        rx.foreach(
            BlogListState.filtered_posts,
            lambda post, i: rx.box(
                post_preview(post),
                width="100%",
                class_name="fade-in-up",
                style={"--delay": f"{i * 0.08}s"},
            ),
        ),
        spacing="4",
        align="start",
        width="100%",
    )
