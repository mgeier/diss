import os
from pathlib import Path

import sphinx
import docutils

original_conf_py = Path(__file__).resolve().parent / 'splines/doc/conf.py'
locals().update(sphinx.config.eval_config_file(str(original_conf_py), tags))

templates_path = ['../_templates', '_templates']
# Exclude templates in the original source directory:
exclude_patterns.append('_templates/**')
html_favicon = None

latex_engine = 'lualatex'

latex_documents = [
    ('index', 'splines.tex', '', '', 'howto', True),
]

exclude_patterns.append('references.rst')
suppress_warnings = ['toc.excluded']

extensions.remove('sphinxcontrib.bibtex')


def _build_finished(app, exception):
    # The inventory file is normally only created in the HTML builder,
    # we also create it for LaTeX.
    from sphinx.util.inventory import InventoryFile
    if exception is not None:
        return
    for docname in ('genindex', 'modindex', 'py-modindex', 'search'):
        del app.env.domains['std'].labels[docname]
        del app.env.domains['std'].anonlabels[docname]
    InventoryFile.dump(
        os.path.join(app.builder.outdir, 'objects.inv'), app.env, app.builder)


# This avoids a myriad of footnotes for "object":
def _autodoc_process_bases(app, name, obj, options, bases):
    if bases == [object]:
        #del bases[0]  # This still shows the unnecessary text "Bases:"
        bases[0] = '``object``'


def cite_role(macroname):

    def role(name, rawtext, text, lineno, inliner, options=None, content=None):
        latex_code = rf'\{macroname}{{{text}}}'
        return [docutils.nodes.raw('', latex_code, format='latex')], []

    return role


def setup(app):
    app.connect('build-finished', _build_finished)
    app.connect('autodoc-process-bases', _autodoc_process_bases)
    app.add_role('cite', cite_role('parencite'))
    app.add_role('cite:t', cite_role('textcite'))
