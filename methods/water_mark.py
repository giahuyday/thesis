from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfWriter, PdfReader


def makeWatermark(water_mark_infor):
    pdf = canvas.Canvas("watermark.pdf", pagesize=A4)
    pdf.translate(inch, inch)
    pdf.setFillColor(colors.black, alpha=0.01)
    pdf.setFont("Helvetica", 50)
    pdf.rotate(45)
    pdf.drawCentredString(400, 100, water_mark_infor)
    pdf.save()


def makepdf(file):
    watermark = '../watermark.pdf'
    merged = "../Watermarked.pdf"

    with open(file, "rb") as input_file, open(watermark, "rb") as watermark_file:
        input_pdf = PdfReader(input_file)
        watermark_pdf = PdfReader(watermark_file)
        watermark_page = watermark_pdf.pages[0]
        output = PdfWriter()

        for i in range(len(input_pdf.pages)):
            pdf_page = input_pdf.pages[i]
            pdf_page.merge_page(watermark_page)
            output.add_page(pdf_page)

        with open(merged, "wb") as merged_file:
            output.write(merged_file)

