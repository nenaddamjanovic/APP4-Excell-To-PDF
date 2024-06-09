import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# reads data filepath(folder)
filepaths = glob.glob("invoices/*.xlsx")


for filepath in filepaths:
    # adds pdf page
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    # extracts filename from filepath
    # 10001-2023.1.18.xlsx -> 10001-2023.1.18
    filename = Path(filepath).stem

    # splits string on " - ", creates list, pick first item
    # 10001-2023.1.18 -> [10001, 2023.1.18]
    # invoice_number = filename.split("-")[0]
    # 10001
    # date = filename.split("-")[1]
    # 2023.1.18
    invoice_number, date = filename.split("-")

    # creates title
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice number: {invoice_number}", ln=1)
    # creates date
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    # reads each data filepath in folder
    datafile = pd.read_excel(filepath, sheet_name="Sheet 1")

    # reads and create headers in table
    columns = datafile.columns
    # menja _ u space u nazivu svih kolona
    columns = [i.replace("_", " ").title() for i in columns]
    # print(columns)
    pdf.set_font(family="times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=60, h=8, txt=columns[1], border=1)
    pdf.cell(w=35, h=8, txt=columns[2], border=1)
    pdf.cell(w=35, h=8, txt=columns[3], border=1)
    pdf.cell(w=35, h=8, txt=columns[4], border=1, ln=1)

    # reads and creates rows in table
    for index, row in datafile.iterrows():
        # creates all data in table
        pdf.set_font(family="times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=35, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=35, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=35, h=8, txt=str(row["total_price"]), border=1, ln=1)

    pdf.output(f"pdfs/{filename}.pdf")

