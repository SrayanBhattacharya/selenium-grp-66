from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import time

browsername = input("Enter the name of the browser that you want to use : ")
#What actions for chrome or firefox browsers
if browsername.lower()=="chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browsername.lower()=="firefox":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    raise Exception("Invalid browser name. Please choose 'chrome' or 'firefox'." )

driver.get("https://testautomationpractice.blogspot.com/")

try:
    #Dropdown
    Select(driver.find_element(By.ID,"country")).select_by_value("india")
    #Multi-select List
        #List1
    Select(driver.find_element(By.ID,"colors")).select_by_visible_text("Red")
        #List2
    Select(driver.find_element(By.ID,"animals")).select_by_visible_text("Deer")
    

    time.sleep(10) 
finally:
    driver.quit()