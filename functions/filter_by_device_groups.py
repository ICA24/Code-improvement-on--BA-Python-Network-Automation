from data.globals import SELECTED_DEVICES, NORNIR_INIT
from functions import menu

def SelectJuniperFirewalls():
    SELECTED_DEVICES = NORNIR_INIT.filter(group="JuniperFirewalls")
    menu.menu_configuration_options_init()

def SelectJuniperRouters():
    SELECTED_DEVICES = NORNIR_INIT.filter(group="JuniperRouters")


def SelectJuniperSwitches():
    SELECTED_DEVICES = NORNIR_INIT.filter(group="JuniperSwitches")
