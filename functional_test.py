import os
from selenium import webdriver

chromedriver = "G:\SoftAndIT\DRIVERS\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost:8000")

assert  'Django' in driver.title