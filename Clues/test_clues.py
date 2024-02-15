from locators import clues
from common.waits import wait_present
from common.authorization import authorization


def test_check_clue_present(browser):
    """Проверка наличия элемента подсказки"""
    authorization(browser)
    wait_present(browser, 'XPATH', clues.xpath_hint_daily_pic, "Элемент подсказки не найден на странице 'Картина дня'")

