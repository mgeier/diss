#!/usr/bin/env python3
from pathlib import Path

from sphinx import highlighting

EXTENSIONS = {
    'asd': 'xml',
    'osc': 'none',
    'txt': 'none',
    'wrl': 'none',
}


def pygmentize(source, destination):
    lang = source.suffix[1:]
    lang = EXTENSIONS.get(lang, lang)
    code = source.read_text()
    highlighter = highlighting.PygmentsBridge(
        'latex', latex_engine='lualatex')
    hlcode = highlighter.highlight_block(code, lang)
    hlcode = hlcode.replace(r'\begin{Verbatim}', r'\begin{sphinxVerbatim}')
    hlcode = hlcode.replace(r'\end{Verbatim}', r'\end{sphinxVerbatim}')
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(hlcode)


if __name__ == '__main__':
    srcdir = Path('raw-code')
    destdir = Path('highlighted-code')
    for filename in srcdir.iterdir():
        if filename.name.startswith('.'):
            continue
        pygmentize(filename, destdir / (filename.name + '.tex'))
