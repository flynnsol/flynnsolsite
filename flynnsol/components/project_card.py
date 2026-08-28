"""GitLab project card, plus a matching skeleton for the loading state.

`project` is a State-backed dict Var (from ProjectsState.projects), normalized
in ProjectsState.load_projects to always have: name, description, url, stars,
updated, topics.
"""

import reflex as rx

from ..styles import GOLD, TEXT, TEXT_77, TEXT_CC, card_style, gold_soft_style


def project_card(project: rx.Var) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading(project["name"], size="4", color=TEXT),
                rx.spacer(),
                rx.hstack(
                    rx.icon("star", size=14, color=GOLD),
                    rx.text(project["stars"].to_string(), size="2", color=GOLD),
                    spacing="1",
                    align="center",
                ),
                width="100%",
                align="center",
            ),
            rx.text(project["description"], color=TEXT_CC, size="3"),
            rx.hstack(
                rx.foreach(
                    project["topics"],
                    lambda topic: rx.badge(topic, style=gold_soft_style),
                ),
                spacing="2",
                wrap="wrap",
            ),
            rx.hstack(
                rx.text(
                    f"Updated {project['updated']}",
                    size="2",
                    color=TEXT_77,
                ),
                rx.spacer(),
                rx.link(
                    rx.hstack(
                        rx.text("View on GitLab", size="2"),
                        rx.icon("arrow-up-right", size=14),
                        spacing="1",
                        align="center",
                    ),
                    href=project["url"],
                    is_external=True,
                    color=GOLD,
                    underline="none",
                ),
                width="100%",
                align="center",
            ),
            spacing="3",
            align="start",
            width="100%",
        ),
        style=card_style,
        width="100%",
    )


def project_card_skeleton() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.skeleton(rx.box(height="1.5em", width="40%")),
            rx.skeleton(rx.box(height="1em", width="90%")),
            rx.skeleton(rx.box(height="1em", width="70%")),
            rx.skeleton(rx.box(height="1.5em", width="30%")),
            spacing="3",
            width="100%",
        ),
        style=card_style,
        width="100%",
    )
