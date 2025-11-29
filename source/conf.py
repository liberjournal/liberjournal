# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Liber Journal'
copyright = '2025, Liber Journal. Text is available under the CC BY-SA 4.0'
author = 'Liber Journal'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_copybutton',]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_title = 'Liber Journal'
html_favicon = '_static/favicon.svg'

html_css_files = [
    'theme-overrides.css',
]

html_theme_options = {
  "footer_start": ["copyright"],
  "footer_center": ["sphinx-version"],
  "footer_end": ["theme-version"],
}