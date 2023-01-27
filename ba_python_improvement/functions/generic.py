from ba_python_improvement.functions import menu
import subprocess

def EditHostsFile():
	print("\nConfigure hosts inventory YAML file with care to avoid potential issues.\nPlease see documentation for guidance: https://nornir.readthedocs.io/en/3.0.0/tutorial/inventory.html")
	subprocess.call([r"C:\Program Files\Notepad++\notepad++.exe", r"D:\Network Automation\BA Python Improvement\data\hosts.yml"])

def exit():
	quit()

def list_hosts():
	hostsYAML = open("data/hosts.yml")
	print(hostsYAML.read())
	menu.menu_device_selection_init()
