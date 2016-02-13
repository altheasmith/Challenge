Part 1 - CSV Test

TODO Write a script to transform input CSV to desired output CSV.

You will find a CSV file available for download here: test.csv. There are two steps (plus an optional bonus) to this part of the test. Each step concerns manipulating the values for a single field according to the step's requirements. The steps are as follows:

1. String cleaning - The bio field contains text with arbitrary padding, spacing and line breaks. Normalize these values to a space-delimited string.
2. Code swap - There is a supplementary CSV file for download here: state_abbreviations.csv. This "data dictionary" contains state abbreviations alongside state names. For the state field of the input CSV, replace each state abbreviation with its associated state name from the data dictionary.
3. Date offset (bonus) - The start_date field contains data in a variety of formats. These may include e.g., "June 23, 1912" or "5/11/1930" (month, day, year). But not all values are valid dates. Invalid dates may include e.g., "June 2018", "3/06" (incomplete dates) or even arbitrary natural language. Add a start_date_description field adjacent to the start_date column to filter invalid date values into. Normalize all valid date values in start_date to ISO 8601 (i.e., YYYY-MM-DD).
Your script should take "test.csv" as input and produce a cleansed "solution.csv" file according to the step requirements above. Please attach your "solution.csv" file along with your solution code in your reply!

Recommended libraries:

Python's csv module is standard for dealing with CSV data.


Part 2 - Web Scrape

TODO Write a script to scrape a sample site and output its data in JSON.

edgar is a company listings site containing ten pages of company links. Each link endpoint holds company-specific data such as name, description and address. The sole requirement of this part of the test is to produce JSON of all of the company listings data for the site.

Recommended libraries:

Beautiful Soup contains a robust HTML parser.
Python's json module is convenient for JSON format.

Assessment Criteria

Your ability to effectively solve the problems posed.
Your ability to solve these problems in a clear and logical manner, with tasteful design.
Your ability to appropriately document and comment your code.
When in doubt, import this.
