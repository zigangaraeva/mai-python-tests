from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


wait_time = 20


def wait_present(browser, selector_cat, selector, message):
    """Метод ожидания наличия элемента на странице"""
    if selector_cat == 'NAME':
        return WebDriverWait(browser, wait_time).until(expected_conditions.presence_of_element_located((
            By.NAME, selector)), message)
    if selector_cat == 'ID':
        return WebDriverWait(browser, wait_time).until(expected_conditions.presence_of_element_located((
            By.ID, selector)), message)
    if selector_cat == 'XPATH':
        return WebDriverWait(browser, wait_time).until(expected_conditions.presence_of_element_located((
            By.XPATH, selector)), message)
    if selector_cat == 'CSS':
        return WebDriverWait(browser, wait_time).until(expected_conditions.presence_of_element_located((
            By.CSS_SELECTOR, selector)), message)


def wait_not_present(browser, selector_cat, selector, message):
    """Метод ожидания отсутствия элемента на странице"""
    if selector_cat == 'NAME':
        return WebDriverWait(browser, wait_time).until_not(expected_conditions.presence_of_element_located((
            By.NAME, selector)), message)
    if selector_cat == 'ID':
        return WebDriverWait(browser, wait_time).until_not(expected_conditions.presence_of_element_located((
            By.ID, selector)), message)
    if selector_cat == 'XPATH':
        return WebDriverWait(browser, wait_time).until_not(expected_conditions.presence_of_element_located((
            By.XPATH, selector)), message)
    if selector_cat == 'CSS':
        return WebDriverWait(browser, wait_time).until_not(expected_conditions.presence_of_element_located((
            By.CSS_SELECTOR, selector)), message)

def wait_clickable(browser, selector_cat, selector, message):
    """Метод ожидания кликабельности элемента"""
    if selector_cat == 'NAME':
        return WebDriverWait(browser, wait_time).until(expected_conditions.element_to_be_clickable((
            By.NAME, selector)), message)
    if selector_cat == 'ID':
        return WebDriverWait(browser, wait_time).until(expected_conditions.element_to_be_clickable((
            By.ID, selector)), message)
    if selector_cat == 'XPATH':
        return WebDriverWait(browser, wait_time).until(expected_conditions.element_to_be_clickable((
            By.XPATH, selector)), message)
    if selector_cat == 'CSS':
        return WebDriverWait(browser, wait_time).until(expected_conditions.element_to_be_clickable((
            By.CSS_SELECTOR, selector)), message)


def wait_text_present(browser, selector_cat, selector, text, message):
    """Метод ожидания появления определенного текста"""
    if selector_cat == 'NAME':
        return WebDriverWait(browser, wait_time).until(expected_conditions.text_to_be_present_in_element((
            By.NAME, selector), text), message)
    if selector_cat == 'ID':
        return WebDriverWait(browser, wait_time).until(expected_conditions.text_to_be_present_in_element((
            By.ID, selector), text), message)
    if selector_cat == 'XPATH':
        return WebDriverWait(browser, wait_time).until(expected_conditions.text_to_be_present_in_element((
            By.XPATH, selector), text), message)
    if selector_cat == 'CSS':
        return WebDriverWait(browser, wait_time).until(expected_conditions.text_to_be_present_in_element((
            By.CSS_SELECTOR, selector), text), message)
