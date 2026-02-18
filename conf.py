"""Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""

# pylint: disable=invalid-name,redefined-builtin

author = "Xander Harris <xandertheharris@gmail.com>"
autoyaml_root = "."
autoyaml_depth = 10

copyright = "2025, Xander Harris"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".venv/*",
    ".tmp/*",
    ".pytest_cache/*",
    ".venv/",
]

extensions = [
    "myst_parser",
    "sphinx_favicon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.duration",
    "sphinx.ext.extlinks",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    #"sphinxcontrib.autoyaml",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_logo = "_static/img/monitoring.png"
html_static_path = ["_static"]
html_theme = "sphinx_book_theme"
myst_dmath_double_inline = True
myst_enable_extensions = [
    "amsmath",
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_title_to_header = True
project = "Ansible Monitoring"
release = "0.0.1"
show_authors = True
source_suffix = {".md": "markdown"}
templates_path = ["_templates"]
