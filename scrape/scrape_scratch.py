Regex for scraping company links:

# pattern = re.compile('\/companies\/(\w+\s*)+')
# company_links = []
# for link in link_values:
#     if pattern.match(link):
#         company_links.append(link)


def page_url(page_num):
    return requests.get(domain + next_slug + str(page_num)).urls
