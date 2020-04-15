import requests
from urllib.request import urlopen as uReq
import bs4
from bs4 import BeautifulSoup as soup
import lxml
from time import sleep
import time

## for reading csv files  makes life easier
import csv

f = open("customerDataDMCC.csv", "r", encoding='utf-8')
csv_f = csv.reader(f)
# skips first line  where is Name, Email
next(csv_f)

## skips first 30 rows because there is bot detector so every 30 info we will check marking manually
for i in range(0):
    next(csv_f)
Names=[]
EMAIL=[]
counter=1
for row in csv_f:

    root = row[1]
    print(counter)
    ## theese 3 line will read the link
    uClient = uReq(root)
    page_html = uClient.read()
    uClient.close()

    # html parsing (conversion)
    page_soup = soup(page_html, "html.parser")
    Name = page_soup.find_all('table')
    for mail in Name:
        email=mail.find("span", itemprop="email").text
        print(email)
        Names.append(row[0])
        EMAIL.append(email)
    #time.sleep(15)
    if counter==40:
        break
    counter += 1
f.close()


#filepath = 'customerDataDMCC.csv'
#with open(filepath) as fp:
 #  line = fp.readline()
  # cnt = 1
   #while line:
    #   print("Line {}: {}".format(cnt, line.strip()))
     #  line = fp.readline()
      # cnt += 1

filename = "Email.csv"
# opening file
count=0
f = open(filename, "w", encoding='utf-8')

for mail,name in zip(EMAIL,Names):
    f.write(str(count))
    f.write(",")
    f.write(name)
    f.write(",")
    f.write(mail)
    f.write(",\n")
    count+=1