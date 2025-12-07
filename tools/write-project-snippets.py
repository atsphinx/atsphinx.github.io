"""Sync package information from https://github.com/atsphin/ ."""

import logging
import os
import textwrap
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

import dotenv
from github import Auth, Github
from jinja2 import Template

if TYPE_CHECKING:
    from typing import Self

    from github.Repository import Repository

EXCLUDE_REPOS = [
    ".github",  # Organization profile
    "atsphinx.github.io",  # Pages repository
    "cookiecutter-sphinx-extension",  # Template
    "buildtime",
    "demo",
    "helper",  # Not Sphinx extensions
    "reveal-og-image",  # Not yet released
    "revealjs-design",
    "revealjs-rtd",
    "revealjs-toybox",
    "picocss",
    "powersearch",
    "revealjs-desktop",
    "sandbox",
    "semantic-html",
    "test20251130",
]

TEMPLATES = {
    "contents/_snippets/packages.rst": """
        .. |LAST_FETCHED| replace:: {{ now.strftime('%Y-%m-%d') }}

        .. grid:: 2
        {% for proj in projects %}
            .. grid-item-card:: {{ proj.name }} {{ proj.version }}

                {{ proj.description }}
                +++
                {{ proj.released_at.strftime('%Y-%m-%d') }} / {{ proj.stargazers_count }} star(s)
                /
                `PyPI <https://pypi.org/project/atsphinx-{{ proj.name }}>`_
                /
                `Repo <https://github.com/atsphinx/{{ proj.name }}>`_
        {% endfor -%}
        """,
}

logger = logging.getLogger(__name__)


@dataclass
class Project:  # noqa: D101
    name: str
    description: str
    stargazers_count: int
    version: str
    released_at: datetime

    @classmethod
    def from_repo(cls, repo: Repository) -> Self:  # noqa: D102
        release = repo.get_latest_release()
        return cls(
            name=repo.name,
            description=repo.description or "(None description)",
            stargazers_count=repo.stargazers_count,
            version=release.tag_name,
            released_at=release.created_at,
        )


def main():  # noqa: D103
    now = datetime.now()
    auth = Auth.Token(os.environ["GITHUB_TOKEN"])
    org = Github(auth=auth).get_organization("atsphinx")
    projects = []
    for repo in org.get_repos():
        if repo.name in EXCLUDE_REPOS:
            continue
        projects.append(Project.from_repo(repo))
    for dest, template in TEMPLATES.items():
        dest = Path(dest)
        tmpl = Template(textwrap.dedent(template).strip())
        dest.write_text(tmpl.render(now=now, projects=projects))


if __name__ == "__main__":
    dotenv.load_dotenv()
    if "LOGGING_LEVEL" in os.environ:
        loglevel = os.environ["LOGGING_LEVEL"]
        if loglevel in logging.getLevelNamesMapping():
            logging.basicConfig(level=logging.getLevelNamesMapping()[loglevel])
    logger.debug("START")
    main()
    logger.debug("END")
