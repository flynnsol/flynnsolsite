"""Home page: hero with the animated logo mark + a quick bio."""

import reflex as rx

from ..components.logo import logo_mark
from ..components.post_preview import post_preview
from ..components.project_card import project_card, project_card_skeleton
from ..data.resume import RESUME
from ..states.blog_state import ALL_POST_SUMMARIES
from ..states.projects_state import ProjectsState
from ..styles import GOLD, TEXT, TEXT_99, TEXT_DD, gold_soft_style, outline_button_hover
from ..template import template


def _section(title: str, view_all_href: str, content: rx.Component) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading(title, size="6", color=TEXT),
            rx.spacer(),
            rx.link(
                rx.hstack(
                    rx.text("View all", size="2"),
                    rx.icon("arrow-right", size=14),
                    spacing="1",
                    align="center",
                ),
                href=view_all_href,
                color=GOLD,
                underline="none",
            ),
            width="100%",
            align="center",
        ),
        content,
        spacing="3",
        align="start",
        width="100%",
        max_width="620px",
        margin_top="3em",
    )


def _latest_post_section() -> rx.Component:
    if not ALL_POST_SUMMARIES:
        return rx.fragment()
    return _section("Latest post", "/blog", post_preview(ALL_POST_SUMMARIES[0]))


def _latest_project_section() -> rx.Component:
    # ProjectsState.load_projects requests projects ordered by last_activity_at,
    # so the first entry is always the most recently updated one.
    return _section(
        "Latest project",
        "/projects",
        rx.cond(
            ProjectsState.is_loading,
            project_card_skeleton(),
            rx.cond(
                ProjectsState.has_error | (ProjectsState.projects.length() == 0),
                rx.text("No projects to show right now.", color=TEXT_99),
                project_card(ProjectsState.projects[0]),
            ),
        ),
    )


@rx.page(
    route="/",
    title="Flynn Sol — Software Engineer",
    on_load=ProjectsState.load_projects,
)
@template
def index() -> rx.Component:
    return rx.vstack(
        rx.box(height="4vh"),
        logo_mark(size="96px", animated=True),
        rx.heading(RESUME.name, size="9", color=TEXT, margin_top="0.75em"),
        rx.text(RESUME.title, size="5", color=GOLD, weight="medium"),
        rx.badge(RESUME.status, style=gold_soft_style, margin_top="0.5em"),
        rx.text(
            RESUME.short_bio,
            size="5",
            color=TEXT_DD,
            text_align="center",
            max_width="620px",
            margin_top="1.5em",
            line_height="1.6",
        ),
        rx.hstack(
            rx.link(
                rx.button("Resume", size="3", variant="surface", style=outline_button_hover),
                href="/resume",
            ),
            spacing="4",
            margin_top="2em",
            wrap="wrap",
            justify="center",
        ),
        _latest_post_section(),
        _latest_project_section(),
        spacing="3",
        align="center",
        justify="center",
        min_height="70vh",
        width="100%",
    )
