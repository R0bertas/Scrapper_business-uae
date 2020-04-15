import requests
from urllib.request import urlopen as uReq
import bs4
from bs4 import BeautifulSoup as soup
import lxml
from time import sleep
import time

CompanyNames = []
CompanyURL = []
# this is first page
# http://business-uae.com/eng/biz/jewellers-4800?p=1
for i in range(60,87     ):
    time.sleep(15)
    root = 'http://business-uae.com/eng/biz/jewellers-4800?p=' +str(i)
    print(i)

    uClient = uReq(root)
    page_html = uClient.read()
    uClient.close()

    # html parsing (conversion)
    page_soup = soup(page_html, "html.parser")
      # it will print whole html code
     #print(page_soup)


    # now we will try to get required info
    # finds h2 heading for all info
    Name= page_soup.find_all('h2')

    shortURL="http://business-uae.com"
    # loops in that heading
    for link in Name:
        # find  a attribute which has a href
        for a in link.find_all('a', href=True):
            # getting title apending to list
            CompanyNames.append(a['title'])
            ## gets href link later it will go to company website
            print(a)
            CompanyURL.append(shortURL+a['href'])




#print(soup.find_all("span", { "itemprop"  : "name"}))
#for post in page_soup.find_all("span", { "itemprop"  : "name"}):
 #   print("test")
filename = "customerDataDMCC.csv"
# opening file
f = open(filename, "a", encoding='utf-8')

# adding header
#f.write("ID, Name, Email")  ## THERE IS NO ID , you can create easily in excel

f.write("\n")
for names,url in zip(CompanyNames,CompanyURL):
    f.write(names)
    f.write(",")
    f.write(url)
    f.write("\n")




print(CompanyNames)


