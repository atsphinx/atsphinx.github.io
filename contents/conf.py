# -- Project information
project = "atsphinx"
copyright = "2023, Kazuya Takei"
author = "Kazuya Takei"
release = "2023.5.1"

# -- General configuration
extensions = []
extensions = [
    "sphinx.ext.todo",
]
templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output
html_theme = "alabaster"
html_static_path = ["_static"]
html_title = project

# -- Options for extensions
# sphinx.ext.todo
todo_include_todos = True
