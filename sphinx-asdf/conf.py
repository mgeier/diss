import os
from pathlib import Path

import docutils
import sphinx
from sphinx.util.inventory import InventoryFile


HERE = Path(__file__).resolve().parent
original_conf_py = HERE / 'asdf/doc/conf.py'
locals().update(sphinx.config.eval_config_file(str(original_conf_py), tags))

templates_path = ['../_templates']
html_favicon = None

latex_engine = 'lualatex'

latex_documents = [
    ('index', 'asdf.tex', '', '', 'howto', True),
]

# This should not be handled by intersphinx!
del intersphinx_mapping['splines']


def fetch_splines_inventory():
    # uri: base URI of the links to generate
    uri = ''  # Doesn't matter!
    inv = HERE / '../_splines_build/objects.inv'
    # TODO: catch exception if it doesn't exist?
    with open(inv, 'rb') as f:
        return InventoryFile.load(f, uri, os.path.join)


SPLINES_INV = fetch_splines_inventory();


def _missing_reference(app, env, node, contnode):
    reftarget = node['reftarget']
    if not reftarget.startswith('splines:'):
        return
    # Remove 'splines:'
    reftarget = reftarget[8:]
    key = {
        'doc': 'std:doc',
        'ref': 'std:label',
    }[node['reftype']]
    _, _, uri, title = SPLINES_INV[key][reftarget]

    if node['refexplicit']:
        title = node.astext()

    newnode = docutils.nodes.reference('', '', refuri=uri, internal=True)
    newnode += docutils.nodes.Text(title)
    return newnode


def setup(app):
    from docutils import nodes, parsers
    parsers.rst.roles.register_generic_role('scene-link', nodes.literal)
    app.connect('missing-reference', _missing_reference)
