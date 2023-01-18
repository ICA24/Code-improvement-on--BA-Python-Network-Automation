from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from data.globals import SELECTED_DEVICES


def ShowRollback():
    nr = InitNornir(config_file="data/config.yml")
    exitCfgMode = SELECTED_DEVICES.run(task=netmiko_send_command, command_string="exit", expect_string=r">")
    print_result(exitCfgMode)
    results = SELECTED_DEVICES.run(task=netmiko_send_command, command_string="show system rollback compare 0 1", expect_string=r">")
    print("Configuration changes:")
    print_result(results)
