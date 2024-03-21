""" Кнопка перехода на страницу отображения имеющихся каналов """
go_to_channels = "//span[contains(@class, 'Body') and contains(text(), 'Каналы')]"

""" Кнопка перехода на форму для добавления каналов """
add_channel = "//button[contains(text(), 'Добавить канал')]"

""" Форма для добавления канала """
cancel_btn = "(//button[contains(@type, 'button')])[2]"
add_chan_form = "(//div[contains(@class, 'Modal_Content__S')])"
add_chan_name = '//input[@name="name"]'
add_chan_form_btn = "(//button[contains(@class, 'Button')])[2]"
identificator = '//input[@name="address"]'
type_btn = "//input[contains(@class, 'Select')]"
type_telegram = "(//div[contains(@class, 'mantine-q')])[1]"
type_instagram = "(//div[contains(@class, 'mantine-q')])[2]"
type_vkontakte = "(//div[contains(@class, 'mantine-q')])[3]"
type_form = "//div[contains(@class, 'mantine-InputW')]"

""" Отображение добавленного канала """
chan_is_present = "(//div[contains(@class, 'ChannelsTable_Column_1') ])[2]"
name_is_present = "//div[contains(@class, 'NameTelegram')]/span"
id_is_present = "(//span[contains(@class, 'BodySmall')])[6]"

""" Удаление канала """
yes_button = "(//button[contains(@class, 'Button_Button__XAILa Button_Button__b') ])[2]"
no_button = "//button[contains(text(), 'Отмена')]"
delete_channel = "//div[contains(@class, 'ChannelsTable_Tr') ]"
delete_form = "(//div[contains(@class, 'Modal_Content__S')])"