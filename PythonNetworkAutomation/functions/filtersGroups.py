from nornir import InitNornir
from PythonNetworkAutomation import global_def


def SelectJuniperFirewalls():
    nr = InitNornir(config_file="appdata/config.yml")
    SelectedDevicesJFW = nr.filter(group="JuniperFirewalls")
    global_def.SelectedDevices = SelectedDevicesJFW

def SelectJuniperRouters():
    nr = InitNornir(config_file="appdata/config.yml")
    SelectedDevicesJR = nr.filter(group="JuniperRouters")
    global_def.SelectedDevices = SelectedDevicesJR


def SelectJuniperSwitches():
    nr = InitNornir(config_file="appdata/config.yml")
    SelectedDevicesJS = nr.filter(group="JuniperSwitches")
    global_def.SelectedDevices = SelectedDevicesJS
