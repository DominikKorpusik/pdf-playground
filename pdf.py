import PyPDF2
import sys

pdfs = sys.argv[1:]

def pdf_combiner(pdf_lists):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_lists:
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(pdfs)


