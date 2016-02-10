# Challenge:

# Code swap - There is a supplementary CSV file for download here:
# state_abbreviations.csv. This "data dictionary" contains state abbreviations
# alongside state names. For the state field of the input CSV, replace each
# state abbreviation with its associated state name from the data dictionary.

import csv

initial_file = open('test.csv', 'rb')
csv_reader = csv.DictReader(initial_file)
fieldnames = next(csv_reader).keys()
solution_file = open('solution.csv', 'wb')
csv_writer = csv.DictWriter(solution_file, fieldnames=fieldnames)
csv_writer.writeheader()
for row in csv_reader:
    row['bio'] = " ".join(row['bio'].split())
    csv_writer.writerow(row)
