# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'VexV5'
copyright = '2025, Daniel T-B'
author = 'Daniel T-B'
release = '2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'breathe',
    'myst_parser',    # Enable Markdown support
    #'ablog',          # Enable blog post feature
    'sphinx_tabs.tabs', # Enable code tabs
    #'sphinx.ext.intersphinx'
]

templates_path = ['_templates']
exclude_patterns = []

breathe_projects = {
    "LemLibAPI": "./lemlib/api/doxygen/xml",  # LemLib Doxygen XML output folder
    "RobodashAPI": "./robodash/api/doxygen/xml",  # Robodash Doxygen XML output folder
}

breathe_default_project = "LemLibAPI"  # Set the default project (you can switch this as needed)


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']