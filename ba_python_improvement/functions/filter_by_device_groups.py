from ba_python_improvement.data import globals
from ba_python_improvement.functions import menu


def SelectJuniperFirewalls():
    globals.SELECTED_DEVICES = globals.NORNIR_INIT.filter(group="JuniperRouters")
    menu.menu_configuration_options_init()

def SelectJuniperRouters():
    globals.SELECTED_DEVICES = globals.NORNIR_INIT.filter(group="JuniperRouters")
    print("at selection")
    print(globals.SELECTED_DEVICES)
    menu.menu_configuration_options_init()

def SelectJuniperSwitches():
    globals.SELECTED_DEVICES = globals.NORNIR_INIT.filter(group="JuniperSwitches")
    menu.menu_configuration_options_init()