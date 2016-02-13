# Challenge:

# Write a script to scrape a sample site and output its data in JSON.
# edgar is a company listings site containing ten pages of company links.
# Each link endpoint holds company-specific data such as name, description and
# address. The sole requirement of this part of the test is to produce JSON of
# all of the company listings data for the site.

#=============================================================================#

#-----------------------------------------------------------------------------#
# Imports
#-----------------------------------------------------------------------------#
import requests
from bs4 import BeautifulSoup
import json
import pprint

#-----------------------------------------------------------------------------#
# Initializing Values
#-----------------------------------------------------------------------------#
# Base domain of the company info site:
domain = 'http://data-interview.enigmalabs.org'
# The section of the url between the domain and the page number, sectioned
# out to allow for dynamic page incrementation:
next_slug = '/companies/?page='
# Creating Pretty Printer:
pp = pprint.PrettyPrinter()

#-----------------------------------------------------------------------------#
# Helper Functions
#-----------------------------------------------------------------------------#
def get_soup(url):
    # Returns all html data for a given webpage via Beautiful Soup
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    return soup

def check_for_table(page_num):
    # Determines whether there is company info on a page.
    # This function uses beautiful soup to check for table data instead of
    # checking the status code of the page, because pages without data (e.g. 11,
    # 12) still return status code of 200
    soup = get_soup(domain + next_slug + str(page_num))
    if soup.table:
        return True
    else:
        return False

def company_info(company_link):
    # Gets company info and returns the dictionary of company info and the
    # company name, which will serve as the key - value pair respectively in
    # the final dictionary of info.
    #------------------------------------------------------------------------#
    # Creates url to scrape for company info:
    url = domain + company_link
    # Retrieves webpage as html "soup" with Beautiful Soup/get_soup() function:
    soup = get_soup(url)
    # Returns all table rows on page, as data is stored in a table:
    rows = soup.find_all('tr')
    # List comprehension for retrieving lists of each key value pair in
    # company information table:
    cell_list = [row.find_all('td') for row in rows]
    # Creates a dictionary entry for each key-value pair of a company
    # information item in an html table row:
    info_dict = {cell[0].text: cell[1].text for cell in cell_list}
    # Stores the company name as its own variable, for the creation of a key -
    # value pair of {company name: {company data}} in the final dictionary:
    company_name = info_dict['Company Name']
    # Returns company data & data variables:
    return company_name, info_dict

def scrape_links(page_num):
    # Gets all company links on a single page:
    #------------------------------------------------------------------------#
    # Creates url for the page number specified by page_num
    url = domain + next_slug + str(page_num)
    # Returns all table rows on page, as data is stored in a table:
    soup = get_soup(url)
    # Finds and returns all link html tags within a table on the page, as
    # company data is only stored in the table. The company info links can also
    # be found if all links are returned and checked against the regex:
    # '\/companies\/(\w+\s*)+':
    link_tags = soup.table.find_all('a')
    # Pulls text of relative link from each html link tag:
    company_links = [link['href'] for link in link_tags]
    # Returns list of company links for the page
    return company_links

#=============================================================================#

def data_to_json():
    # Function to scrape all company data from the set of pages beginning at
    # http://data-interview.enigmalabs.org/companies/, and return it as JSON
    #------------------------------------------------------------------------#
    # Initializing Values
    #------------------------------------------------------------------------#
    # The starting page number (1) to begin iteration:
    page_num = 1
    # The list of all relative links with company data
    company_links = []
    # The final dictionary of data from which the returned JSON will be built
    company_info_dict = {}
    # The final JSON object built from the dictionary of company data
    company_info_json = {}
    #------------------------------------------------------------------------#
    # Scraping all company links from all pages with data:
    #------------------------------------------------------------------------#
    # Checks if there is table data on the page using check_for_data function:
    while check_for_table(page_num):
        print "Scraping company links from page " + str(page_num) + "..."
        # Returns list of company links with scrape_links function, per page
        company_links += scrape_links(page_num)
        # Increments page number, so the next page can be checked/scraped
        page_num += 1
    #------------------------------------------------------------------------#
    # Scraping all company data from each link in list of company links:
    #------------------------------------------------------------------------#
    # Iterates through each link in company links list
    for link in company_links:
        print "Scraping company info from " + link + "..."
        # Returns the company name and dictionary of company info for each link
        company_name, info_dict = company_info(link)
        # Sets {company name: {company data}} key-value pair in final dictionary
        company_info_dict[company_name] = info_dict
    # JSON-ifying company info dictionary:
    company_info_json = json.dumps(company_info_dict)
    #------------------------------------------------------------------------#
    # Returning JSON-ified dictionary, and optional Data Print/File Dump
    #------------------------------------------------------------------------#
    # Uncomment these two lines to print the company information (unicode):
    #----------------PRINT----------------#
    print "Company Data Information (Unicode Encoded):"
    pp.pprint(company_info_dict)
    #-------------------------------------#
    # Uncomment these two lines to save the JSON data to a file:
    #----------------SAVE----------------#
    # with open('company_data.json', 'w') as outfile:
    #     json.dump(company_info_dict, outfile)
    #------------------------------------#
    return company_info_json

# To run from command line:
'''
python scrape.py
'''

#------FOR RUNNING FROM COMMAND LINE------#
data_to_json()
#-----------------------------------------#

# To run from python shell, comment out the above line, and enter the lines
# below into the python shell:
'''
from scrape import data_to_json
data_to_json()
'''
