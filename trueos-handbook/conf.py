# -*- coding: utf-8 -*-

# requirements:
# textproc/py-sphinx
# textproc/py-sphinx_numfig
# textproc/py-sphinx_rtd_theme
# textproc/py-sphinxcontrib-httpdomain

import os
import six
import string
import sys
import time

templates_path = ['_templates']

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

sys.path.append(os.path.abspath('/usr/local/lib/python2.7/site-packages/sphinx/ext/'))

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.ifconfig',
    'sphinxcontrib.httpdomain',
    'wikipedia',
]
# -- Options for automatic Figure numbering
numfig = True
numfig_secnum_depth = (2)

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'trueos'

# General information about the project.
project = u'TrueOS® User Guide'
copyright = u'2011-2017, iXsystems'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
#version = '11.0'
# The full version, including alpha/beta/rc tags.
#release = '11.0'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

#Option to add text substitutions to all .rst files being built.
rst_prolog = """
.. |freenas| replace:: FreeNAS\ :sup:`"""u'\u00AE'"""`
.. |truenas| replace:: TrueNAS\ :sup:`"""u'\u00AE'"""`
.. |pcbsd| replace:: PC-BSD\ :sup:`"""u'\u00AE'"""`
.. |trueos| replace:: TrueOS\ :sup:`"""u'\u00AE'"""`
.. |appcafe| replace:: AppCafe\ :sup:`"""u'\u00AE'"""`
.. |lumina| replace:: Lumina\ :sup:`"""u'\u00AE'"""`
.. |sysadm| replace:: SysAdm\ :sup:`"""u'\u2122'"""`
.. |trpi| replace:: TrueOS Pico\ :sup:`"""u'\u2122'"""`
.. |pise| replace:: Pico Server\ :sup:`"""u'\u2122'"""`
.. |picl| replace:: Pico Client\ :sup:`"""u'\u2122'"""`
"""

# -- Option to change :menuselection: arrow -----------------------------

from docutils import nodes, utils
from docutils.parsers.rst import roles
from sphinx.roles import _amp_re

def patched_menusel_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
    text = utils.unescape(text)
    if typ == 'menuselection':
        text = text.replace('-->', u'\u2192') # Here is the patch

    spans = _amp_re.split(text)  

    node = nodes.literal(rawtext=rawtext)
    for i, span in enumerate(spans):
        span = span.replace('&&', '&')
        if i == 0:
            if len(span) > 0:
                textnode = nodes.Text(span)
                node += textnode
            continue
        accel_node = nodes.inline()
        letter_node = nodes.Text(span[0])
        accel_node += letter_node
        accel_node['classes'].append('accelerator')
        node += accel_node
        textnode = nodes.Text(span[1:])
        node += textnode

    node['classes'].append(typ)
    return [node], []

# Use 'patched_menusel_role' function for processing the 'menuselection' role
roles.register_local_role("menuselection", patched_menusel_role)

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'trueos_style'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project + " "

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "trueoslogo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "trueos.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = ['trueos-handbook/themes/trueos_style/searchresults.html']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {'searchresults' : 'searchresults.html',}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'TrueOSdoc'

# -- Options for LaTeX output ---------------------------------------------

if six.PY3:
    texproject = project.replace('®', r'''\textsuperscript{\textregistered}''')
else:
    texproject = project.replace(u'®', r'''\textsuperscript{\textregistered}''')

PREAMBLE = r'''\def\docname{''' + texproject + '}'

PREAMBLE = (PREAMBLE
            + r'''\def\docdate{'''
            + time.strftime("%B %Y")
            + ' Edition}')

# define custom title page
PREAMBLE = PREAMBLE + r'''
% FreeNAS/TrueNAS LaTeX preamble
\usepackage[default,scale=0.95]{opensans}
\usepackage[T1]{fontenc}
\usepackage{color}
\usepackage{tikz}
\usetikzlibrary{calc}
%for ragged right tables
\usepackage{array,ragged2e}
\definecolor{ixblue}{cmyk}{0.85,0.24,0,0}
\newenvironment{widemargins}{%
\begin{list}{}{%
  \setlength{\leftmargin}{-0.5in}%
  \setlength{\rightmargin}{-0.5in}%
  }\item}%
  {\end{list}%
}
\makeatletter
\renewcommand{\maketitle}{%
  \begin{titlepage}%
    \newlength{\thistitlewidth}%
    \begin{widemargins}%
      \usefont{T1}{fos}{l}{n}%
      \vspace*{-6mm}%
      \fontsize{32}{36}\selectfont%
      \docname\par%
      \vspace*{-4.5mm}%
      \settowidth{\thistitlewidth}{\docname}%
      {\color{ixblue}\rule{\thistitlewidth}{1.5pt}}\par%
      \vspace*{4.5mm}%
      \fontsize{18}{22}\fontseries{sbc}\selectfont%
      \docdate\par%
    \end{widemargins}%
    \begin{tikzpicture}[remember picture,overlay]
      \fill [ixblue] (current page.south west) rectangle ($(current page.south east) + (0, 2in)$);
    \end{tikzpicture}
  \end{titlepage}
}
\makeatother
% a plain page style for front matter
\fancypagestyle{frontmatter}{%
  \fancyhf{}
  \fancyhf[FCO,FCE]{}
  \fancyhf[FLE,FRO]{\textbf{\thepage}}
  \fancyhf[FLO,FRE]{}
}
'''

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
'preamble': PREAMBLE,

# remove blank pages
'classoptions': ',openany',
'babel': r'''\usepackage[english]{babel}''',

# strict positioning of figures
'figure_align': 'H'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
#  Auto-generated version differs a bit:
# latex_documents = [
#   ('pcbsd', 'PC-BSDUserGuide.tex', u'PC-BSD User Guide 10.1.2',
#    u'iXsystems', 'manual'),
# ]
latex_documents = [
('trueos', u'trueos.tex', u'TrueOS® User Guide',
   u'iXsystems', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
#latex_show_urls = 'inline'

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# -- Options for translations
locale_dirs = ['_build/locale-po/']

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'TrueOS® User Guide'
epub_author = u'iXsystems'
epub_publisher = u'iXsystems'
epub_copyright = u'2011-2016, iXsystems'

# The basename for the epub file. It defaults to the project name.
epub_basename = u'trueos_userguide'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
epub_scheme = 'URL'

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
epub_identifier = 'trueos.org'

# A unique identification for the text.
#epub_uid = '11'

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html', 'searchresults.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
epub_show_urls = 'no'

# If false, no index is generated.
#epub_use_index = True

# -- Epilogue additions ----------------------------------------------------------
# .. |keyword| replace:: text to replace it with
# .. |copy| unicode:: U+000A9 .. COPYRIGHT SIGN
rst_epilog = """
.. |cop| unicode:: U+000A9 
.. |reg| unicode:: U+000AE
.. |TrueOS| replace:: TrueOS\ |reg|
"""
