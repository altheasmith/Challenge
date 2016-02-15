# Challenge:

# String cleaning - The bio field contains text with arbitrary padding, spacing
# and line breaks. Normalize these values to a space-delimited string.

import csv

def string_cleaning(csv_file):
    '''
    This function opens and reads a CSV file, and removes extra whitespace
    characters from the 'bio' field, resulting in a single-space delimited text
    field. The original CSV file and the resulting CSV use csv.QUOTE_MIMIMAL to
    determine which fields are surrounded by quotes. As a result, the bio field
    is quoted in the original and not quoted in the solution, as it no longer
    contains characters requiring the field to be quoted.

    Args:
        csv_file (csv file): A CSV file in the same directory as the string
        cleaning module, with a 'bio' field.
    Returns:
        A csv file in the same directory called 'solution.csv', with extra
        whitespace characters cleaned from the 'bio' field.
    '''
    print "Reading CSV..."
    # Opens csv file and creating csv DictReader:
    with open(csv_file, 'rb') as initial_file:
        csv_reader = csv.DictReader(initial_file)
        # Sets fieldnames variable for DictWriter to use
        fieldnames = csv_reader.fieldnames
        # Creates solution csv file & csv DictWriter
        with open('solution.csv', 'wb') as solution_file:
            csv_writer = csv.DictWriter(solution_file, fieldnames=fieldnames)
            # Writes column headings
            csv_writer.writeheader()
            print "Cleaning Bios..."
            for row in csv_reader:
                # Removes extra whitespace from "bio" field for each row
                row['bio'] =" ".join(row['bio'].split())
                # Writes new spreadsheet with fixed "bio" rows
                csv_writer.writerow(row)
            print "Cleaning Complete"
            # Nothing to return - output is in csv file


if __name__ == '__main__':
    string_cleaning('test.csv')


# To run from command line:
'''
python a_string_cleaning.py
'''

# To run from python shell
'''
from a_string_cleaning import string_cleaning
string_cleaning('test.csv')
'''
