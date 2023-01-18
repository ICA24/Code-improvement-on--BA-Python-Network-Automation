from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from data.globals import SELECTED_DEVICES


def CLIcommands():
	print("Define CLI command, each CLI command needs to be entered on a new line:\nPress CTRL+D to finish.\n")
	CLIInput = []
	while True:
		try:
			line = input()
		except EOFError:
			break
		CLIInput.append(line)

	for cmd in CLIInput:
		nr = InitNornir(config_file="data/config.yml")
		results = SELECTED_DEVICES.run(task=netmiko_send_command, command_string=cmd)
		print_result(results)



