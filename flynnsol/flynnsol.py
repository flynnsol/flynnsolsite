"""App entry point. Pages register themselves via @rx.page decorators, fired
by importing flynnsol.pages in flynnsol/__init__.py."""

import reflex as rx

app = rx.App(
    stylesheets=["/styles.css"],
    head_components=[
        rx.el.link(rel="icon", type="image/png", href="/favicon.png"),
    ],
)
