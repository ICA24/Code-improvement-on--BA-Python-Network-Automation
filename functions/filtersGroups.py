from nornir import InitNornir
from data.globals import SELECTED_DEVICES


def SelectJuniperFirewalls():
    nr = InitNornir(config_file="data/config.yml")
    SELECTED_DEVICESJFW = nr.filter(group="JuniperFirewalls")
    SELECTED_DEVICES = SELECTED_DEVICESJFW

def SelectJuniperRouters():
    nr = InitNornir(config_file="data/config.yml")
    SELECTED_DEVICESJR = nr.filter(group="JuniperRouters")
    SELECTED_DEVICES = SELECTED_DEVICESJR


def SelectJuniperSwitches():
    nr = InitNornir(config_file="data/config.yml")
    SELECTED_DEVICESJS = nr.filter(group="JuniperSwitches")
    SELECTED_DEVICES = SELECTED_DEVICESJS
