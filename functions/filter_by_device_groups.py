from data import globals
from functions import menu

def SelectJuniperFirewalls():
    print(globals.SELECTED_DEVICES)
    menu.menu_configuration_options_init()

def SelectJuniperRouters():
    globals.SELECTED_DEVICES = globals.NORNIR_INIT.filter(group="JuniperRouters")


def SelectJuniperSwitches():
    globals.SELECTED_DEVICES = globals.NORNIR_INIT.filter(group="JuniperSwitches")
