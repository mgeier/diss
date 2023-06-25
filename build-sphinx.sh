#!/bin/sh

set -e

cd "$(dirname "$0")"

SPHINX="python3 -m sphinx"

for x in splines asdf
do
    $SPHINX sphinx-$x/$x/doc _${x}_build -c sphinx-$x -b latex $@
done
