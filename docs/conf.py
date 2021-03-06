# -*- coding: utf-8 -*-

# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import re
import sys
from datetime import datetime


# Custom ReST roles. (Thanks for Fabric for these awesome ideas)
from docutils.parsers.rst import roles
from docutils import nodes, utils
issue_types = ('bug', 'feature', 'support')


def issues_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Use: :issue|bug|feature|support:`ticket number`

    When invoked as :issue:, turns into just a "#NN" hyperlink to Github.

    When invoked otherwise, turns into "[Type] <#NN hyperlink>: ".
    """
    # Old-style 'just the issue link' behavior
    issue_no = utils.unescape(text)
    ref = "https://github.com/trigger/trigger/issues/" + issue_no
    link = nodes.reference(rawtext, '#' + issue_no, refuri=ref, **options)
    ret = [link]
    # Additional 'new-style changelog' stuff
    if name in issue_types:
        which = '[<span class="changelog-%s">%s</span>]' % (
            name, name.capitalize()
        )
        ret = [
            nodes.raw(text=which, format='html'),
            nodes.inline(text=" "),
            link,
            nodes.inline(text=":")
        ]
    return ret, []

for x in issue_types + ('issue',):
    roles.register_local_role(x, issues_role)

# Also ripped from Fabric, but we need to nail down the versioning and release process for Trigger before we start to use this.
'''
year_arg_re = re.compile(r'^(.+?)\s*(?<!\x00)<(.*?)>$', re.DOTALL)
def release_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Invoked as :release:`N.N.N <YYYY-MM-DD>`.

    Turns into: <b>YYYY-MM-DD</b>: released <b><a>Trigger N.N.N</a></b>, with
    the link going to the Github source page for the tag.
    """
    # Make sure year has been specified
    match = year_arg_re.match(text)
    if not match:
        msg = inliner.reporter.error("Must specify release date!")
        return [inliner.problematic(rawtext, rawtext, msg)], [msg]
    number, date = match.group(1), match.group(2)
    return [
        nodes.strong(text=date),
        nodes.inline(text=": released "),
        nodes.reference(
            text="Fabric %s" % number,
            refuri="https://github.com/fabric/fabric/tree/%s" % number,
            classes=['changelog-release']
        )
    ], []
roles.register_local_role('release', release_role)
'''

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))
this = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(this, "_ext"))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
#extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage']
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'triggerdocs']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Trigger'
copyright = u'2006-%s, AOL Inc' % datetime.now().year

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..')))
#from trigger import __version__ as trigger_version
from trigger import full_version, short_version

# The short X.Y version.
version = short_version
# The full version, including alpha/beta/rc tags.
release = full_version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None
default_role = 'obj'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'default'
html_style = 'rtd.css'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'Triggerdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'Trigger.tex', u'Trigger Documentation',
   u'Jathan McCollum, Eileen Tschetter, Mark Ellzey Thomas, Michael Shields', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True
