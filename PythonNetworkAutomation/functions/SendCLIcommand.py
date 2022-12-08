from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from PythonNetworkAutomation import global_def





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
		nr = InitNornir(config_file="appdata/config.yml")
		results = global_def.SelectedDevices.run(task=netmiko_send_command, command_string=cmd)
		print_result(results)



