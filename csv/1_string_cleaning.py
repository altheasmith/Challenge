# Challenge:

# String cleaning - The bio field contains text with arbitrary padding, spacing
# and line breaks. Normalize these values to a space-delimited string.

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
