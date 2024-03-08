from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfWriter, PdfReader


def read_trailer(file):
    merged = "addTokenToTrailer.pdf"
    with open(file, "rb") as input_file:
        input_pdf = PdfReader(input_file)
        trailer = input_pdf.trailer
        trailer.update({"tokenize": "1231312312312"})
        print(trailer)
        input_pdf.trailer = trailer
        output = PdfWriter()

        for i in range(len(input_pdf.pages)):
            pdf_page = input_pdf.pages[i]
            output.add_page(pdf_page)

        with open(merged, "wb") as merged_file:
            output.write(merged_file)


read_trailer('./methods/test1.pdf')