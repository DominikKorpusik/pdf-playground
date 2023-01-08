import PyPDF2
import sys

pdfs = sys.argv[1:]

def pdf_combiner(pdf_lists):
    '''Combining all PDFs in one pdf'''
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_lists:
        merger.append(pdf)
    merger.write('super.pdf')


def pdf_UWatermark(pdf):
    templet = PyPDF2.PdfFileReader(open(f"{pdf[0]}", "rb"))
    watermark = PyPDF2.PdfFileReader(open("wtr.pdf", "rb"))
    output = PyPDF2.PdfFileWriter()

    for i in range(templet.getNumPages()):
        page = templet.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open("watermarked_doc.pdf", "wb") as pdf:
            output.write(pdf)

pdf_UWatermark(pdfs)