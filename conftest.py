import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("URL")
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

""" Данные для формы добавления тематики """
name1 = 'Футбол'
event_class1 = 'В мире'
channels1 = 'https://t.me/rflive'
channels2 = ' ' #Одиночный пробел
channels3 = 'Eh bien, mon prince. Gênes et Lucques ne sont plus que des!' #Ввод текста вместо ссылки
channels4 = 'https://www.instagram.com/footballru_news?igsh=MW05Z3FwMnBucnZzdw=='
channels5 = 'https://vk.com/footballru'

key_phr1 = 'Чемпион'
ai_on1 = 'on'

""" Данные для формы добавления канала """
name_ch1 = 'Футбол'
name_ch2 = 'Бейсбол'
name_ch3 = '~`!@#$%^&*()_+?:"{}[];’' # Специальные символы
name_ch4 = '1234567890' # Цифры
name_ch5 = ' ' # Одиночный пробел
name_ch6 = '我朋友坐飞机回国' # Буквы других алфавитов
type_ch1 = 'Telegram'
type_ch2 = 'Instagram'
type_ch3 = 'ВКонтакте'



@pytest.fixture
def browser():
    service = Service('C:/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()





