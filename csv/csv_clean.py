# Challenge

# TODO Write a script to transform input CSV to desired output CSV.
#
# You will find a CSV file available for download here: test.csv. There are two
# steps (plus an optional bonus) to this part of the test. Each step concerns
# manipulating the values for a single field according to the step's requirements.
# The steps are as follows:
#
# 1. String cleaning - The bio field contains text with arbitrary padding,
# spacing and line breaks. Normalize these values to a space-delimited string.
# 2. Code swap - There is a supplementary CSV file for download here:
# state_abbreviations.csv. This "data dictionary" contains state abbreviations
# alongside state names. For the state field of the input CSV, replace each
# state abbreviation with its associated state name from the data dictionary.
# 3. Date offset (bonus) - The start_date field contains data in a variety of
# formats. These may include e.g., "June 23, 1912" or "5/11/1930" (month, day,
# year). But not all values are valid dates. Invalid dates may include e.g.,
# "June 2018", "3/06" (incomplete dates) or even arbitrary natural language.
# Add a start_date_description field adjacent to the start_date column to filter
# invalid date values into. Normalize all valid date values in start_date to ISO
# 8601 (i.e., YYYY-MM-DD).
# Your script should take "test.csv" as input and produce a cleansed
# "solution.csv" file according to the step requirements above. Please attach
# your "solution.csv" file along with your solution code in your reply!

#=============================================================================#

#-----------------------------------------------------------------------------#
# Imports
#-----------------------------------------------------------------------------#
import csv
from datetime import datetime
import dateutil.parser as parser
import pandas as pd

def csv_clean():
    print "Reading CSV..."
    # Opening csv file and creating csv DictReader:
    initial_file = open('test.csv', 'rb')
    csv_reader = csv.DictReader(initial_file)
    # Setting fieldnames variable for DictWriter to use, including new column
    # for invalid dates
    fieldnames = csv_reader.fieldnames + ['start_date_description']
    # Using pandas to create lists out of state name & abbreviation columns
    # without opening/reading state file twice with csv module
    state_csv = pd.read_csv('state_abbreviations.csv')
    state_abbrs = state_csv.state_abbr.tolist()
    state_names = state_csv.state_name.tolist()
    # Creating solution csv file & csv DictWriter
    solution_file = open('solution.csv', 'wb')
    csv_writer = csv.DictWriter(solution_file, fieldnames=fieldnames)
    # Writing column headings
    csv_writer.writeheader()
    print "Cleaning Data..."
    for row in csv_reader:
        # Removing extra whitespace from "bio" field for each row
        row['bio'] = " ".join(row['bio'].split())
        # Switching state abbreviation with state name in the spreadsheet using
        # the index of the state abbreviations in the lists created with pandas
        row['state'] = state_names[state_abbrs.index(row['state'])]
        row['start_date_description'] = row['start_date']
        # Tries parsing dates with dateutil.parser
        try:
            # Dateutil.parser assigns a default value to any missing date
            # information. To avoid allowing incomplete dates with added
            # default date information to get into the validated dates data
            # set, this is a workaround to check whether any default values
            # are in any given date. Dateutil.parser allows a default date
            # as a parameter, so by parsing the date with two different
            # defaults, the end results will be different if any of the
            # defaults were used.
            #
            # Parses date with Oct 16, 2000 as the default:
            row_parse1 = parser.parse(row['start_date'],
                                        default=datetime(2000, 10, 16)).date()
            # Parses date with Dec 3, 2008 as the default:
            row_parse2 = parser.parse(row['start_date'],
                                        default=datetime(2008, 12, 3)).date()
            # Checks whether the end results are the same:
            if row_parse1 == row_parse2:
                # If they are equal and the inputted date is valid, the
                # start_date column is set to that valid date:
                row['start_date'] = row_parse1
                # And the start_date_description column is set to blank:
                row['start_date_description'] = ''
            else:
                # If the two parsed dates are not the same, but both parseable,
                # the date is incomplete. The incomplete date is put in the
                # start_date_description column:
                row['start_date_description'] = row['start_date']
                # And the start_date column is set to blank:
                row['start_date'] = ''
        except ValueError:
            # If the date is unparseable by dateutil.parser, it is invalid, and
            # the invalid entry is put in the start_date_description column:
            row['start_date_description'] = row['start_date']
            # And the start_date column is set to blank:
            row['start_date'] = ''
        # Writes new spreadsheet with fixed "bio" rows, state name instead of
        # state abbreviation, and only validated dates in 'start_date' column,
        # and incomplete/invalid dates in the 'start_date_description' column:
        csv_writer.writerow(row)
    print "Cleaning Complete"
    # Nothing to return - output is in csv file

# To run from command line:
'''
python csv_clean.py
'''

#------FOR RUNNING FROM COMMAND LINE------#
csv_clean()
#------FOR RUNNING FROM COMMAND LINE------#

# To run from python shell, comment out the above line, and enter the lines
# below into the python shell:
'''
from csv import csv_clean
csv_clean()
'''
