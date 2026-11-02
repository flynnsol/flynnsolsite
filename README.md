# flynnsol

Flynn Sol's personal portfolio site — resume, blog, and projects, built with [Reflex](https://reflex.dev).

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Reflex](https://img.shields.io/badge/framework-Reflex-8A2BE2.svg)

## Description

This is the source for [flynnsol.com](https://flynnsol.com) — a full-stack Python site built entirely with Reflex, no separate frontend framework. It exists both as a personal site and as a live demo of the stack: the Projects page fetches directly from the GitHub API at request time, so this repo showing up there is the project working as intended.

## Features

- **Live Projects page** — pulls name, description, topics, stars, and last-activity straight from the GitHub API, no manual syncing.
- **File-based blog** — posts are markdown with frontmatter, parsed once at import time and filterable by tag.
- **Resume page** — structured work history/skills data rendered as a page, shared with the home page bio.
- **Light/dark theme** with a custom Radix Themes palette (amber accent, slate gray).

## Getting Started

### Requirements

- Python 3.12+
- [Reflex](https://reflex.dev) (installed via `requirements.txt`; Reflex manages its own Node/Bun toolchain for the frontend build)

### Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
reflex init
```

### Usage

```bash
reflex run
```

The app serves the frontend at `http://localhost:3000` and the backend at `http://localhost:8000`.

## Tech Stack

- **[Reflex](https://reflex.dev)** — Python framework compiling to a React frontend + FastAPI backend, single codebase.
- **Tailwind CSS v4** and **Radix Themes**, via Reflex plugins.
- **httpx** for the live GitHub API calls behind the Projects page.
- **python-frontmatter** for parsing the markdown blog posts.

## License

[MIT](https://choosealicense.com/licenses/mit/)
