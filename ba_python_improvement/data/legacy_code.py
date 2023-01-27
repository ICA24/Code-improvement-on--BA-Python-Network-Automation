from ba_python_improvement.functions import backupFunct, compareConfig, filter_by_device_groups, conf_template_ospf, \
    conf_template_name_server, filtersSpecific
from ba_python_improvement.functions.conf_cli_commands import CLIcommands
import subprocess


def printMenuDevices():
	print("\n1. Edit hosts file")
	print("2. Select hosts")
	print ("3. Configure all devices")
	print("4. Exit")

def selectMenuDevices ():
	option = input ("-Choose option:")
	if option == "1":
		EditHostsFile()
	elif option == "2":
		selectMenuDevicesSelect()
	elif option == "3":
		printMenuConfiguration()
		selectMenuConfiguration()
	elif option == "4":
		quit()
	else:
		print("\nInvalid option. \n")

def printMenuDevicesSelect():
	print("\n1. Show device list")
	print("2. Select device group")
	print("3. Select specific devices")
	print("4. Back")

def selectMenuDevicesSelect():
	printMenuDevicesSelect()
	optionSelect = input("-Choose option:")
	if optionSelect == "4":
		printMenuDevices()
		selectMenuDevices()
	elif optionSelect == "1":
		openHostsYAML()
	elif optionSelect == "2":
		printMenuDevicesSelectGroups()
		selectMenuDevicesSelectGroups()
	elif optionSelect == "3":
		filtersSpecific.filterSpecificfunc()
		selectMenuDevicesSelect()
	else:
		print("\nInvalid option. \n")

def printMenuDevicesSelectGroups():
	print("\n1.Juniper Firewalls")
	print("2.Juniper Routers")
	print("3.Juniper Switches")
	print("4. Back")

def selectMenuDevicesSelectGroups():
	optionSelectGroups = input("-Choose option:")
	if optionSelectGroups == "4":
		printMenuDevicesSelect()
		selectMenuDevicesSelect ()
	elif optionSelectGroups == "1":
		filtersGroups.SelectJuniperFirewalls()
		print("\nJuniper Firewalls group chosen. Please select configuration option:")
		printMenuConfiguration()
		selectMenuConfiguration()
	elif optionSelectGroups == "2":
		filtersGroups.SelectJuniperRouters()
		print("\nJuniper Routers group chosen. Please select configuration option:")
		printMenuConfiguration()
		selectMenuConfiguration()
	elif optionSelectGroups == "3":
		filtersGroups.SelectJuniperSwitches()
		print("\nJuniper Switches group chosen. Please select configuration option:")
		printMenuConfiguration()
		selectMenuConfiguration()
	else:
		print("\nInvalid option. \n")

def printMenuConfiguration():
	print("1.CLI commands")
	print("2.Templates ")
	print("3.Backups")
	print("4.Back")

def selectMenuConfiguration():
	optionConfiguration = input("-Choose option:")
	if optionConfiguration == "4":
		printMenuDevices()
		selectMenuDevices()
	elif optionConfiguration == "1":
		CLIcommands()
		printMenuConfiguration()
		selectMenuConfiguration()
	elif optionConfiguration == "2":
		PrintMenuConfigurationTemplates()
		SelectMenuConfigurationTemplates()
	elif optionConfiguration == "3":
		backupFunct.Backups()
		printMenuConfiguration()
		selectMenuConfiguration()
	else:
		print("\nInvalid option. \n")
def PrintMenuConfigurationTemplates():
	print("\n1. Name server template")
	print("2. OSPF template")
	print("3. Back")

def SelectMenuConfigurationTemplates():
	optionConfigurationTemplate = input("-Choose option:")
	if optionConfigurationTemplate == "3":
		printMenuConfiguration()
		selectMenuConfiguration()
	elif optionConfigurationTemplate == "1":
		templateNameServer.TemplatingNameServer()
		PrintMenuConfigurationTemplates()
		SelectMenuConfigurationTemplates()
	elif optionConfigurationTemplate == "2":
		templateOSPF.TemplatingOSPF()
		printMenuConfiguration()
		selectMenuConfiguration()

def EditHostsFile():
	print("\nConfigure hosts inventory YAML file with care to avoid potential issues.\nPlease see documentation for guidance: https://nornir.readthedocs.io/en/3.0.0/tutorial/inventory.html")
	subprocess.call([r"C:\Program Files\Notepad++\notepad++.exe", r"D:\v1.1\mypackage\data\hosts.yml"])

def openHostsYAML():
	hostsYAML = open("data/hosts.yml")
	print(hostsYAML.read())
	selectMenuDevicesSelect()

def TemplateConfig():
	templateNameServer.TemplatingNameServer()
	compareConfig.ShowRollback()
	printMenuConfiguration()
	selectMenuConfiguration()

while True:
	printMenuDevices()
	selectMenuDevices ()
