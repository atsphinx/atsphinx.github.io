# noqa: D100
# -- Project information
project = "atsphinx"
copyright = "2023, Kazuya Takei"
author = "Kazuya Takei"
release = "2023.5.1"

# -- General configuration
extensions = []
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
    "sphinx_design",
]
templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_title = project
html_permalinks = False
html_theme_options = {
    "article_footer_items": [],
    "secondary_sidebar_items": [],
}

# -- Options for extensions
# sphinx.ext.todo
todo_include_todos = True
