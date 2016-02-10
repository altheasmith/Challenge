# Challenge:

# Code swap - There is a supplementary CSV file for download here:
# state_abbreviations.csv. This "data dictionary" contains state abbreviations
# alongside state names. For the state field of the input CSV, replace each
# state abbreviation with its associated state name from the data dictionary.

import csv

initial_file = open('test.csv', 'rb')
csv_reader = csv.DictReader(initial_file)
state_file = open('state_abbreviations.csv', 'rb')
state_reader = csv.DictReader(state_file)
state_names = [row['state_name'] for row in state_reader]
# Re-declaring state_reader for second list comprehension
state_file = open('state_abbreviations.csv', 'rb')
state_reader = csv.DictReader(state_file)
state_abbrs = [row['state_abbr'] for row in state_reader]
solution_file = open('solution.csv', 'wb')
fieldnames = next(csv_reader).keys()
csv_writer = csv.DictWriter(solution_file, fieldnames=fieldnames)
csv_writer.writeheader()
for row in csv_reader:
    row['state'] = state_names[state_abbrs.index(row['state'])]
    csv_writer.writerow(row)

# Try with one for loop
# Try with 'vlookup' command
