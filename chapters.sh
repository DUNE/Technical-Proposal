#!/bin/bash

# This script is used by the Waf build as directed in the wscript file.
# Do not modify unless you know what you are doing.

usage () {
    echo "chapters.sh chapter-template.tex chapter-file.tex output-chapter-file.tex"
    exit 1
}

tmpl=$1 ; shift
tex=$1 ; shift
out=$1 ; shift

volume=$(basename $(dirname $tex))
chapter=$(basename $tex .tex)

cat $tmpl | sed -e "s/volume/$volume/g" -e "s/chapter/$chapter/g" > "${out}"

