#!/usr/bin/env python

'''
usage:   metadata.py <first.pdf> [<next.pdf> ...]

Creates metadata.<first.pdf>

This file demonstrates two features:

1) Concatenating multiple input PDFs.

2) adding metadata to the PDF.

If you do not need to add metadata, look at subset.py, which
has a simpler interface to PdfWriter.

'''

import sys
import os

from pdfrw import PdfReader, PdfWriter, IndirectPdfDict

inputs = sys.argv[1:]
assert inputs
outfn = 'metadata.' + os.path.basename(inputs[0])

writer = PdfWriter()
for inpfn in inputs:
    writer.addpages(PdfReader(inpfn).pages)

writer.trailer.Info = IndirectPdfDict(
    Title='your title goes here',
    Author='your name goes here',
    Subject='what is it all about?',
    Creator='some script goes here',
)
writer.write(outfn)
