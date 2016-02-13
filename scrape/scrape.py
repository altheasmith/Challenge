# Challenge:

# Write a script to scrape a sample site and output its data in JSON.
# edgar is a company listings site containing ten pages of company links.
# Each link endpoint holds company-specific data such as name, description and
# address. The sole requirement of this part of the test is to produce JSON of
# all of the company listings data for the site.

#=============================================================================#

# Imports and setup:
import requests
from bs4 import BeautifulSoup
import json

# Initializing values for: dictionary of company info, the base domain of
# the set of company info, the section of the url between the domain and the
# page number, sectioned out to allow for dynamic page incrementation, and the
# starting page number (1).
company_info_dict = {}
domain = 'http://data-interview.enigmalabs.org'
next_slug = '/companies/?page='
page_num = 1

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
    info_dict = {}
    url = domain + company_link
    soup = get_soup(url)
    rows = soup.find_all('tr')
    cell_list = [row.find_all('td') for row in rows]
    for cell in cell_list:
        info_dict[cell[0].text.encode('ascii')] = cell[1].text.encode('ascii')
    company_name = info_dict['Company Name']
    return company_name, info_dict

# company_info_dict[company_name] = info_dict


def scrape_links(page_num):
    # Get all company links on one page
    url = domain + next_slug + str(page_num)
    soup = get_soup(url)
    link_tags = soup.table.find_all('a')
    company_links = [link['href'] for link in link_tags]
    return company_links


def data_to_json():
    # Function to scrape all company data from the set of pages beginning at
    # http://data-interview.enigmalabs.org/companies/, and return it as JSON
    #------------------------------------------------------------------------#
    # Initializing Values
    #------------------------------------------------------------------------#
    # Base domain of the company info site:
    domain = 'http://data-interview.enigmalabs.org'
    # The section of the url between the domain and the page number, sectioned
    # out to allow for dynamic page incrementation:
    next_slug = '/companies/?page='
    # The starting page number (1) to begin iteration:
    page_num = 1
    # The list of all relative links with company data
    company_links = []
    # The final dictionary of data from which the returned JSON will be built
    company_info_dict = {}
    #------------------------------------------------------------------------#
    while check_for_table(page_num):
        print "Scraping company links from page " + str(page_num) + "..."
        company_links += scrape_links(page_num)
        page_num += 1
    for link in company_links:
        print "Scraping company info from " + link + "..."
        company_name, info_dict = company_info(link)
        # Setting key - value pair in final dictionary
        company_info_dict[company_name] = info_dict
    print "Company Data JSON:\n"
    return company_info_dict
