"""Importing each page module fires its @rx.page decorator, registering the
route. Static routes are imported before the dynamic /blog/[slug] route."""

from . import index  # noqa: F401
from . import resume  # noqa: F401
from . import projects  # noqa: F401
from . import blog  # noqa: F401
from . import blog_post  # noqa: F401
