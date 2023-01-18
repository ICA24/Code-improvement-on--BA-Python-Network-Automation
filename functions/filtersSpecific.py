from nornir import InitNornir
from data.globals import SELECTED_DEVICES
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from jinja2 import Environment, PackageLoader, select_autoescape
from nornir_utils.plugins.tasks.files import write_file
from datetime import date


def filterSpecificfunc():
    def printMenuConfiguration():
        print("\n1.CLI commands")
        print("2.Templates ")
        print("3.Backups")
        print("4.Exit")

    def selectMenuConfiguration():
        optionConfiguration = input("-Choose configuration option prior to selecting specific devices:")
        if optionConfiguration == "4":
            quit()
        elif optionConfiguration == "1":
            filterSpecificCLIcommands()
            printMenuConfiguration()
            selectMenuConfiguration()
        elif optionConfiguration == "2":
            PrintMenuConfigurationTemplates()
            SelectMenuConfigurationTemplates()
        elif optionConfiguration == "3":
            filterSpecificBackups ()
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
            templateNameServer()
            PrintMenuConfigurationTemplates()
            SelectMenuConfigurationTemplates()
        elif optionConfigurationTemplate == "2":
            templateOSPF()
            printMenuConfiguration()
            selectMenuConfiguration()

            # CLI COMMANDS #
    def filterSpecificCLIcommands():
        input_string = input("Enter devices names separated by space:")
        list  = input_string.split()
        print("Selected Devices:")
        for i in list:
            print(i)
        print("Define CLI command, each CLI command needs to be entered on a new line:\nPress CTRL+D to finish.\n")
        CLIInput = []
        while True:
            try:
                line = input()
            except EOFError:
                break
        CLIInput.append(line)
        for i in list:
            nr = InitNornir(config_file="data/config.yml")
            SELECTED_DEVICES = nr.filter(name=i)
            for cmd in CLIInput:
                results = SELECTED_DEVICES.run(task=netmiko_send_command, command_string=cmd)
                print_result(results)

            # Templates#
    def templateNameServer():
        templateNameServerFunct()
        printMenuConfiguration()
        selectMenuConfiguration()

    def templateOSPF():
        templateOSPFFunct()
        printMenuConfiguration()
        selectMenuConfiguration()

    def templateNameServerFunct ():
        nr = InitNornir(config_file="data/config.yml")
        env = Environment(loader=PackageLoader("PythonNetworkAutomation"),autoescape=select_autoescape())
        template = env.get_template("nameServer.j2")
        input_string = input("Enter devices names separated by space:")
        template = env.get_template("nameServer.j2")
        global list
        list  = input_string.split()
        print("Selected Devices:")
        for i in list:
            print(i)
        ipaddr = input ("Specify IP:")
        ipaddr1 = input ("Specify IP:")
        def retipaddr():
            value= template.render(ipaddr=ipaddr, ipaddr1=ipaddr1)
            return value
        var = retipaddr()

        for i in list:
            SELECTED_DEVICES = nr.filter(name=i)
            for i in list:
                for line in var.splitlines():
                    nr = InitNornir(config_file="data/config.yml")
                    results = SELECTED_DEVICES.run(task=netmiko_send_command, command_string=line, expect_string=r"#")
                    print_result(results)
                    if results=="commit complete":
                        break

    def templateOSPFFunct():
        nr = InitNornir(config_file="data/config.yml")
        input_string = input("Enter devices names separated by space:")
        env = Environment(loader=PackageLoader("PythonNetworkAutomation"),autoescape=select_autoescape())
        template = env.get_template("ospf.j2")
        area = input ("\nSpecify OSPF area:")
        int = input ("Specify interface name:")
        def retipaddr():
                value= template.render(area=area, int=int)
                return value
        var = retipaddr()
        global list
        list  = input_string.split()
        print("Selected Devices:")
        for i in list:
            print(i)

        for i in list:
            SELECTED_DEVICES = nr.filter(name=i)
            for i in list:
                for line in var.splitlines():
                    results = SELECTED_DEVICES.run(task=netmiko_send_command, command_string=line, expect_string=r"#")
                    print_result(results)
                    if results=="commit complete":
                        break

    def filterSpecificBackups ():
        nr = InitNornir(config_file="data/config.yml")
        input_string = input("Enter devices names separated by space:")
        global list
        list  = input_string.split()
        print("Selected Devices:")
        for i in list:
            print(i)

        for i in list:
            SELECTED_DEVICES = nr.filter(name=i)
            def backup_configurations(task):
                cmds = [ "show configuration | display set"]
                for cmd in cmds:
                    r = task.run(task=netmiko_send_command, command_string=cmd)
                task.run(task=write_file,content=r.result,filename=f"" + str(date.today()) + " " + task.host.name + ".txt")
            results = SELECTED_DEVICES.run(name="Creating Backup Archive", task=backup_configurations)
            print_result(results)



    printMenuConfiguration()
    selectMenuConfiguration()



