import glob
from fpdf import FPDF
from pathlib import Path

# reads data filepath(folder)
filepaths = glob.glob("textfiles/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    with open(filepath, "r") as file:
        content = file.read()

    # extracts filename from filepath
    filename = Path(filepath).stem
    filename = filename.title()
    pdf.add_page()
    pdf.set_font(family="times",size=18, style="B")
    pdf.cell(w=50, h=20, txt=filename, ln=1)
    pdf.set_font(family="times",size=12, style="I")
    pdf.multi_cell(w=0, h=8, txt=content, border=1)

pdf.output("output.pdf")

