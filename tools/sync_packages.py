"""Sync package information from https://github.com/atsphin/ ."""

import logging
import os
import textwrap
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path

import dotenv
from github import Auth, Github
from jinja2 import Template

ROOT = Path(__file__).parent.parent
CONTENTS_ROOT = ROOT / "contents"

logger = logging.getLogger(__name__)


@dataclass
class RepoData:
    """Dataset of repository to render on Jinja2."""

    name: str
    url: str
    version: str
    description: str
    updated_at: datetime


@dataclass
class Context:
    """Document context."""

    updated_at: datetime
    repos: list[RepoData]
    grid_num: int = 2


def fetch_repos(client: Github) -> list[RepoData]:
    """Fetch package repositories from org."""
    NOT_PACKAGES = [
        "atsphinx.github.io",
        "cookiecutter-sphinx-extension",
        "helper",
        "demo",
        "buildtime",
    ]
    repos = []
    for r in client.get_organization("atsphinx").get_repos(
        type="public", sort="pushed", direction="desc"
    ):
        if r.name in NOT_PACKAGES:
            continue
        logger.info(f"Get context of {r.full_name}")
        version = r.get_latest_release().tag_name
        description = r.description or "(None description)"
        repos.append(RepoData(r.name, r.html_url, version, description, r.updated_at))
    return repos


def write_document(target: Path, ctx: Context):
    """Write out reST file from repositories."""
    template = Template(
        textwrap.dedent(
            """\
        ============
        All packages
        ============

        :Updated: {{ updated_at.strftime('%Y-%m-%d') }}

        List of packages published on PyPI.

        .. grid:: {{ grid_num }}

           {% for repo in repos -%}
           .. grid-item-card:: {{ repo.name }} {{ repo.version }}

              {{ repo.description or '(None description)' }}
              +++
              {{ repo.updated_at.strftime('%Y-%m-%d') }}
              /
              `Repo <{{ repo.url }}>`_

           {% endfor -%}
    """
        )
    )
    target.write_text(template.render(**asdict(ctx)).strip() + "\n")


def main():  # noqa: D103
    now = datetime.now()
    auth = Auth.Token(os.environ["GITHUB_PAT"])
    client = Github(auth=auth)
    repos = fetch_repos(client)
    for r in repos:
        if r.description is None:
            logger.warning(f"{r.name} is not set description")
    ctx = Context(now, repos)
    write_document(CONTENTS_ROOT / "packages.rst", ctx)


if __name__ == "__main__":
    dotenv.load_dotenv()
    main()
