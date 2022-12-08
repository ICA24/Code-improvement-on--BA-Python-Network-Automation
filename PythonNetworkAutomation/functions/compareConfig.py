from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from PythonNetworkAutomation import global_def

def ShowRollback():
    nr = InitNornir(config_file="appdata/config.yml")
    exitCfgMode = global_def.SelectedDevices.run(task=netmiko_send_command, command_string="exit" , expect_string=r">")
    print_result(exitCfgMode)
    results = global_def.SelectedDevices.run(task=netmiko_send_command, command_string="show system rollback compare 0 1", expect_string=r">")
    print("Configuration changes:")
    print_result(results)
