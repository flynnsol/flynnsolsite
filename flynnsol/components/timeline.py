"""Resume experience timeline: a company block with nested roles, stagger-fades
in on page load. Resume content is static Python data (not State), so this is
plain composition — no Vars/rx.cond needed."""

import reflex as rx

from ..data.resume import CompanyBlock, Role
from ..styles import GOLD, TEXT, TEXT_77, TEXT_CC


def _role(role: Role, delay: float) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(role.title, weight="bold", color=TEXT, size="4"),
            rx.spacer(),
            rx.text(
                f"{role.start} – {role.end}",
                color=GOLD,
                size="2",
                white_space="nowrap",
            ),
            width="100%",
            align="baseline",
        ),
        rx.list.unordered(
            *[rx.list.item(b, color=TEXT_CC, size="3") for b in role.bullets],
            margin_top="0.5em",
            spacing="1",
        ),
        margin_bottom="1.25em",
        class_name="fade-in-up",
        style={"--delay": f"{delay}s"},
    )


def timeline_entry(block: CompanyBlock, index: int) -> rx.Component:
    header_children = [rx.heading(block.company, size="5", color=TEXT)]
    if block.location:
        header_children.append(
            rx.text(f"· {block.location}", color=TEXT_77, size="3")
        )
    return rx.box(
        rx.hstack(
            rx.box(
                width="8px",
                height="8px",
                min_width="8px",
                border_radius="999px",
                background=GOLD,
                margin_top="0.6em",
            ),
            rx.vstack(
                rx.hstack(*header_children, spacing="2", align="baseline"),
                *[_role(r, index * 0.12 + i * 0.06) for i, r in enumerate(block.roles)],
                align="start",
                width="100%",
                spacing="2",
            ),
            align="start",
            spacing="4",
            width="100%",
        ),
        border_left=f"2px solid {GOLD}33",
        padding_left="1.5em",
        margin_bottom="2em",
        class_name="fade-in-up",
        style={"--delay": f"{index * 0.12}s"},
    )
