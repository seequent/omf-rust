# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import omf_python

project = "OMF Rust Python API"
copyright = "2024, Seequent"
author = "Catalyst IT"

release = omf_python.version()
version = release

extensions = [
    "sphinx.ext.napoleon",
    "autoapi.extension",
]

autoapi_dirs = ["../../"]
autoapi_file_patterns = ["omf_python.pyi"]

html_theme = "sphinx_rtd_theme"

templates_path = ["_templates"]
exclude_patterns = []

html_static_path = []
