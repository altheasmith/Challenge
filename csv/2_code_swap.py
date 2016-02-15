# Challenge:

# Code swap - There is a supplementary CSV file for download here:
# state_abbreviations.csv. This "data dictionary" contains state abbreviations
# alongside state names. For the state field of the input CSV, replace each
# state abbreviation with its associated state name from the data dictionary.

import csv

def code_swap(csv_file):
    print "Reading CSV..."
    # Opens csv file and creates csv DictReader for test.csv file
    with open(csv_file, 'rb') as initial_file:
        csv_reader = csv.DictReader(initial_file)
        # Sets fieldnames variable for DictWriter to use
        fieldnames = csv_reader.fieldnames
        # Opens state csv file and creates csv DictReader for
        # state_abbreviations.csv file
        with open('state_abbreviations.csv', 'rb') as state_file:
            state_reader = csv.DictReader(state_file)
            # Creates dictionary with state abbr as key and state name as value
            state_dict = {row['state_abbr']: row['state_name'] for row in state_reader}
            # Creates solution csv file & csv DictWriter
            with open('solution.csv', 'wb') as solution_file:
                csv_writer = csv.DictWriter(solution_file, fieldnames=fieldnames)
                # Writes column headings
                csv_writer.writeheader()
                print "Replacing State Abbreviation with State Name..."
                for row in csv_reader:
                    # Switches state abbreviation with state name in the
                    # spreadsheet using the dictionary created from the state
                    # abbreviations file
                    row['state'] = state_dict[row['state']]
                    # Writes solution csv with state name instead of state
                    # abbreviation
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
