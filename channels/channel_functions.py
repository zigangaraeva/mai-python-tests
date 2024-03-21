import time

import conftest
from common.waits import wait_present, wait_clickable, wait_text_present, wait_not_present
from locators import settings, channels
from selenium.webdriver.common.by import By


def go_to_channels(browser):
    wait_present(browser, 'XPATH', settings.settings, "Кнопка 'Настройки' отсутствует на странице ")
    wait_clickable(browser, 'XPATH', settings.settings, "Кнопка 'Настройки' не кликабельна")
    browser.find_element(By.XPATH, settings.settings).click()
    wait_present(browser, 'XPATH', settings.monit_settings, "Страница настроек не открылась")
    wait_clickable(browser, 'XPATH', channels.go_to_channels, "Кнопка перехода на страницу каналов не кликабельна")
    browser.find_element(By.XPATH, channels.go_to_channels).click()


def add_channel(browser, name, type=None, identificator=None):
    """ Функция добавления канала """
    wait_present(browser, 'XPATH', channels.add_channel,
                   "Кнопка перехода на форму для добавления каналов отсуствует")
    wait_clickable(browser, 'XPATH', channels.add_channel, "Кнопка перехода на форму для добавления каналов не кликабельна")
    browser.find_element(By.XPATH, channels.add_channel).click()
    wait_present(browser, 'XPATH', channels.add_chan_form, "Форма добавления канала отсутствует")

    """ Название канала """
    wait_present(browser, 'XPATH', channels.add_chan_name, "Поле ввода для названия отсутствует")
    browser.find_element(By.XPATH, channels.add_chan_name).send_keys(name)

    """ Тип канала """
    if type is not None:
        wait_present(browser, 'XPATH', channels.type_btn, "Поле выбора типа канала не кликабельна")
        browser.find_element(By.XPATH, channels.type_btn).click()
        wait_present(browser, 'XPATH', channels.type_form, "Форма для типа канала отсутствует")
        wait_present(browser, 'XPATH', channels.type_telegram, "Поле выбора отсутствует")
        browser.find_element(By.XPATH, channels.type_telegram).click()
        assert browser.find_element(By.XPATH, channels.type_btn).get_attribute(
            'value') == type  # проверка заполнения поля

    """ Идентификатор канала """
    if identificator is not None:
        wait_present(browser, 'XPATH', channels.identificator, "Поле ввода идентификатора отсутствует")
        browser.find_element(By.XPATH, channels.identificator).send_keys(identificator)

    """ Добавление канала """
    wait_present(browser, 'XPATH', channels.add_chan_form_btn, "Кнопка добавления канала в форме отсутствует")
    wait_clickable(browser, 'XPATH', channels.add_chan_form_btn, "Кнопка добавления канала в форме не кликабельна")
    wait_present(browser, 'XPATH', channels.cancel_btn, "Кнопка отмены добавления канала в форме отсутствует")
    browser.find_element(By.XPATH, channels.add_chan_form_btn).click()
    wait_not_present(browser, 'XPATH', channels.add_chan_form, "Форма добавления канала присутствует на странице")
    wait_present(browser, 'XPATH', channels.chan_is_present, "Канал не добавился на страницу")
    wait_text_present(browser, 'XPATH', channels.name_is_present, name, "Название отображается некорректно")
    wait_text_present(browser, 'XPATH', channels.id_is_present, identificator, "Идетификатор отображается некорректно")

def delete_channel(browser):
    """ Функция удаления канала """
    wait_present(browser, 'XPATH', channels.delete_channel, "Кнопка удаления канала отсутствует")
    wait_clickable(browser, 'XPATH', channels.delete_channel, "Кнопка удаления канала не кликабельна")
    browser.find_element(By.XPATH, channels.delete_channel).click()
    wait_present(browser, 'XPATH', channels.delete_form, "Форма удаления канала отсутствует")
    wait_present(browser, 'XPATH', channels.yes_button, "Кнопка 'Да' отсутствует")
    wait_present(browser, 'XPATH', channels.no_button, "Кнопка 'Отмена' отсутствует")
    wait_clickable(browser, 'XPATH', channels.yes_button, "Кнопка 'Да' не кликабельна")
    browser.find_element(By.XPATH, channels.yes_button).click()
    wait_not_present(browser, 'XPATH', channels.chan_is_present, "Канал присутствует на странице")


def edit_channel(browser, name, type=None, identificator=None):
    """ Редактирование канала """
    wait_present(browser, 'XPATH', channels.name_is_present, 'Название канала отсутствует')
    wait_clickable(browser, 'XPATH', channels.name_is_present, 'Название канала не кликабельно')
    browser.find_element(By.XPATH, channels.name_is_present).click()

    wait_present(browser, 'XPATH', channels.add_chan_name, 'Поле ввода названия отсутствует')
    browser.find_element(By.XPATH, channels.add_chan_name).clear()
    browser.find_element(By.XPATH, channels.add_chan_name).send_keys(name)

    wait_present(browser, 'XPATH', channels.type_btn, 'Поле выбора типа канала отсутствует')
    wait_clickable(browser, 'XPATH', channels.type_btn, 'Поле выбора типа канала не кликабельно')
    browser.find_element(By.XPATH, channels.type_btn).click()  # Клик на поле выбора типа канала

    wait_present(browser, 'XPATH', channels.type_form, 'Форма отображения типов каналов отсутствует')
    wait_present(browser, 'XPATH', channels.type_instagram, 'Тип канала "Инстаграм" отсутствует в форме')
    wait_clickable(browser, 'XPATH', channels.type_instagram, 'Тип канала "Инстаграм" не кликабельный')
    browser.find_element(By.XPATH, channels.type_instagram).click()
    assert browser.find_element(By.XPATH, channels.type_btn).get_attribute(
        'value') == type  # проверка заполнения поля

    wait_present(browser, 'XPATH', channels.identificator, 'Поле выбора идентификатора канала отсутствует')
    wait_clickable(browser, 'XPATH', channels.identificator, 'Поле выбора идентификатора канала не кликабельно')
    browser.find_element(By.XPATH, channels.identificator).clear()
    browser.find_element(By.XPATH, channels.identificator).send_keys(identificator)

    wait_present(browser, 'XPATH', channels.add_chan_form_btn, "Кнопка добавления канала в форме не кликабельна")
    wait_clickable(browser, 'XPATH', channels.add_chan_form_btn, "Кнопка добавления канала в форме не кликабельна")
    browser.find_element(By.XPATH, channels.add_chan_form_btn).click()

    wait_present(browser, 'XPATH', channels.chan_is_present, "Канал не добавился на страницу")