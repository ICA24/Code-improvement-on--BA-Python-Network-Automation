from collections import namedtuple

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
        return string

    def callback(self, i):
        if i <= len(self._options):
            return self._options[i - 1].callback


class Menu_Device_Selection(Menu):
    def __init__(self, title, options):
        Menu.__init__(self, title, options)

