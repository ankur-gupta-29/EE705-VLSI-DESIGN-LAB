# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#import sphinxcontrib.youtube
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'EE705 VLSI DESIGN LAB'
copyright = '2024, Ankur Gupta'
author = 'Ankur Gupta'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme',
              "myst_parser",
              "sphinx_design",
              ]

templates_path = ['_templates']
exclude_patterns = []
source_suffix = ['.rst', '.md']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = "sphinx_rtd_theme"
html_theme = "furo"
html_static_path = ['_static']

# Enable numref
numfig = True
