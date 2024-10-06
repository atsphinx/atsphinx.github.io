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
extensions = []
extensions = [
    "atsphinx.color_text",
    "atsphinx.footnotes",
    "atsphinx.mini18n",
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
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
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_title = project
html_permalinks = False
html_theme_options = {
    "navbar_start": [
        "navbar-logo",
        "mini18n/snippets/select-lang",
    ],
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

# atsphinx.mini18n
mini18n_default_language = "en"
mini18n_support_languages = ["en", "ja"]
mini18n_select_lang_label = ""
