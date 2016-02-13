# Challenge:

# String cleaning - The bio field contains text with arbitrary padding, spacing
# and line breaks. Normalize these values to a space-delimited string.

import csv

def string_cleaning():
    print "Reading CSV..."
    # Opens csv file and creating csv DictReader:
    initial_file = open('test.csv', 'rb')
    csv_reader = csv.DictReader(initial_file)
    # Sets fieldnames variable for DictWriter to use
    fieldnames = csv_reader.fieldnames
    # Creates solution csv file & csv DictWriter
    solution_file = open('solution.csv', 'wb')
    csv_writer = csv.DictWriter(solution_file, fieldnames=fieldnames)
    # Writes column headings
    csv_writer.writeheader()
    print "Cleaning Bios..."
    for row in csv_reader:
        # Removes extra whitespace from "bio" field for each row
        row['bio'] = " ".join(row['bio'].split())
        # Writes new spreadsheet with fixed "bio" rows
        csv_writer.writerow(row)
    print "Cleaning Complete"
    # Nothing to return - output is in csv file


# To run from command line:
'''
python 1_string_cleaning.py
'''

#------FOR RUNNING FROM COMMAND LINE------#
string_cleaning()
#-----------------------------------------#

# To run from python shell, comment out the above line, and enter the lines
# below into the python shell:
'''
from csv import string_cleaning
string_cleaning()
'''
