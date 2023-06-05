import names
import xlsxwriter

if __name__ == '__main__':
    workbook = xlsxwriter.Workbook('data.xlsx')
    worksheet = workbook.add_worksheet()
    for i in range(1000000):
        name = names.get_full_name()
        worksheet.write(i, 0, name)

    workbook.close()

