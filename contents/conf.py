# noqa: D100

import os

import dotenv
from atsphinx.mini18n import get_template_dir

dotenv.load_dotenv()

# -- Project information
project = "atsphinx"
copyright = "2023, Kazuya Takei"
author = "Kazuya Takei"
release = "2023.5.1"
version = release

# -- General configuration
extensions = [
    # Core bundled extensions
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    # atsphinx projects
    "atsphinx.bulma.layout.hero",  # TODO: Require to build doctree.
    "atsphinx.color_text",
    "atsphinx.footnotes",
    "atsphinx.mini18n",
    # Third-party extensions
    "sphinx_design",
]
templates_path = ["_templates", get_template_dir()]
exclude_patterns = []

# For i18n
language = "en"
locale_dirs = ["../locales"]
gettext_compact = False
gettext_language_team = "Kazuya Takei <myself@attakei.net>"
gettext_last_translator = os.environ.get("SPHINXINTL_TRANSLATOR", None)

# -- Options for HTML output
html_theme = "bulma-basic"
html_static_path = ["_static"]
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
    "css/custom.css",
]
html_title = project
html_permalinks = False
html_theme_options = {
    "bulmaswatch": "flatly",
    "navbar_icons": [
        {
            # "label": "GitHub repo",
            "url": "https://github.com/atsphinx/atsphinx.github.io/",
            "icon": "fa-brands fa-solid fa-github fa-2x",
        }
    ],
    "navbar_links": [
        {
            "title": "OpenCollective",
            "url": "https://opencollective.com/atsphinx",
        }
    ],
    "navbar_show_hidden_toctree": True,
    "show_theme_credit": True,
    "layout": {
        "index": [
            {"type": "space", "size": 2},
            {"type": "main", "size": 8},
            {"type": "space", "size": 2},
        ],
        "**": [
            {"type": "main", "size": 10},
            {"type": "sidebar", "size": 2},
        ],
    },
}

# -- Options for extensions
# sphinx.ext.todo
todo_include_todos = True

# atsphinx.mini18n
mini18n_default_language = "en"
mini18n_support_languages = ["en", "ja"]
mini18n_select_lang_label = ""
