from tabula import read_pdf
from tabulate import tabulate


def defdun():
    pdf_file=read_pdf("",pages="all")
    d=tabulate(pdf_file)
    print(d)
    
defdun()
