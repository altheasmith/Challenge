# Challenge:

# String cleaning - The bio field contains text with arbitrary padding, spacing
# and line breaks. Normalize these values to a space-delimited string.

import csv

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
    return

string_cleaning()
