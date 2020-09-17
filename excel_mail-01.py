import xlrd
path = "C:\\Users\\rulo\\Desktop\\test.xlsx"

book = xlrd.open_workbook(path)
sheet = book.sheet_by_index(0)
mails = []
for r in range(1, sheet.nrows):
    mails.append(sheet.cell_value(r, 1))


print(sheet.nrows)
print(sheet.ncols)
print(mails)
