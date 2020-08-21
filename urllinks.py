import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('https://noragami.fandom.com/wiki/Category:Characters', context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

links = list()

# Retrieve all anchor tags
tags = soup('a')
for tag in tags:
    links.append(str(tag.get('href', None)))

nothanks = ["Category", "Blog", "List", "Community", "Template", "Special", "Forum", "Local", "God", "Phantom", "Shinki", "Noragami", "Adachitoka"]

final_list = list()

for link in links:
    if any(x in link for x in nothanks):
        continue
    elif link.startswith('/wiki/'):
        res = link.replace('/wiki/', '')
        final = res.replace('_', ' ')
        if final not in final_list:
            final_list.append(final)

for name in sorted(final_list):
    print(name)
