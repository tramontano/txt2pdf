#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename          : TXT2PDF.py
# author            : tramontano
# email             : tramontanophillipe@gmail.com
# date              : 2022-12-28
# version           : 1.0
# usage             : python TXT2PDF.py
# notes             : Version 1.0
# license           : MIT
# py version        : 3.7.0
#==============================================================================

from fpdf import FPDF
import glob
list = glob.glob('*.txt')
for log in list:
    name = log.replace('.txt', '')
    file = name + ".txt"
    print('Converting TXT', file, 'to PDF')
    output_pdf = name + '.pdf'
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 6)
    cmd = open(file, "r")
    for lines in cmd:
        pdf.cell(0, 3, lines, 0, 1)
    pdf.output(output_pdf)
    print(output_pdf, "created successfully")
