"""The split-F logo mark. Renders as two clipped layers of the same SVG so the
two halves can animate into place independently on the hero, while staying a
single static mark everywhere else (e.g. the navbar)."""

import reflex as rx

_UP_CLIP = "polygon(0% 0%, 100% 0%, 100% 13%, 0% 65%)"
_DOWN_CLIP = "polygon(0% 68%, 100% 16%, 100% 100%, 0% 100%)"


def logo_mark(size: str = "32px", animated: bool = False) -> rx.Component:
    src = rx.color_mode_cond(light="/mark-on-light.svg", dark="/mark-on-dark.svg")
    return rx.box(
        rx.image(
            src=src,
            width=size,
            height=size,
            position="absolute",
            top="0",
            left="0",
            style={"clip_path": _UP_CLIP},
            class_name="hero-half-up" if animated else "",
        ),
        rx.image(
            src=src,
            width=size,
            height=size,
            position="absolute",
            top="0",
            left="0",
            style={"clip_path": _DOWN_CLIP},
            class_name="hero-half-down" if animated else "",
        ),
        position="relative",
        width=size,
        height=size,
        display="inline-block",
        flex_shrink="0",
    )
