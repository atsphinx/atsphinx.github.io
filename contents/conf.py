# noqa: D100

import os

import dotenv

dotenv.load_dotenv()

# -- Project information
project = "atsphinx"
copyright = "2023, Kazuya Takei"
author = "Kazuya Takei"
release = "2023.5.1"
version = release

# -- General configuration
extensions = []
extensions = [
    "atsphinx.color_text",
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
    "sphinx_design",
]
templates_path = ["_templates"]
exclude_patterns = []

# For i18n
language = "en"
locale_dirs = ["../locales"]
gettext_compact = False
gettext_language_team = "Kazuya Takei <myself@attakei.net>"
gettext_last_translator = os.environ.get("SPHINXINTL_TRANSLATOR", None)

# -- Options for HTML output
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_title = project
html_permalinks = False
html_theme_options = {
    "article_footer_items": [],
    "icon_links": [
        {
            "name": "GitHub repo",
            "url": "https://github.com/atsphinx/atsphinx.github.io/",
            "icon": "fa-brands fa-github",
        }
    ],
    "secondary_sidebar_items": [],
}

# -- Options for extensions
# sphinx.ext.todo
todo_include_todos = True
