import time
import pytest
import conftest
from common.authorization import authorization
from channel_functions import add_channel, delete_channel, go_to_channels, edit_channel
from common.waits import wait_present, wait_clickable, wait_text_present, wait_not_present
from locators import settings, channels
from selenium.webdriver.common.by import By

@pytest.mark.skip(reason="Заполение только обязательных полей не даёт добавить канал")
def test_required_items(browser):
    """ Проверка заполнения обязательных полей """
    authorization(browser)
    go_to_channels(browser)
    add_channel(browser, conftest.name_ch1)
    delete_channel(browser)


def test_all_items(browser):
    """ Проверка заполнения всех полей """
    authorization(browser)
    go_to_channels(browser)
    add_channel(browser, conftest.name_ch1, conftest.type_ch1, conftest.channels1)
    delete_channel(browser)


def test_edit_channels(browser):
    authorization(browser)
    go_to_channels(browser)
    add_channel(browser, conftest.name_ch1, conftest.type_ch1, conftest.channels1)
    edit_channel(browser, conftest.name_ch2, conftest.type_ch2, conftest.channels4)
    delete_channel(browser)
