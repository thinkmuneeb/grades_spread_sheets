import openpyxl as xl
from openpyxl.chart import BarChart, Reference

def grade_absolute(score):
    s = score
    if s > 80:
        return 'A'
    elif s > 70:
        return 'B'
    elif s > 60:
        return 'C'
    elif s >= 50:
        return 'D'
    elif s < 50:
        return 'F'

def grade_relative(score):
    return 'realative'
        
def process_workbook_absolute_grade(filename):
    wb = xl.load_workbook(filename)
    sheet = wb['Sheet1']

    for row in range(5, sheet.max_row+1):
        cell = sheet.cell(row, 3)
        grade = grade_absolute(score = cell.value)
        grade_cell = sheet.cell(row,4)
        grade_cell.value = grade
    
    values = Reference(sheet,
                min_row=5,
                max_row= sheet.max_row, 
                min_col=3,
                max_col=3)
    chart = BarChart()
    chart.add_data(values)
    sheet.add_chart(chart, 'j4')

    wb.save(filename)
        

def process_workbook_relative_grade(filename):
    wb = xl.load_workbook(filename)
    sheet = wb['Sheet1']

    for row in range(5, sheet.max_row+1):
        cell = sheet.cell(row, 3)
        grade = grade_relative(score = cell.value)
        grade_cell = sheet.cell(row,4)
        grade_cell.value = grade
    
    #which values will be used to make graph
    values = Reference(sheet,
                min_row=5,
                max_row= sheet.max_row, 
                min_col=3,
                max_col=3)
    chart = BarChart()
    chart.add_data(values)
    sheet.add_chart(chart, 'j4')

    wb.save(filename)
        

process_workbook_absolute_grade('marks_to_grades.xlsx')
print('--------done')