"""Theme toggle: a small gold dot that sits beside the "Flynn Sol" wordmark —
solid in dark mode, hollow in light mode. Deliberately understated rather
than a separate widget competing with the nav's icons/links."""

import reflex as rx

from ..styles import GOLD


def theme_toggle() -> rx.Component:
    return rx.box(
        id="theme-toggle-btn",
        on_click=rx.toggle_color_mode,
        title="Toggle light/dark mode",
        width="9px",
        height="9px",
        border_radius="999px",
        border=f"1.5px solid {GOLD}",
        background=rx.color_mode_cond(light="transparent", dark=GOLD),
        cursor="pointer",
        flex_shrink="0",
        style={"transition": "background 0.25s ease, transform 0.15s ease"},
        _hover={"transform": "scale(1.35)"},
    )
