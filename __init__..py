from data import constants as const

# print(x.MENU_DEVICE_SELECTION.display())
print(const.MAIN_MENU.display())
while True:
    option = int(input('-Choose option:'))
    const.MAIN_MENU.callback(option)()



