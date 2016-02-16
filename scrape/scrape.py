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
    '''
    This function uses the BeautifulSoup module to return the HTML on a page
    for any given URL.

    Args:
        url (string): the URL for the webpage from which to scrape all HTML.
    Returns:
        A BeautifulSoup result set with all HTML for the page.
    '''
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    return soup

def check_for_table(page_num):
    '''
    This function determines whether there are company links on a webpage using
    the BeautifulSoup module, in order to determine whether the page needs to be
    scraped. It checks for a table via BeautifulSoup instead of just checking
    the status code of the page with the requests module, because even pages
    with no company information (e.g. 11, 12) still return a successful status
    code (200). There are now ten pages with company links on them, and this
    function would allow the same module to be used even if pages were added or
    removed.

    Args:
        page_num (integer): the page number in the company data domain on which
        to search for company links.
    Returns:
        A Boolean value, True if there are company links on the page, False if
        not.
    '''
    soup = get_soup(domain + next_slug + str(page_num))
    if soup.table:
        return True
    else:
        return False

def scrape_links(page_num):
    '''
    This function uses BeautifulSoup to return all of the company links on a
    specific page within the company information domain.

    Args:
        page_num (integer): the page number of the webpage from which to scrape
        all company links.
    Returns:
        A list of all company links on the page.
    '''
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

def company_info(company_link):
    '''
    This function returns all company info on a page as a single dictionary
    entry, in the correct format to be added to the final dictionary of all
    collected company information.

    Args:
        company_link (string): the string to append to the end of the company
        information domain to get to the company page.
    Returns:
        A dictionary of a single company's information, with the company name
        as the key, and a dictionary of all company info as the value.
    '''
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


#=============================================================================#

def data_to_json():
    '''
    This function uses the helper functions get_soup, check_for_table,
    scrape_links, and company_info to iterate through all pages of company
    links and company information pages within the company information domain
    (http://data-interview.enigmalabs.org/companies/) and return all of the
    company data in JSON.

    Args:
        N/A
    Returns:
        A JSON object of all company information. The keys are the company
        names, and the values are the dictionaries of company information
        retrieved from each company information page.
    '''
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
    # Checks if there is table data on the page using check_for_table function:
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
    # Note: if running from the python shell, it will print twice unless the
    # output is saved to a variable, due to the return statement.
    #----------------PRINT----------------#
    print "Company Data Information (Unicode Encoded):"
    pp.pprint(company_info_dict)
    #-------------------------------------#
    # Uncomment these two lines to save the JSON data to a file:
    #----------------SAVE----------------#
    with open('solution.json', 'w') as outfile:
        json.dump(company_info_dict, outfile)
    #------------------------------------#
    return company_info_json


if __name__ == '__main__':
    data_to_json()


# To run from command line:
'''
python scrape.py
'''

# To run from python shell:
'''
from scrape import data_to_json
data_to_json()
'''
