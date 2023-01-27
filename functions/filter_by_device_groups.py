from data import globals
from functions import menu

def SelectJuniperFirewalls():
    globals.SELECTED_DEVICES = globals.NORNIR_INIT.filter(group="JuniperRouters")
    menu.menu_configuration_options_init()

def SelectJuniperRouters():
    globals.SELECTED_DEVICES = globals.NORNIR_INIT.filter(group="JuniperRouters")
    menu.menu_configuration_options_init()

def SelectJuniperSwitches():
    globals.SELECTED_DEVICES = globals.NORNIR_INIT.filter(group="JuniperSwitches")
    menu.menu_configuration_options_init()