from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from datetime import date
from PythonNetworkAutomation import global_def


def Backups():
	nr = InitNornir(config_file="appdata/config.yml")
	def backup_configurations(task):
		cmds = ["show configuration | display set"]
		for cmd in cmds:
			r = task.run(task=netmiko_send_command, command_string=cmd)
		task.run(task=write_file,content=r.result,filename=f"" + str(date.today()) + " " + task.host.name + ".txt")
	results = global_def.SelectedDevices.run(name="Creating Backup File", task=backup_configurations)
	print_result(results)
