# Running the program
import calculator
import os
import pandas as pd


raw_excel = 'ftdt.xlsx' #input file with raw data

# Read pilot's data from the input file and convert to dataframe
instructor_data = pd.read_excel(raw_excel, 'Pilot1', parse_dates=['Date'])

# Calculate and set/format the required columns, fields, text etc
calculator.calculator(instructor_data)

# Open the output file automatically
os.system('start test.xlsx')
