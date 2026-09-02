from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#by id
name=driver.find_element(By.ID, "name")
name.send_keys("Reetoja")

#by name
gender=driver.find_element(By.NAME, "gender")
print("Gender field found using By.NAME")

#by tag name
inputs=driver.find_elements(By.TAG_NAME, "input")
print("Number of input elements:", len(inputs))

#by link text
apple=driver.find_element(By.LINK_TEXT, "Apple")
print("Apple link found using By.LINK_TEXT")

#by class name
element=driver.find_element(By.CLASS_NAME, "form-control")
print("Element found using By.CLASS_NAME")
time.sleep(3)
driver.quit()


                        