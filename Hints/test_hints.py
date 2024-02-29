
import pytest
import time
from locators import hints, collections, report, settings
from common.waits import wait_present, wait_clickable
from common.authorization import authorization
from selenium.webdriver.common.by import By


def test_check_hint_present_daily_pic(browser):
    """ Проверка наличия элемента подсказки на странице "Картина дня" """
    authorization(browser)
    hint_daily_pic_element = browser.find_element(By.XPATH, hints.daypic)
    wait_present(browser, 'XPATH', hints.daypic, "Иконка подсказки отсутствует")
    wait_clickable(browser, 'XPATH', hints.daypic, "Иконка подсказки не кликабельна")
    hint_daily_pic_element.click()
    wait_present(browser, 'XPATH', hints.daypic_elem, "Окна подсказки нет на странице")
    wait_present(browser, 'XPATH', hints.daypic_btn_2page, "Кнопки для переключения между страницами подсказки нет на странице")
    wait_clickable(browser, 'XPATH', hints.daypic_btn_2page, "Кнопка для переключения между страницами подсказкине кликабельна")
    browser.find_element(By.XPATH, hints.daypic_btn_2page).click()
    wait_present(browser, 'XPATH', hints.daypic_elem_2page_1, "Первый элемент подсказки отсутствует на странице ")
    wait_present(browser, 'XPATH', hints.daypic_elem_2page_2, "Второй элемент подсказки отсутствует на странице ")
    wait_present(browser, 'XPATH', hints.daypic_elem_2page_3, "Третий элемент подсказки отсутствует на странице ")


@pytest.mark.skip("На странице нет окна подсказки")
def test_check_hint_present_collections(browser):
    """ Проверка наличия элемента подсказки на странице "Подборки" """
    authorization(browser)
    collections_button = wait_clickable(browser, 'XPATH', collections.collections, "Кнопка перехода на 'Подборки' не кликабельна ")
    collections_button.click()
    hint_collections_element = wait_clickable(browser, 'XPATH', hints.collections, "Кнопка подсказки на странице 'Подборки' не кликабельна ")
    hint_collections_element.click()


def test_check_hint_present_report(browser):
    """ Проверка наличия элемента подсказки на странице "Отчёт" """
    authorization(browser)
    wait_present(browser, 'XPATH', report.report, "Кнопка перехода на 'Отчёт' отсутствует ")
    wait_clickable(browser, 'XPATH', report.report, "Кнопка перехода на 'Отчёт' не кликабельна ")
    browser.find_element(By.XPATH, report.report).click()
    wait_present(browser, 'XPATH', hints.report, "Кнопка подсказки на странице 'Отчёт' отсутствует")
    wait_clickable(browser, 'XPATH', hints.report, "Кнопка подсказки на странице 'Отчёт' не кликабельна ")
    browser.find_element(By.XPATH, hints.report).click()
    time.sleep(5)
    wait_present(browser, 'XPATH', hints.report_elem, "Окна подсказки нет на странице")
    wait_present(browser, 'XPATH', hints.report_btn_3page, "Кнопка третьей страницы подсказки отсутствует на странице")
    wait_clickable(browser, 'XPATH', hints.report_btn_3page, "Кнопка третьей страницы подсказки не кликабельна")
    browser.find_element(By.XPATH, hints.report_btn_3page).click()
    time.sleep(5)
    wait_present(browser, 'XPATH', hints.report_elem_3page, "Элемент подсказки на 3 странице подсказки отсутствует")


def test_check_hint_present_settings(browser):
    """ Проверка наличия элемента подсказки на странице "Настройки" """
    authorization(browser)
    wait_present(browser, 'XPATH', settings.settings, "Кнопка перехода на 'Настройки' отсутствует ")
    wait_clickable(browser, 'XPATH', settings.settings, "Кнопка перехода на 'Настройки' не кликабельна ")
    browser.find_element(By.XPATH, settings.settings).click()
    wait_present(browser, 'XPATH', settings.monit_settings, "Страница настроек не открылась")
    wait_present(browser, 'XPATH', hints.settings, "Кнопка подсказки на странице 'Настройки' отсутствует " )
    wait_clickable(browser, 'XPATH', hints.settings, "Кнопка подсказки на странице 'Настройки' не кликабельна " )
    browser.find_element(By.XPATH, hints.settings).click()
    wait_present(browser, 'XPATH', hints.settings_elem1, "Окна первой подсказки нет на странице")
    wait_present(browser, 'XPATH', hints.settings_elem2, "Окна второй подсказки нет на странице")
    wait_present(browser, 'XPATH', hints.settings_elem3, "Окна третьей подсказки нет на странице")
    wait_present(browser, 'XPATH', hints.settings_elem4, "Окна четвертой подсказки нет на странице")


