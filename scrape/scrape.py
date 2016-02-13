# Challenge:

# Write a script to scrape a sample site and output its data in JSON.
# edgar is a company listings site containing ten pages of company links.
# Each link endpoint holds company-specific data such as name, description and
# address. The sole requirement of this part of the test is to produce JSON of
# all of the company listings data for the site.

import requests
from bs4 import BeautifulSoup
import re

company_info_dict = {}
domain = 'http://data-interview.enigmalabs.org'

# Get all pages with company links
next_slug = '/companies/?page='
pages = []
page_num = 1

def get_soup(page_num):
    page = requests.get(domain + next_slug + str(page_num))
    soup = BeautifulSoup(page.text)
    return soup

def check_for_table(page_num):
    soup = get_soup(domain + next_slug + str(page_num))
    if soup.table:
        return True
    else:
        return False


def page_url(page_num):
    return requests.get(domain + next_slug + str(page_num)).url

# Get company info and return as entry in company_info_dict
slug = "Douglas,%20Walsh%20and%20Luettgen"
page = requests.get('http://data-interview.enigmalabs.org/companies/' + slug)
soup = BeautifulSoup(page.text)
table = soup.table()
rows = soup.find_all('tr')
info_dict = {}
cell_list = [row.find_all('td') for row in rows]
for cell in cell_list:
    info_dict[cell[0].text.encode('ascii')] = cell[1].text.encode('ascii')
company_dict_key = info_dict['Company Name']
company_info_dict[company_dict_key] = info_dict

def scrape_links(page_num):
# Get all company links on one page
    soup = get_soup(page_num)
    link_tags = soup.table.find_all('a')
    company_links = [link['href'] for link in link_tags]
    return company_links
# pattern = re.compile('\/companies\/(\w+\s*)+')
# company_links = []
# for link in link_values:
#     if pattern.match(link):
#         company_links.append(link)

# Get all pages with company links
next_slug = '/companies/?page='
page_num = 1
page = requests.get(domain + next_slug + str(page_num))
if page.status_code == 200:
    pages.append(page.url).encode('ascii')
