# Challenge:

# Code swap - There is a supplementary CSV file for download here:
# state_abbreviations.csv. This "data dictionary" contains state abbreviations
# alongside state names. For the state field of the input CSV, replace each
# state abbreviation with its associated state name from the data dictionary.

import csv
import pandas as pd

def code_swap(csv_file):
    print "Reading CSV..."
    # Opens csv file and creating csv DictReader for test.csv file
    with open(csv_file, 'rb') as initial_file:
        csv_reader = csv.DictReader(initial_file)
        # Creates lists out of state name & abbreviation columns with pandas to
        # avoid opening/reading state file twice with csv module
        state_csv = pd.read_csv('state_abbreviations.csv')
        state_abbrs = state_csv.state_abbr.tolist()
        state_names = state_csv.state_name.tolist()
        # Sets fieldnames variable for DictWriter to use
        fieldnames = csv_reader.fieldnames
        # Creates solution csv file & csv DictWriter
        with open('solution.csv', 'wb') as solution_file:
            csv_writer = csv.DictWriter(solution_file, fieldnames=fieldnames)
            # Writes column headings
            csv_writer.writeheader()
            print "Replacing State Abbreviation with State Name..."
            for row in csv_reader:
                # Switches state abbreviation with state name in the spreadsheet using
                # the index of the state abbreviations in the lists created with pandas
                row['state'] = state_names[state_abbrs.index(row['state'])]
                # Writes solution csv with state name instead of state abbreviation
                csv_writer.writerow(row)
            print "Replacement Complete"
            # Nothing to return - output is in csv file


# To run from command line:
'''
python 2_code_swap.py
'''

#------FOR RUNNING FROM COMMAND LINE------#
code_swap('test.csv')
#-----------------------------------------#

# To run from python shell, comment out the above line, and enter the lines
# below into the python shell:
'''
from csv import code_swap
code_swap()
'''
