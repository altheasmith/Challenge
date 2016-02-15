# Challenge:

# Code swap - There is a supplementary CSV file for download here:
# state_abbreviations.csv. This "data dictionary" contains state abbreviations
# alongside state names. For the state field of the input CSV, replace each
# state abbreviation with its associated state name from the data dictionary.

import csv

def code_swap(csv_file):
    '''
    This function opens and reads a csv file with a 'state' field, and replaces
    state abbreviations in the 'state' field with the full state name, using
    a dictionary lookup created with another CSV file with a state abbreviation
    and a state name column.

    Args:
        csv_file (csv file): A CSV file in the same directory as the string
        cleaning module, with a 'state' field.
    Returns:
        A csv file in the same directory called 'solution.csv', with the full
        state name in the 'state' field instead of the state abbreviation.
    '''
    print "Reading CSV..."
    # Opens csv file and creates csv DictReader for test.csv file
    with open(csv_file, 'rb') as initial_file:
        csv_reader = csv.DictReader(initial_file)
        # Sets fieldnames variable for DictWriter to use
        fieldnames = csv_reader.fieldnames
        # Opens state csv file and creates csv DictReader for
        # state_abbreviations.csv file
        with open('state_abbreviations.csv', 'rb') as state_file:
            state_reader = csv.DictReader(state_file)
            # Creates dictionary with state abbr as key and state name as value
            state_dict = {row['state_abbr']: row['state_name'] for row in state_reader}
            # Creates solution csv file & csv DictWriter
            with open('solution.csv', 'wb') as solution_file:
                csv_writer = csv.DictWriter(solution_file, fieldnames=fieldnames)
                # Writes column headings
                csv_writer.writeheader()
                print "Replacing State Abbreviation with State Name..."
                for row in csv_reader:
                    # Switches state abbreviation with state name in the
                    # spreadsheet using the dictionary created from the state
                    # abbreviations file
                    row['state'] = state_dict[row['state']]
                    # Writes solution csv with state name instead of state
                    # abbreviation
                    csv_writer.writerow(row)
                print "Replacement Complete"
                # Nothing to return - output is in csv file


if __name__ == '__main__':
    code_swap('test.csv')


# To run from command line:
'''
python b_code_swap.py
'''

# To run from python shell:
'''
from b_code_swap import code_swap
code_swap('test.csv')
'''
