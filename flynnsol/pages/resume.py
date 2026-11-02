"""Resume page: full structured resume, sourced from data/resume.py."""

import reflex as rx

from ..components.skill_chip import skill_chip
from ..components.timeline import timeline_entry
from ..data.resume import RESUME
from ..styles import GOLD, TEXT, TEXT_99, TEXT_CC, outline_button_hover
from ..template import template


@rx.page(route="/resume", title="Resume — Flynn Sol")
@template
def resume() -> rx.Component:
    return rx.vstack(
        rx.heading("Resume", size="8", color=TEXT),
        rx.text(
            RESUME.summary,
            color=TEXT_CC,
            size="4",
            line_height="1.6",
            margin_bottom="1em",
        ),
        rx.hstack(
            rx.link(
                rx.button("Email me", variant="surface", style=outline_button_hover),
                href=f"mailto:{RESUME.email}",
            ),
            rx.link(
                rx.button("GitHub", variant="surface", style=outline_button_hover),
                href=f"https://{RESUME.github}",
                is_external=True,
            ),
            spacing="3",
            margin_bottom="2.5em",
            wrap="wrap",
        ),
        rx.heading("Experience", size="6", color=GOLD, margin_bottom="1em"),
        *[timeline_entry(block, i) for i, block in enumerate(RESUME.experience)],
        rx.heading("Education", size="6", color=GOLD, margin_top="1em", margin_bottom="1em"),
        *[
            rx.box(
                rx.text(edu.school, weight="bold", color=TEXT, size="4"),
                rx.text(f"{edu.program} · {edu.dates}", color=TEXT_99, size="3"),
                margin_bottom="1em",
            )
            for edu in RESUME.education
        ],
        rx.heading(
            "Certifications", size="6", color=GOLD, margin_top="1em", margin_bottom="1em"
        ),
        *[
            rx.box(
                rx.text(cert.name, weight="bold", color=TEXT, size="4"),
                rx.text(f"{cert.issuer} · {cert.date}", color=TEXT_99, size="3"),
                margin_bottom="1em",
            )
            for cert in RESUME.certifications
        ],
        rx.heading("Skills", size="6", color=GOLD, margin_top="1em", margin_bottom="1em"),
        rx.flex(*[skill_chip(s) for s in RESUME.skills], wrap="wrap", gap="0.6em"),
        spacing="2",
        align="start",
        width="100%",
    )
