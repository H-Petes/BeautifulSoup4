import requests
from bs4 import BeautifulSoup

# using the request module, we use the 'get' function
# provided access to the webpage provided as an
# argument to this function:

result = requests.get('https://www.google.com/')

# To make sure that the website is accessible, we can
# ensure that we obtain a 200 ok response to indicate
# That the page is indeed present:

print(result.status_code)

# for other potential status codes you may encounter,
# consult the following Wikipedia page:
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# we can also check the HTTP header of the website to
# verify that we have indeed accessed the correct page:

print(result.headers)

# for more information on HTTP headers and the informaton
# one can obtain from them, you may consult:
# https://en.wikipedia.org/wiki/List_of_HTTP header fields

# now, let us stoe the page content of the website accessed
# from requests to a variable:

src = result.content

# now that we have the page source stored, we will use the
# BeautifulSoup module to parse and process the source.
# To do so, we create a BeautifulSoup object based on the
# source variable we created above:

soup = BeautifulSoup(src, 'lxml')

# Now that the page source has been processed via BeautifulSoup
# we can access specific information directly from it. For instance,
# say we want to see a list of all the links on the page:

links = soup.find_all('a')
print(links)
print('\n')

# perhaps we just want to extract the link that has contains the text
# 'Kuhusu' on the page instead of every link. we can use built-in
# 'text' function to access the text content between the <a></a>
# tags

for link in links:
    if 'Kuhusu' in link.text:
        print(link)
        print(link.attrs['href'])
