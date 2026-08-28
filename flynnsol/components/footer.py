"""Footer: social/contact links and a small tagline."""

import reflex as rx

from ..data.resume import RESUME
from ..styles import GOLD, TEXT, TEXT_77
from .brand_icons import github_icon, gitlab_icon


def _social_link(icon: rx.Component, label: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            icon,
            rx.text(label, color=TEXT, size="3"),
            spacing="2",
            align="center",
        ),
        href=href,
        is_external=True,
        underline="none",
        class_name="social-link",
    )


def footer() -> rx.Component:
    return rx.box(
        rx.divider(border_color=f"{GOLD}22"),
        rx.box(
            rx.vstack(
                rx.hstack(
                    _social_link(github_icon(size=18, color=TEXT), "GitHub", f"https://{RESUME.github}"),
                    _social_link(gitlab_icon(size=18, color=TEXT), "GitLab", f"https://{RESUME.gitlab}"),
                    _social_link(rx.icon("mail", size=18, color=TEXT), "Email", f"mailto:{RESUME.email}"),
                    spacing="6",
                    wrap="wrap",
                    justify="center",
                ),
                rx.text(
                    f"© {RESUME.name}",
                    size="2",
                    color=TEXT_77,
                ),
                spacing="4",
                align="center",
                padding_top="2em",
                padding_bottom="3em",
            ),
            max_width="980px",
            margin="0 auto",
            padding="0 1.5em",
            width="100%",
        ),
        width="100%",
    )
