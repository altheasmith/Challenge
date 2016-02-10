# Challenge:

# Write a script to scrape a sample site and output its data in JSON.
# edgar is a company listings site containing ten pages of company links.
# Each link endpoint holds company-specific data such as name, description and
# address. The sole requirement of this part of the test is to produce JSON of
# all of the company listings data for the site.

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(http://data-interview.enigmalabs.org/companies, 'html.parser')
# print soup.prettify()

wget('http://data-interview.enigmalabs.org/companies"
