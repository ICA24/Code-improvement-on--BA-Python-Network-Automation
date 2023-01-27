from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from jinja2 import Environment, PackageLoader, select_autoescape
from ba_python_improvement.data.globals import SELECTED_DEVICES as SELECTED_DEVICES


def conf_template_ospf ():
    env = Environment(
        loader=PackageLoader("ba_python_improvement"),
            autoescape=select_autoescape())
    template = env.get_template("ospf.j2")
    area = input ("\nSpecify OSPF area:")
    int = input ("Specify interface name:")
    def retipaddr():
        value= template.render(area=area, int=int)
        return value
    var = retipaddr()
    for line in var.splitlines():
        results = SELECTED_DEVICES.run(task=netmiko_send_command, command_string=line, expect_string=r"#")
        print_result(results)
        if results=="commit complete":
            break




