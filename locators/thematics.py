""" Добавление тематики """
add_btn = "//button[contains(@class, 'Button_Button')]"
save_btn = "(//button[contains(@class, 'Button_Button')])[4]"
cancel_btn = "(//button[contains(@class, 'Button_Button')])[5]"
them_title = "(//span[contains(@class, 'Title')])[1]"

""" Поле ввода "Название" """
name = '//input[@name="name"]'


""" Выпадающий список "Класс событий" """
event_class = "(//input[contains(@class, 'ThematicForm')])[2]"
dropdown = '//div[contains(@class, "mantine-Select-dropdown")]'
world = '(//div[contains(@class, "mantine-qxv4uk")])[1]'

""" Выпадающий список "Каналы для публикации" """
chanells = '(//div[contains(@class, "Channels")])[2]'
chan_1st = '(//div[contains(@class, "mantine-qxv4uk")])[1]'
chan_dropdown = '//div[contains(@class, "mantine-MultiSelect-dropdown mantine-rynikm")]'
chan_created = '(//div[contains(@class, "Chips_chip__bBo8l")])[1]'

""" Выпадающий список "Языки" """
languages = "//button[contains(@class, 'LanguageInput')]"
russian = '(//*[contains(@class, "LanguageInput_Popover__itemLabel")])[2]'
all_lang = '(//*[contains(@class, "LanguageInput_Popover__itemLabel")])[1]'
lang_value = '//div[@class="Chips_chip__bBo8l"]'
lang_dropdown = '//div[contains(@class, "Popover_Popover__b9PMk")]'
lang_selected = '(//div[contains(@class, "Chips_chip__bBo8l")])[2]'

""" Выпадающий список "География публикаций" """
country = '//input[@placeholder="Выбор страны"]'
region = "//input[@placeholder='Выбор региона']"
geogr_add_btn = "(//button[contains(@class, 'Button_Button')])[1]"


""" Поле ввода "Ключевые фразы и слова" """
key_ph = '//input[@name="keywords"]'
key_ph_add_btn = "//button[contains(span, 'Добавить')]"
key_ph_created = '(//span[contains(@class, "BodyNormal_BodyNormal__0hWD_")])[10]'

""" Кнопка переключения "Использовать ИИ" """
use_ai = '//button[contains(@class, "SwitchBox_Switch")]'


""" Поле ввода "Источники публикаций" """
sources = '(//div[contains(@class, "PublicationSourceInput")])[1]'
sources_add_btn = "(//button[contains(@class, 'Button_Button')])[3]"
sources_created = '(//span[contains(@class, "BodyNormal")])[12]'
sources_dropdown = '(//div[contains(@class, "PublicationSourceInput_P")])'
add_channel = '(//div[contains(@class, "PublicationSourceInput_Item")])[1]'
add_all = '(//div[contains(@class, "PublicationSourceInput_Item")])[2]'
add_channel_dropdown = '(//div[contains(@class, "Modal_Content")])'
add_chan_field = '//input[@name = "channel-link"]'
save_chan_btn = "(//button[contains(@class, 'Button_Button')])[6]"
chanel_added = '(//span[contains(@class, "BodyNormal_BodyNormal__0hWD_")])[13]'
checl_all_sourses = '(//span[contains(@class, "BodyNormal")])[11]'