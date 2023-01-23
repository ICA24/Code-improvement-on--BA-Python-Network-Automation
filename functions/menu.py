from collections import namedtuple
from data import constants as const

Option = namedtuple('Option', ['label', 'callback'])

class Menu:
    SEPARATOR = '-'
    def __init__(self, title, options):
        self._title = ''
        self._options = []
        self._title = title
        for option in options:
            self._options.append(Option(option[0], option[1]))
    def header(self, text):
        line = self.SEPARATOR * (len(text) + 2)
        return f"{line}\n {text}\n{line}\n"

    def display(self):
        string = self.header(self._title)

        for i, option in enumerate(self._options):
            string += f"{i + 1} {option.label}\n"
        print (string)

    def callback(self, i):
        if i <= len(self._options):
            return self._options[i - 1].callback

class Menu_Init(Menu):
        def __init__(self, MENU_NAME):
            print(MENU_NAME.display())
            option = int(input('-Choose option:'))
            MENU_NAME.callback(option)()


def main_menu_init():
    Menu_Init(const.MAIN_MENU)

def menu_device_selection_init():
    Menu_Init(const.MENU_DEVICE_SELECTION)

def menu_device_group_init():
    Menu_Init(const.MENU_DEVICE_GROUP_SELECTION)

def menu_configuration_options_init():
    Menu_Init(const.MENU_CONFIGURATION_OPTIONS)
