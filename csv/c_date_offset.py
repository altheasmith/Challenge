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

def date_offset(csv_file):
    '''
    This function opens and reads a csv file with a 'start_date' field, and
    determines whether the content of the field in each line is a valid date
    using the dateutil parser. If the date is valid, it is left in the
    'start_date' field, and if not, it is moved to a newly created
    'start_date_description' field.

    Args:
        csv_file (csv file): A CSV file in the same directory as the string
        cleaning module, with a 'start_date' field.
    Returns:
        A csv file in the same directory called 'solution.csv', with only
        validated dates in the 'start_date' field in ISO 8601 format, and
        invalid or incomplete dates in a new 'start_date_description' field.
    Raises:
        ValueError, if the dateutil parser determines the startdate is
        incomplete.
    '''
    print "Reading CSV..."
    # Opens csv file and creating csv DictReader:
    with open(csv_file, 'rb') as initial_file:
        csv_reader = csv.DictReader(initial_file)
        # Sets fieldnames variable for DictWriter to use, including new column
        # for invalid dates
        fieldnames = csv_reader.fieldnames + ['start_date_description']
        # Creates solution csv file & csv DictWriter
        with open('solution.csv', 'wb') as solution_file:
            csv_writer = csv.DictWriter(solution_file, fieldnames=fieldnames)
            # Writes column headings
            csv_writer.writeheader()
            print "Validating Dates..."
            for row in csv_reader:
                # Tries parsing dates with dateutil.parser
                try:
                    # Dateutil.parser assigns a default value to any missing date
                    # information. To avoid allowing incomplete dates with added
                    # default date information to get into the validated dates data set,
                    # this is a workaround to check whether any default values are in
                    # any given date. Dateutil.parser allows a default date as a
                    # parameter, so by parsing the date with two different defaults,
                    # the end results will be different if any of the defaults were
                    # used.
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
                        # the date is incomplete, and incurs the ValueError exception:
                        raise ValueError('Incomplete Date')
                except ValueError:
                    # If the date is unparseable by dateutil.parser, it is invalid.
                    # Incomplete and invalid entries are put in the
                    # start_date_description column:
                    row['start_date_description'] = row['start_date']
                    # And the start_date column is set to blank:
                    row['start_date'] = ''
                # Writing new spreadsheet with only validated dates in 'start_date'
                # column, and incomplete/invalid dates in the 'start_date_description'
                # column:
                csv_writer.writerow(row)
            print "Validation Complete"
            # Nothing to return - output is in csv file


if __name__ == '__main__':
    date_offset('test.csv')


# To run from command line:
'''
python c_date_offset.py
'''

# To run from python shell:
'''
from c_date_offset import date_offset
date_offset('test.csv')
'''
