import requests
from urllib.request import urlopen as uReq
import bs4
from bs4 import BeautifulSoup as soup
import lxml
from time import sleep
import time


# this is first page
# http://business-uae.com/eng/biz/jewellers-4800?p=1

root = 'http://business-uae.com/eng/biz/jewellers-4800?p=1'


uClient = uReq(root)
page_html = uClient.read()
uClient.close()

# html parsing (conversion)
page_soup = soup(page_html, "html.parser")
  # it will print whole html code
 #print(page_soup)

# now we will try to get required info

try:
    Name= page_soup.find_all('h2')
    for link in Name:
        print(link.find('a'))
except:
    print("Error")


#print(soup.find_all("span", { "itemprop"  : "name"}))
#for post in page_soup.find_all("span", { "itemprop"  : "name"}):
 #   print("test")
print(Name)



