from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

git = os.getenv("GIT")
password = os.getenv("PASSWORD")

print("----------------------------------")
print("Trying to connect to Github with username " + git)
print("----------------------------------")

driver = webdriver.Firefox()
driver.implicitly_wait(30)

driver.get("https://github.com/login")

username_field = driver.find_element_by_id("login_field").send_keys(git)
password_field = driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[12]").click()
print("----------------------------------")
print("Connected")
print("----------------------------------")