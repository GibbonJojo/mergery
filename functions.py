from PyPDF2 import PdfFileMerger
import os
from contextlib import ExitStack

PATH = "./files/"

def merge_pdfs(pdfs, title):
    merger = PdfFileMerger()

    with ExitStack() as stack:
        files = [stack.enter_context(open(PATH + pdf.filename, 'rb')) for pdf in pdfs]
        for f in files:
            merger.append(f)
        with open(PATH + title + ".pdf", 'wb') as f:
            merger.write(f)



def clear_files(files):
    for file in files:
        os.remove(PATH + file.filename)