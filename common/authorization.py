from selenium.webdriver.common.by import By
from common.waits import wait_present
import conftest
from locators import common
#from conftest import browser
from waits import wait_text_present, wait_clickable

def authorization(browser):
    """Авторизация"""
    browser.get(conftest.url)
    wait_present(browser, 'XPATH', common.xpath_for_login, "Отсутствует поле ввода для логина")
    browser.find_element(By.XPATH, common.xpath_for_login).send_keys(conftest.login)
    wait_present(browser, 'XPATH', common.xpath_for_password, "Отсутствует поле ввода для пароля")
    browser.find_element(By.XPATH, common.xpath_for_password).send_keys(conftest.password)
    wait_present(browser, 'XPATH', common.login_button, "Отсутствует кнопка 'Войти' ")
    wait_clickable(browser, 'XPATH', common.login_button, "Кнопка не кликабельна ")
    browser.find_element(By.XPATH, common.login_button).click()
    wait_text_present(browser, 'XPATH', common.text_daily_pic, 'Картина дня',
                      "Страница 'Картина дня' не открылась")

