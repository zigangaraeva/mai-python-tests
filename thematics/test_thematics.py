
from common.authorization import authorization
from thematics_functions import setup_theme_page, elements_present, add_thematics
from channels.channel_functions import add_channel, delete_channel
import conftest


def test_input_check(browser):
    """ Проверка заполнения всех полей """
    authorization(browser)
    add_channel(browser, conftest.name_ch1)
    setup_theme_page(browser)
    elements_present(browser)
    add_thematics(browser, conftest.name1, conftest.event_class1, conftest.channels1, conftest.key_phr1, conftest.ai_on1)
    delete_channel(browser)


def test_required_elems(browser):
    """ Проверка обязательных полей """
    authorization(browser)
    add_channel(browser, conftest.name_ch1, conftest.type_ch1, conftest.channels1)
    setup_theme_page(browser)
    elements_present(browser)
    add_thematics(browser, conftest.name1, conftest.event_class1)
    delete_channel(browser)


