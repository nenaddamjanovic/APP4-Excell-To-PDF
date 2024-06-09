import pandas as pd
import glob

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    datafile = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(datafile)