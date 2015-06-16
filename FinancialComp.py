import random
import pymongo
import sys
import pandas as pd
from pprint import pprint
import csv
import xlrd

c = pymongo.Connection("localhost")
collection = c.mydb.collection

db = c['Financial Computation DataBase']

def getSheets(filename):
    pointSheetObj = []
    import xlrd as xl
    TeamPointWorkbook = xl.open_workbook(filename)
    pointSheets = TeamPointWorkbook.sheet_names()
    for i in pointSheets:
        pointSheetObj.append(tuple((TeamPointWorkbook.sheet_by_name(i),i)))
    return pointSheetObj
    
def initCollections(filename):
    sheets = getSheets(filename)       

def extendedDataBase(filename, sheets):
    workbook = xlrd.open_workbook(filename)
    curr_row = -1
    
    while curr_row: # Reads in the excel sheets 
        try:
            curr_row += 1
            worksheet = workbook.sheet_by_name(sheets[curr_row]) 
            worksheetName = sheets[curr_row]
            worksheetName = db[worksheetName]
            num_rows = worksheet.nrows - 1
            num_cells = worksheet.ncols - 1
            row = worksheet.row(curr_row)
            curr_cell = -1
            while curr_cell < num_cells:
                curr_cell += 1
                # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
                cell_type = worksheet.cell_type(curr_row, curr_cell)
                cell_value = worksheet.cell_value(curr_row, curr_cell)
                db.worksheetName.insert(cell_value)
                if curr_row < num_rows:
       	            break
        except (TypeError):
            pass

if __name__ == "__main__":
    filename = sys.argv[1]
    collectName = str(filename)
    # creates collection of database names
    collectName = db[collectName]
    sheets = getSheets(filename)
    db.collectName.insert(sheets)
    # creates collections of actual data
    extendedDataBase(filename, sheets)
