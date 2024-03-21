from locators import settings, thematics
from common.waits import wait_present, wait_clickable, wait_text_present, wait_not_present
from common.authorization import authorization
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def setup_theme_page(browser):
    wait_present(browser, 'XPATH', settings.settings, "Кнопка 'Настройки' отсутствует на странице ")
    wait_clickable(browser, 'XPATH', settings.settings, "Кнопка 'Настройки' не кликабельна")
    browser.find_element(By.XPATH, settings.settings).click()
    wait_present(browser, 'XPATH', settings.monit_settings, "Страница настроек не открылась")
    wait_present(browser, 'XPATH', thematics.add_btn, "Кнопка 'Добавить тематику' отсутствует на странице ")
    wait_clickable(browser, 'XPATH', thematics.add_btn, "Кнопка 'Добавить тематику' не кликабельна")
    browser.find_element(By.XPATH, thematics.add_btn).click()
    wait_present(browser, 'XPATH', thematics.them_title, "Страница настройки тематики не открылась")


def elements_present(browser):
    """ Проверка формы добавления тематики на наличие элементов"""
    wait_present(browser, 'XPATH', thematics.name, 'Поля "Название" нет на странице')
    wait_present(browser, 'XPATH', thematics.event_class, 'Поля "Класс событий" нет на странице')
    wait_present(browser, 'XPATH', thematics.chanells, 'Поля "Каналы для публикации" нет на странице')
    wait_present(browser, 'XPATH', thematics.languages, "Поле для выбора языков отсутствует")
    wait_present(browser, 'XPATH', thematics.country, "Поле для выбора страны отсутствует")
    wait_present(browser, 'XPATH', thematics.region, "Поле для выбора региона отсутствует")
    wait_present(browser, 'XPATH', thematics.geogr_add_btn,
                 "Кнопка'Добавить' для добавления страны и региона отсутствует")
    wait_present(browser, 'XPATH', thematics.key_ph, "Поле ввода ключевых фраз отсутствует")
    wait_present(browser, 'XPATH', thematics.key_ph, "Кнопка 'Добавить' для добавления ключевых фраз отсутствует")
    wait_present(browser, 'XPATH', thematics.use_ai, "Кнопка переключения 'Использовать ИИ' отсутствует")
    wait_present(browser, 'XPATH', thematics.sources, "Поле ввода источников отсутствует")
    wait_present(browser, 'XPATH', thematics.sources_add_btn, "Кнопка 'Добавить' для добавления источников отсутствует")
    wait_present(browser, 'XPATH', thematics.save_btn, "Кнопка 'Сохранить' для сохранения тематики отсутствует")
    wait_present(browser, 'XPATH', thematics.cancel_btn, "Кнопка 'Отменить' для отмены тематики отсутствует")


def add_thematics(browser, name, event_class, channels=None, key_phr=None, ai_on=None):
    """ Проверка добавления тематики """

    """ Название """
    browser.find_element(By.XPATH, thematics.name).send_keys(name)

    """ Класс событий """
    wait_clickable(browser, 'XPATH', thematics.event_class, 'Поле "Класс событий" не кликабельно')
    browser.find_element(By.XPATH, thematics.event_class).click()
    wait_present(browser, 'XPATH', thematics.dropdown, 'Элемент раскрывающегося списка не появился')
    wait_present(browser, 'XPATH', thematics.world, 'Опция "В мире" осутствует на странице')
    wait_clickable(browser, 'XPATH', thematics.world, 'Опция "В мире" не кликабельна')
    browser.find_element(By.XPATH, thematics.world).click()
    assert browser.find_element(By.XPATH, thematics.event_class).get_attribute(
        'value') == event_class  # проверка заполнения поля

    if channels is not None:
        """ Каналы для публикации """
        wait_clickable(browser, 'XPATH', thematics.chanells, 'Поле "Каналы для пабликаций" не кликабельно')
        browser.find_element(By.XPATH, thematics.chanells).click()
        wait_present(browser, 'XPATH', thematics.chan_dropdown, 'Элемент раскрывающегося списка не появился')
        wait_present(browser, 'XPATH', thematics.chan_1st, 'Элемент канала отсутствует на странице')
        browser.find_element(By.XPATH, thematics.chan_1st).click()
        wait_present(browser, 'XPATH', thematics.chan_created, 'Созданный элемент канала не появился под полем')
        wait_text_present(browser, 'XPATH', thematics.chan_created, channels,
                          'Текст отсутствует в поле отображения добавленного канала')

        """ Языки """
        wait_clickable(browser, 'XPATH', thematics.languages, 'Поле "Языки" не кликабельно')
        browser.find_element(By.XPATH, thematics.languages).click()
        wait_present(browser, 'XPATH', thematics.lang_dropdown, 'Элемент раскрывающегося списка не появился')
        wait_present(browser, 'XPATH', thematics.russian, 'Опция выбора русского языка отсутствует')
        wait_clickable(browser, 'XPATH', thematics.russian, 'Опция выбора русского языка отсутствует')
        wait_clickable(browser, 'XPATH', thematics.all_lang, 'Опция выбора всех языков отсутствует')
        browser.find_element(By.XPATH, thematics.all_lang).click()  # чтобы отключить все языки
        browser.find_element(By.XPATH, thematics.russian).click()
        # тут надо написать куда тыкнуть чтобы поле языков убралось
        # browser.find_element(By.XPATH, thematics.name).click()
        ActionChains(browser).move_by_offset(500, 300).click().perform()  # 500 по горизонтали и 300 по вертикали
        wait_not_present(browser, 'XPATH', thematics.lang_dropdown, 'Выпадающий список не исчез')
        wait_present(browser, 'XPATH', thematics.lang_selected, 'Выбранный элемент языка не появился под полем')
        wait_text_present(browser, 'XPATH', thematics.lang_selected, 'Русский', 'Текст не появился в элементе')

    """ Функционал еще не работает """
    #""" География публикаций """
    #wait_clickable(browser, 'XPATH', thematics.country, 'Поле выбора страны отсутствует')
    #wait_clickable(browser, 'XPATH', thematics.region, 'Поле выбора региона отсутствует')

    if ai_on is not None:
        """ Использовать ИИ """
        wait_clickable(browser, 'XPATH', thematics.use_ai, 'Кнопка переключения использования ИИ не кликабельна')
        browser.find_element(By.XPATH, thematics.use_ai).click()
        assert browser.find_element(By.XPATH, thematics.use_ai).get_attribute('value') == ai_on

    if key_phr is not None:
        """ Ключевые фразы и слова """
        browser.find_element(By.XPATH, thematics.key_ph).send_keys(key_phr)
        wait_clickable(browser, 'XPATH', thematics.key_ph_add_btn, 'Кнопка добавления ключевых фраз не кликабельна')
        browser.find_element(By.XPATH, thematics.key_ph_add_btn).click()
        wait_present(browser, 'XPATH', thematics.key_ph_created, 'Созданный элемент ключевых фраз не появился под полем')
        wait_text_present(browser, 'XPATH', thematics.key_ph_created, key_phr, 'Текст не появился в элементе')

    """ Источики публикаций 
     Ввод источников через поле 
    browser.find_element(By.XPATH, thematics.sources).send_keys("Футбол")
    wait_clickable(browser, 'XPATH', thematics.sources_add_btn, 'Кнопка добавления источников не кликабельна')
    browser.find_element(By.XPATH, thematics.sources_add_btn).click()
    wait_present(browser, 'XPATH', thematics.sources_created, 'Созданный элемент источников не появился под полем')
    wait_text_present(browser, 'XPATH', thematics.sources_created, 'Футбол', 'Текст не появился в элементе')
     Ввод источников через добавление канала 
    wait_clickable(browser, 'XPATH', thematics.sources, 'Поле добавления источников кликабельно')
    browser.find_element(By.XPATH, thematics.sources).click()
    wait_present(browser, 'XPATH', thematics.sources_dropdown, 'Выпадающий список источников отсутствует')
    wait_present(browser, 'XPATH', thematics.add_channel, 'Опция добавления каналов в источниках отсутствует')
    wait_clickable(browser, 'XPATH', thematics.add_channel, 'Опция добавления каналов в источниках не кликабельна')
    browser.find_element(By.XPATH, thematics.add_channel).click()
    wait_present(browser, 'XPATH', thematics.add_channel_dropdown, 'Окно для добавления канала отсутствует')
    wait_present(browser, 'XPATH', thematics.add_chan_field, 'Поле для добавления канала отсутствует')
    browser.find_element(By.XPATH, thematics.add_chan_field).send_keys("https://t.me/mhlrus")
    wait_present(browser, 'XPATH', thematics.save_chan_btn, 'Кнопка для сохранения канала отсутствует')
    wait_clickable(browser, 'XPATH', thematics.save_chan_btn, 'Кнопка для сохранения канала не кликабельна')
    browser.find_element(By.XPATH, thematics.save_chan_btn).click()
    wait_present(browser, 'XPATH', thematics.chanel_added, 'Созданный элемент канала не появился под полем')
    wait_text_present(browser, 'XPATH', thematics.chanel_added, 'https://t.me/mhlrus', 'Текст не появился в элементе')

    Ввод всех иточников 
    wait_present(browser, 'XPATH', thematics.add_all, 'Опция добавления всех источников отсутствует')
    wait_clickable(browser, 'XPATH', thematics.add_all, 'Опция добавления всех источников не кликабельна')
    browser.find_element(By.XPATH, thematics.add_all).click()
    wait_text_present(browser, 'XPATH', thematics.checl_all_sourses, 'Все', 'Текст не появился в элементе') """

    """ Сохранить """
    wait_clickable(browser, 'XPATH', thematics.save_btn, 'Кнопка сохранения тематики не кликабельна')
    browser.find_element(By.XPATH, thematics.save_btn).click()
