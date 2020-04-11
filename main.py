from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")  ## can be firefox or any other browser

driver.get("http://business-uae.com/eng/biz/jewellers-4800")

# creating csv file to upload database
filename = "customerDataDMCC.csv"
# opening file
f = open(filename, "w", encoding='utf-8')

# adding header
#f.write("ID, Name, Email")  ## THERE IS NO ID , you can create easily in excel

#f.write( " Name, Email")
#f.write("\n")

# waiting 5sec for iframe to load

time.sleep(5)

def infopage():

    for i in range(2):
        try:
            comp_name = driver.find_element_by_xpath("/html/body/div[5]/div/main/div/div[6]/div[1]/div[1]/div[1]/h2/a/span ").get_attribute("innerHTML")
            print(comp_name)
            driver.find_element_by_xpath(  "/html/body/div[5]/div/main/div/div[6]/div[1]/div[1]/div[1]/h2/a/span ").click()
            time.sleep(2)
        except:
            print("couldn't find name")
        try:
            time.sleep(2)
            #  email = driver.find_element_by_xpath("/html/body/div[5]/div/main/div[1]/section/div[1]/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[2]/span").get_attribute("innerHTML")
            email = driver.find_element_by_xpath("//span[@itemprop='email']").get_attribute("innerHTML")
            print(email)
        except:
            print("no email")


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
infopage()