from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import  random
driver = webdriver.Chrome(executable_path="chromedriver.exe")  ## can be firefox or any other browser

driver.get("http://business-uae.com/eng/biz/jewellers-4800")

# creating csv file to upload database
filename = "customerDataDMCC.csv"
# opening file
f = open(filename, "w", encoding='utf-8')

# adding header
#f.write("ID, Name, Email")  ## THERE IS NO ID , you can create easily in excel

f.write( "Name, Email")
f.write("\n")

# waiting 5sec for to load
time.sleep(5)

# this is first page
# http://business-uae.com/eng/biz/jewellers-4800?p=1

url  = "http://business-uae.com/eng/biz/jewellers-4800?p="

# this method gathers info from x page  , it has 20 companies in it
def infopage(x):
    print("which page one: " + str(x)  )
    for i in range(1,24):
        temp_url = url + str(x)
        print(" check name" + str(i))
        driver.get(temp_url)
        if i== 2 or i==3:
            continue
        try:
            time.sleep(random.randint(4,15))
            comp_name = driver.find_element_by_xpath("/html/body/div[5]/div/main/div/div[6]/div[1]/div[ "+ str(i) +"]/div[1]/h2/a/span ").get_attribute("innerHTML")
            print(comp_name)

            f.write(comp_name)

            # goes to another compnay page to get an email
            driver.find_element_by_xpath(  "/html/body/div[5]/div/main/div/div[6]/div[1]/div[ "+ str(i) +"]/div[1]/h2/a/span ").click()
        except:
            f.write("-")
            print("couldn't find name")

        f.write(",")
        time.sleep(random.randint(4,15))
        try:

            #  email = driver.find_element_by_xpath("/html/body/div[5]/div/main/div[1]/section/div[1]/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[2]/span").get_attribute("innerHTML")
            email = driver.find_element_by_xpath("//span[@itemprop='email']").get_attribute("innerHTML")
            f.write(email)
            print(email)
        except:
            f.write("-")
            print("no email")

        f.write("\n")
        # this will go to another pager  we create temp because we need to keep starting url  with empty p=
        time.sleep(random.randint(4,15))

# /html/body/div[5]/div/main/div/div[6]/div[1]/div[1]/div[1]/h2/a/span
# /html/body/div[5]/div/main/div/div[6]/div[1]/div[1]/div[1]/h2/a/span
#
# /html/body/div[5]/div/main/div/div[6]/div[1]/div[4]/div[1]/h2/a/span
# /html/body/div[5]/div/main/div/div[6]/div[1]/div[4]/div[1]/h2/a/span
#
# /html/body/div[5]/div/main/div/div[6]/div[1]/div[5]/div[1]/h2/a/span
# /html/body/div[5]/div/main/div/div[6]/div[1]/div[5]/div[1]/h2/a/span
#
# /html/body/div[5]/div/main/div/div[6]/div[1]/div[6]/div[1]/h2/a/span
for i in range(1,12):
    time.sleep(random.randint(4,15))
    infopage(i)