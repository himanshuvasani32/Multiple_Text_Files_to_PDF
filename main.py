from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("Text_Files/*.txt")

# Created PDF for all text filesF
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()

    # Get the title name without extension and capitalized it
    page_title = Path(filepath).stem.capitalize()

    # Added the title to PDF for each text file
    pdf.set_font(family="Times", size=20, style="B")
    pdf.cell(w=50, h=12, txt=page_title, ln=1, align="L")

    # Get the content of each text file and write in PDF
    with open(filepath, "r") as file:
        content = file.read()
        pdf.set_font(family="Times", size=12)
        pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("data.pdf")


