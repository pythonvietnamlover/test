import openpyxl

wb = openpyxl.load_workbook('O:\\test\\data_openpyxl.xlsx')
connect_sheet = wb.get_sheet_by_name('small')
for i in range(1, 100000,1):
    for j in range(1, 20, 1):
        connect_sheet.cell(row=i, column=j).value = str(i) + " " + str(j)

wb.save('O:\\test\\data_openpyxl_changed.xlsx')