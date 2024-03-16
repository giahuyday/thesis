from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument


def read_xref(pdf_path):
    with open(pdf_path, 'rb') as f:
        parser = PDFParser(f)
        document = PDFDocument(parser)

        # Lấy đối tượng xref từ tài liệu PDF
        xref = document.xrefs
    return xref


# Đường dẫn đến tệp PDF
pdf_path = 'test1.pdf'

# Đọc phần xref từ tệp PDF
xref_data = read_xref(pdf_path)

# In ra dữ liệu xref
print(xref_data)