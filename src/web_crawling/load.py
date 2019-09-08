import urllib.request
from bs4 import BeautifulSoup

urls = "https://www.partnc.org/"
html_list = []
a_list = []


def url_load(u, hl):  # opens up index.html and then runs then appends html dat to htmlList
    f = urllib.request.urlopen(u)
    mf = f.read()
    h_soup = BeautifulSoup(mf, 'html.parser')
    list.append(hl, h_soup)
    return h_soup


data = url_load(urls, html_list)





# cleans up the url to only include root domain url
# ex. https://www.walter.com => walter.com


def domain(u):
    d = u
    if 'https://www.' in d:
        u.replace('https://www.', '')
    elif 'http://www.' in d:
        u.replace('http://www.', '')
    elif 'http://' in d:
        u.replace('http://', '')
    elif 'https://' in d:
        u.replace('https://', '')
    return d


dom = domain(urls)


# 3. runs a check to see if the links in the page contain the domain
# and then add that to aList
# and then then adds then appends htmlList
def all_links(al, hl):
    for link in data.find_all('a'):
        if dom in link:
            a = link.get('href')
            list.append(a, al)
    for link in al:
        f = urllib.request.urlopen(link)
        mf = f.read()
        soup = BeautifulSoup(mf, 'html.parser')
        list.append(hl, soup)
        return mf


fin = all_links(a_list, html_list)

print(a_list)

print(html_list)


