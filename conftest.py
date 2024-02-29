import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("URL")
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
@pytest.fixture
def browser():
    service = Service('C:/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()





