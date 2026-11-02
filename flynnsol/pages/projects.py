"""Projects page: live GitHub-sourced project cards, with explicit
loading / error / empty states so the page never breaks on a network hiccup
or on the (currently true) fact that there are zero public repos yet.
"""

import reflex as rx

from ..components.project_card import project_card, project_card_skeleton
from ..states.projects_state import GITHUB_PROFILE_URL, ProjectsState
from ..styles import GOLD, TEXT, TEXT_99, outline_button_hover
from ..template import template


def _empty_state() -> rx.Component:
    return rx.vstack(
        rx.icon("folder_git_2", size=40, color=GOLD),
        rx.heading("No public projects yet", size="5", color=TEXT),
        rx.text(
            "This site is the first one — check back soon, or see what's cooking on GitHub.",
            color=TEXT_99,
            text_align="center",
        ),
        rx.link(
            rx.button(
                "Visit GitHub profile",
                variant="surface",
                style=outline_button_hover,
            ),
            href=GITHUB_PROFILE_URL,
            is_external=True,
        ),
        spacing="3",
        align="center",
        padding="4em 0",
        width="100%",
    )


def _error_state() -> rx.Component:
    return rx.vstack(
        rx.icon("wifi_off", size=40, color=GOLD),
        rx.heading("Couldn't reach GitHub", size="5", color=TEXT),
        rx.text(
            "Something went wrong fetching projects — try again in a moment.",
            color=TEXT_99,
        ),
        rx.button(
            "Retry",
            on_click=ProjectsState.load_projects,
            variant="surface",
            style=outline_button_hover,
        ),
        spacing="3",
        align="center",
        padding="4em 0",
        width="100%",
    )


@rx.page(
    route="/projects",
    title="Projects — Flynn Sol",
    on_load=ProjectsState.load_projects,
)
@template
def projects() -> rx.Component:
    return rx.vstack(
        rx.heading("Projects", size="8", color=TEXT),
        rx.text(
            "Pulled live from my GitHub profile.",
            color=TEXT_99,
            margin_bottom="1.5em",
        ),
        rx.cond(
            ProjectsState.is_loading,
            rx.vstack(
                *[project_card_skeleton() for _ in range(3)],
                spacing="4",
                width="100%",
            ),
            rx.cond(
                ProjectsState.has_error,
                _error_state(),
                rx.cond(
                    ProjectsState.projects.length() == 0,
                    _empty_state(),
                    rx.vstack(
                        rx.foreach(
                            ProjectsState.projects,
                            lambda project, i: rx.box(
                                project_card(project),
                                width="100%",
                                class_name="fade-in-up",
                                style={"--delay": f"{i * 0.08}s"},
                            ),
                        ),
                        spacing="4",
                        width="100%",
                    ),
                ),
            ),
        ),
        spacing="2",
        align="start",
        width="100%",
    )
