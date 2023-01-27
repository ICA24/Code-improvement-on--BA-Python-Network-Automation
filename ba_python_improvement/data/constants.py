from ba_python_improvement.functions import backupFunct, compareConfig, filter_by_device_groups, conf_template_ospf, conf_template_name_server, filtersSpecific, conf_cli_commands, menu, generic

MENU_TEMPLATE_CONFIGURATION_OPTIONS = menu.Menu(
	"Device Group selection Menu - Please Select an Option", [
	('Name server template', conf_template_name_server.conf_template_name_server),
	('OSPF template', conf_template_ospf.conf_template_ospf),
	('Back', menu.menu_configuration_options_init)])


MENU_CONFIGURATION_OPTIONS = menu.Menu(
	"Device Group selection Menu - Please Select an Option", [
	('CLI commands', conf_cli_commands.send_cli_command),
	('Templates', menu.menu_configuration_template_options_init),
	('Juniper Switches', filter_by_device_groups.SelectJuniperSwitches),
	('Back', menu.menu_device_selection_init)])

MENU_DEVICE_GROUP_SELECTION = menu.Menu(
	"Device Group selection Menu - Please Select an Option", [
	('Juniper Firewalls', filter_by_device_groups.SelectJuniperFirewalls),
	('Juniper Routers', filter_by_device_groups.SelectJuniperRouters),
	('Juniper Switches', filter_by_device_groups.SelectJuniperSwitches),
	('Back', menu.menu_device_selection_init)])


MENU_DEVICE_SELECTION = menu.Menu(
	"Device selection Menu - Please Select an Option", [
	('Show device list', generic.list_hosts),
	('Select device group', menu.menu_device_group_init),
	('Select specific devices', filtersSpecific),
	('Back', menu.main_menu_init)])

MAIN_MENU = menu.Menu(
	"Main Menu - Please Select an Option", [
	('Edit hosts file', generic.EditHostsFile),
	('Select hosts', menu.menu_device_selection_init),
	('Configure all devices', menu.menu_configuration_options_init),
	('Exit', generic.exit)])





