#!/bin/sh
# Scan for PDFs and make then searchable
find . -name *.pdf -print -exec ocrmypdf --deskew --rotate-pages {} {} \;