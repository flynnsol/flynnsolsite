"""Top navigation: logo, page links, active-route indicator, and theme toggle."""

import reflex as rx

from ..styles import GOLD, NAV_BG, TEXT
from .logo import logo_mark
from .theme_toggle import theme_toggle

NAV_LINKS = [
    ("Home", "/"),
    ("Resume", "/resume"),
    ("Blog", "/blog"),
    ("Projects", "/projects"),
]


def _is_active(path: rx.Var, href: str) -> rx.Var:
    if href == "/":
        return path == href
    return path.contains(href)


def _nav_link(label: str, href: str) -> rx.Component:
    active = _is_active(rx.State.router.url.path, href)
    return rx.link(
        rx.vstack(
            rx.text(
                label,
                size="3",
                weight="medium",
                color=rx.cond(active, GOLD, TEXT),
                style={"transition": "color 0.2s ease"},
            ),
            rx.cond(
                active,
                rx.box(height="2px", width="100%", background=GOLD, class_name="nav-underline"),
                rx.box(height="2px", width="100%", background="transparent"),
            ),
            spacing="1",
            align="center",
        ),
        href=href,
        underline="none",
        _hover={"opacity": "0.85"},
    )


def navbar() -> rx.Component:
    links = rx.hstack(
        *[_nav_link(label, href) for label, href in NAV_LINKS],
        spacing="6",
        display=["none", "none", "none", "flex"],
    )

    mobile_menu = rx.box(
        rx.menu.root(
            rx.menu.trigger(
                rx.icon_button(
                    rx.icon("menu"),
                    variant="ghost",
                    color_scheme="gray",
                    style={"cursor": "pointer"},
                ),
            ),
            rx.menu.content(
                *[
                    rx.menu.item(label, on_click=rx.redirect(href))
                    for label, href in NAV_LINKS
                ],
            ),
        ),
        display=["flex", "flex", "flex", "none"],
    )

    return rx.box(
        rx.box(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.hstack(
                            logo_mark(size="32px"),
                            rx.text("Flynn Sol", weight="bold", size="4", color=TEXT),
                            spacing="2",
                            align="center",
                        ),
                        href="/",
                        underline="none",
                    ),
                    theme_toggle(),
                    spacing="2",
                    align="center",
                ),
                rx.spacer(),
                links,
                mobile_menu,
                align="center",
                width="100%",
                padding="1.25em 0",
            ),
            max_width="980px",
            margin="0 auto",
            padding="0 1.5em",
            width="100%",
        ),
        position="sticky",
        top="0",
        z_index="10",
        width="100%",
        background=NAV_BG,
        backdrop_filter="blur(8px)",
        border_bottom=f"1px solid {GOLD}22",
    )
