from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfWriter, PdfReader
import img2pdf
from PIL import Image
import os

def water_mark_use_img(img, file_path):
    # storing image path
    img_path = img
    # storing pdf path
    pdf_path = file_path
    # opening image
    image = Image.open(img_path)
    # converting into chunks using img2pdf
    pdf_bytes = img2pdf.convert(image.filename)
    # opening or creating pdf file
    file = open(pdf_path, "wb")
    # writing pdf files with chunks
    file.write(pdf_bytes)
    # closing image file
    image.close()
    # closing pdf file
    file.close()
    # output
    print("Successfully made pdf file")

def makeWatermark(water_mark_infor):
    pdf = canvas.Canvas("watermark.pdf", pagesize=A4)
    pdf.translate(inch, inch)
    pdf.setFillColor(colors.black, alpha=0.5)
    pdf.setFont("Helvetica", 50)
    pdf.rotate(45)
    pdf.drawCentredString(400, 100, water_mark_infor)
    pdf.save()


def makepdf(file, token):
    watermark_bg = 'new.pdf'
    watermark_text = 'watermark.pdf'
    merged = "Watermarked.pdf"

    with open(file, "rb") as input_file, open(watermark_bg, "rb") as watermark_file, open(watermark_text, 'rb') as watermark_content:
        input_pdf = PdfReader(input_file)
        watermark_bg = PdfReader(watermark_file)
        watermark_page_bg = watermark_bg.pages[0]

        watermark_text = PdfReader(watermark_content)
        watermark_page_text = watermark_text.pages[0]

        output = PdfWriter()

        for i in range(len(input_pdf.pages)):
            pdf_page = input_pdf.pages[i]
            pdf_page.merge_page(watermark_page_bg)
            pdf_page.merge_page(watermark_page_text)
            output.add_page(pdf_page)

        # Encrypt the new file with the entered password
        output.encrypt(token)

        with open(merged, "wb") as merged_file:
            output.write(merged_file)
