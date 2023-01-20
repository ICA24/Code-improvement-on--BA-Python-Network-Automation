from data import constants as const

while True:
    const.MAIN_MENU.display()
    option = int(input('-Choose option:'))
    const.MAIN_MENU.callback(option)()



