"""A small pill badge for a skill/tag, used on the Resume and Blog pages."""

import reflex as rx

from ..styles import skill_chip_style


def skill_chip(label: str) -> rx.Component:
    return rx.box(rx.text(label, as_="span"), style=skill_chip_style)
