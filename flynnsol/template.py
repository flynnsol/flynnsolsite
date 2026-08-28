"""Shared page shell: navbar + content container + footer.

Usage (order matters — @rx.page registers the already-templated function):

    @rx.page(route="/", title="Flynn Sol")
    @template
    def index() -> rx.Component:
        ...
"""

import functools

import reflex as rx

from .components.footer import footer
from .components.navbar import navbar
from .styles import CREAM, FONT_FAMILY, GOLD, NAVY, TEXT, page_container_style


def template(page):
    @functools.wraps(page)
    def wrapper(*args, **kwargs) -> rx.Component:
        return rx.box(
            navbar(),
            rx.box(page(*args, **kwargs), style=page_container_style),
            footer(),
            background=rx.color_mode_cond(light=CREAM, dark=NAVY),
            color=TEXT,
            min_height="100vh",
            font_family=FONT_FAMILY,
            background_image=rx.color_mode_cond(
                light="none",
                dark=f"radial-gradient(ellipse 900px 500px at 90% -10%, {GOLD}1A, transparent 60%)",
            ),
            background_repeat="no-repeat",
        )

    return wrapper
