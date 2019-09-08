import urllib.request
from bs4 import BeautifulSoup

urls = "https://www.partnc.org/"
aList = []
html_list = []


def url_load(u, hl):  # opens up index.html and then runs then appends html dat to htmlList
    f = urllib.request.urlopen(u)
    mf = f.read()
    list.append(mf, hl)
    return mf


data = url_load(urls, html_list)


soup = BeautifulSoup(data, 'html.parser')


# cleans up the url to only include root domain url
# ex. https://www.walter.com => walter.com


def domain(u):
    d = u
    if 'https://www.' in d:
        u.replace('https://www.','')
    elif 'http://www.' in d:
        u.replace('http://www.','')
    elif 'http://' in d:
        u.replace('http://','')
    elif 'https://' in d:
        u.replace('https://','')
    return d


dom = domain(urls)


# 3. runs a check to see if the links in the page contain the domain
# and then add that to aList
# and then then adds then appends htmlList
def all_links(aL, hl):
    for link in soup.find_all('a'):
        if dom in link:
            a = link.get('href')
            list.append(a, aL)
    for link in aL:
        f = urllib.request.urlopen(link)
        mf = f.read()
        list.append(mf, hl)
        return mf






