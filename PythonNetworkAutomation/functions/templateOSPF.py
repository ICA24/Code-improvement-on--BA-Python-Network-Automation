from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from jinja2 import Environment, PackageLoader, select_autoescape
from PythonNetworkAutomation import global_def

SelectedDevices = global_def.SelectedDevices

def TemplatingOSPF ():
    env = Environment(
        loader=PackageLoader("PythonNetworkAutomation"),
            autoescape=select_autoescape())
    template = env.get_template("ospf.j2")
    area = input ("\nSpecify OSPF area:")
    int = input ("Specify interface name:")
    def retipaddr():
        value= template.render(area=area, int=int)
        return value
    var = retipaddr()
    for line in var.splitlines():
        results = global_def.SelectedDevices.run(task=netmiko_send_command, command_string=line, expect_string=r"#")
        print_result(results)
        if results=="commit complete":
            break




