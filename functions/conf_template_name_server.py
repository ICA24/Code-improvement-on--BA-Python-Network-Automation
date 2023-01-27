from jinja2 import Environment, PackageLoader, select_autoescape
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from data.globals import SELECTED_DEVICES



def conf_template_name_server ():
    env = Environment(
        loader=PackageLoader("PythonNetworkAutomation"),
            autoescape=select_autoescape())
    template = env.get_template("nameServer.j2")
    ipaddr = input ("\nSpecify first Name Server IP:")
    ipaddr1 = input ("Specify second Name Server IP:")
    def retipaddr():
        value= template.render(ipaddr=ipaddr, ipaddr1=ipaddr1)
        return value
    var = retipaddr()
    for line in var.splitlines():
        results = SELECTED_DEVICES.run(task=netmiko_send_command, command_string=line, expect_string=r"#")
        print_result(results)
        if results=="commit complete":
            break




