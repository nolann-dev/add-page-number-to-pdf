# add_page_numbers.py

import sys
import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

def add_page_numbers(input_pdf_path, output_pdf_path):
    # Read the original PDF
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    num_pages = len(reader.pages)

    for i in range(num_pages):
        # Create a PDF with the page number
        packet = BytesIO()
        # Use the same page size as the original
        page = reader.pages[i]
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        can = canvas.Canvas(packet, pagesize=(width, height))
        # Draw page number at the bottom center
        page_number_text = f"{i+1} / {num_pages}"
        font_size = 12
        can.setFont("Helvetica", font_size)
        text_width = can.stringWidth(page_number_text, "Helvetica", font_size)
        x = (width - text_width) / 2
        y = 20  # 20 points from the bottom
        can.drawString(x, y, page_number_text)
        can.save()
        packet.seek(0)

        # Merge the page number PDF with the original page
        from PyPDF2 import PdfReader as RLReader
        overlay_pdf = RLReader(packet)
        overlay_page = overlay_pdf.pages[0]
        page.merge_page(overlay_page)
        writer.add_page(page)

    # Write the output PDF
    with open(output_pdf_path, "wb") as out_f:
        writer.write(out_f)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add_page_numbers.py input.pdf output.pdf")
        sys.exit(1)
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    add_page_numbers(input_pdf, output_pdf)
    print(f"Page numbers added: {output_pdf}")
