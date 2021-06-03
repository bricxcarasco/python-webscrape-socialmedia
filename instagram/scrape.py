from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import wget
import time

# Use dotenv for account credentials
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path)

# Account credentials in .env file
instagram_username = os.environ.get('INSTAGRAM_USERNAME')
instagram_password = os.environ.get('INSTAGRAM_PASSWORD')

# Relative path of chromedriver in the project
dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, '../chromedriver')

# Create an insstance of chromediver
driver = webdriver.Chrome(file_path)
# Load the url site path for web scraping
driver.get('https://www.instagram.com/')

# Get instance of the username and password inputs
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# Clear those inputs and enter the account credentials
username.clear()
password.clear()
username.send_keys(instagram_username)
password.send_keys(instagram_password)

# Click login, after that click the not now text in notification modal
login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
not_now_two = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

time.sleep(1)

# Target the searchbox and input the keyword to be search
search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
search_box.clear()
keyword = "#cats"
search_box.send_keys(keyword)

time.sleep(4)

# Hit enter key in the search box
search_box.send_keys(Keys.ENTER)
# Apparently by hitting just one enter key, nothing happened, so again hit enter key in the search box
time.sleep(1)
search_box.send_keys(Keys.ENTER)

# Sleep to make sure search result is done rendering
time.sleep(4)

# Window scroll page to bottom
driver.execute_script("window.scrollTo(0,4000);")
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]

print(images)