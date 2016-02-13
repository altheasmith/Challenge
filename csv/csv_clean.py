import csv
from datetime import datetime
import dateutil.parser as parser
import pandas as pd

def string_cleaning():
    print "Reading CSV..."
    # Opening csv file and creating csv DictReader:
    initial_file = open('test.csv', 'rb')
    csv_reader = csv.DictReader(initial_file)
    # Setting fieldnames variable for DictWriter to use
    fieldnames = next(csv_reader).keys()
    # Creating solution csv file & csv DictWriter
    solution_file = open('solution.csv', 'wb')
    csv_writer = csv.DictWriter(solution_file, fieldnames=fieldnames)
    # Writing column headings
    csv_writer.writeheader()
    print "Cleaning Bios..."
    for row in csv_reader:
        # Removing extra whitespace from "bio" field for each row
        row['bio'] = " ".join(row['bio'].split())
        # Writing new spreadsheet with fixed "bio" rows
        csv_writer.writerow(row)
    print "Cleaning Complete"


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

def date_offset():
    print "Reading CSV..."
    initial_file = open('test.csv', 'rb')
    fieldnames_reader = csv.reader(initial_file)
    fieldnames = fieldnames_reader.next() + ['start_date_description']
    initial_file = open('test.csv', 'rb')
    csv_reader = csv.DictReader(initial_file)
    solution_file = open('solution.csv', 'wb')
    csv_writer = csv.DictWriter(solution_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    print "Validating Dates..."
    for row in csv_reader:
        row['start_date_description'] = row['start_date']
        try:
            row_parse1 = parser.parse(row['start_date'],
                                        default=datetime(2000, 10, 16)).date()
            row_parse2 = parser.parse(row['start_date'],
                                        default=datetime(2008, 12, 3)).date()
            if row_parse1 == row_parse2:
                row['start_date'] = row_parse1
                row['start_date_description'] = ''
            else:
                row['start_date_description'] = row['start_date']
                row['start_date'] = ''
        except ValueError:
            row['start_date_description'] = row['start_date']
            row['start_date'] = ''
        csv_writer.writerow(row)
    print "Validation Complete"
