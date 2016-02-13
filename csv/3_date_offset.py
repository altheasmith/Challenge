# Challenge:

# Date offset (bonus) - The start_date field contains data in a variety of
# formats. These may include e.g., "June 23, 1912" or "5/11/1930" (month, day,
# year). But not all values are valid dates. Invalid dates may include e.g.,
# "June 2018", "3/06" (incomplete dates) or even arbitrary natural language.
# Add a start_date_description field adjacent to the start_date column to
# filter invalid date values into. Normalize all valid date values in
# start_date to ISO 8601 (i.e., YYYY-MM-DD).

import csv
from datetime import datetime
import dateutil.parser as parser

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
    return

date_offset()
