from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from dotenv import load_dotenv
import os

load_dotenv()

git = os.getenv("GIT")
password = os.getenv("PASSWORD")

print("-"*30)
print("Trying to connect to Github with username " + git)
print("-"*30)

driver = webdriver.Firefox()
driver.implicitly_wait(30)

driver.get("https://github.com/login")

username_field = driver.find_element_by_id("login_field").send_keys(git)
password_field = driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[12]").click()
driver.get("https://github.com/new")
print("-"*30)
print("Please enter the name for your repo")
print("-"*30)
repoName = str(input())
driver.find_element_by_id("repository_name").send_keys(repoName)
print("-"*30)
print("Please choose some privacy options")
print("1: Public")
print("2: Private")
print("-"*30)
privacy = int(input())
if privacy == 1:
	driver.find_element_by_id("repository_visibility_public").click()
elif privacy == 2:
	driver.find_element_by_id("repository_visibility_private").click()
else:
	print("-"*30)
	print("Error")
	print("-"*30)
	driver.quit()
	exit()
driver.find_element_by_id("repository_auto_init").click()
driver.find_element_by_id("repository_gitignore_template_toggle").click()
driver.find_element_by_id("repository_name").send_keys(Keys.RETURN)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/main/div[1]/nav/ul/li[1]/a/span[1]"))
    )
finally:
    driver.quit()
print("-"*30)
print("Successfully created Repository with the name " + repoName)
print("-"*30)
