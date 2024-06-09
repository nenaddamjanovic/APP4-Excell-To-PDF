import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# reads data filepath(folder)
filepaths = glob.glob("invoices/*.xlsx")


for filepath in filepaths:
    # reads each data filepath in folder
    datafile = pd.read_excel(filepath, sheet_name="Sheet 1")
    # adds pdf page
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # extracts filename from filepath
    # 10001-2023.1.18.xlsx -> 10001-2023.1.18
    filename = Path(filepath).stem
    # splits string on " - ", creates list, pick first item
    # 10001-2023.1.18 -> [10001, 2023.1.18]
    invoice_number = filename.split("-")[0]
    # 10001

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice number:{invoice_number}")
    pdf.output(f"pdfs/{filename}.pdf")

