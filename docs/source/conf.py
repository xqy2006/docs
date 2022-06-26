# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'xuqinyang-doc'
copyright = '2022, xuqinyang'
author = 'xuqinyang'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',
    'sphinx_markdown_tables'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#Add project information to the template context.
context = {
    'using_theme': "sphinx_rtd_theme",
    'html_theme': html_theme,
    'current_version': "latest",
    'version_slug': "latest",
    'MEDIA_URL': "https://media.readthedocs.org/",
    'STATIC_URL': "https://assets.readthedocs.org/static/",
    'PRODUCTION_DOMAIN': "readthedocs.org",
    'proxied_static_path': "/_/static/",
    'versions': [
    ("latest", "/zh_CN/latest/"),
    ],
    'downloads': [ 
    ("pdf", "//xqy2006.github.io/docs/xuqinyang-doc.pdf"),
    ("html", "//xqy2006.github.io/docs/xuqinyang-doc.zip"),
    ("epub", "//xqy2006.github.io/docs/xuqinyang-doc.epub"),
    ],
    'subprojects': [ 
    ],
    'slug': 'xuqinyang-doc',
    'name': u'xuqinyang-doc',
    'rtd_language': u'zh_CN',
    'programming_language': u'words',
    'canonical_url': 'https://xqy2006.github.io/docs/',
    'analytics_code': 'None',
    'single_version': False,
    'conf_py_path': '/docs/source/',
    'api_host': 'https://readthedocs.org',
    'github_user': 'xqy2006',
    'proxied_api_host': '/_',
    'github_repo': 'doc',
    'github_version': 'main',
    'display_github': True,
    'bitbucket_user': 'None',
    'bitbucket_repo': 'None',
    'bitbucket_version': 'main',
    'display_bitbucket': False,
    'gitlab_user': 'None',
    'gitlab_repo': 'None',
    'gitlab_version': 'main',
    'display_gitlab': True,
    'READTHEDOCS': False,
    'using_theme': (html_theme == "default"),
    'new_theme': (html_theme == "sphinx_rtd_theme"),
    'docsearch_disabled': False,
    'user_analytics_code': '',
    'global_analytics_code': 'UA-17997319-1',
    'commit': 'fb252565',
}

if 'html_context' in globals():
    
    html_context.update(context)
    
else:
    html_context = context
readthedocs_build_url = 'https://github.com/xqy2006/docs'
