# Challenge:

# Code swap - There is a supplementary CSV file for download here:
# state_abbreviations.csv. This "data dictionary" contains state abbreviations
# alongside state names. For the state field of the input CSV, replace each
# state abbreviation with its associated state name from the data dictionary.

import csv
import pandas as pd

def code_swap():
    print "Reading CSV..."
    # Opening csv file and creating csv DictReader for test.csv file
    initial_file = open('test.csv', 'rb')
    csv_reader = csv.DictReader(initial_file)
    # Using pandas to create lists out of state name & abbreviation columns
    # without opening/reading state file twice with csv module
    state_csv = pd.read_csv('state_abbreviations.csv')
    state_abbrs = state_csv.state_abbr.tolist()
    state_names = state_csv.state_name.tolist()
    # Setting fieldnames variable for DictWriter to use
    fieldnames = next(csv_reader).keys()
    # Creating solution csv file & csv DictWriter
    solution_file = open('solution.csv', 'wb')
    csv_writer = csv.DictWriter(solution_file, fieldnames=fieldnames)
    # Writing column headings
    csv_writer.writeheader()
    print "Replacing State Abbreviation with State Name..."
    for row in csv_reader:
        # Switching state abbreviation with state name in the spreadsheet using
        # the index of the state abbreviations in the lists created with pandas
        row['state'] = state_names[state_abbrs.index(row['state'])]
        # Writing solution csv with state name instead of state abbreviation
        csv_writer.writerow(row)
    print "Replacement Complete"
    return

code_swap()
