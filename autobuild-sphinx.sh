#!/bin/sh

# Trying to avoid invalidating Sphinx's cache between commits and on errors

PYTHON=python3

PROJECT=splines

$PYTHON -m sphinx_autobuild sphinx-$PROJECT/$PROJECT/doc _${PROJECT}_build \
    -c sphinx-$PROJECT \
    -b latex \
    -Drelease=dummy \
    -Dversion=dummy \
    -Dtoday=dummy \
    -Dhtml_title=dummy \
    -Dnbsphinx_allow_errors=1 \
    --port 0 \
    $@
