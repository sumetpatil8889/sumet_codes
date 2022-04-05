from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config, netmiko_commit, netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli, napalm_ping, napalm_configure, napalm_validate
from getpass import getpass

nr123 = InitNornir("configs1.yml")
# password123 = getpass()
# nr123.inventory.defaults.password = password123


# napalmfacts123 = nr123.run(napalm_get, getters=["get_facts"])
# napalmarp123 = nr123.run(napalm_get, getters=["get_arp_table"])
# napalmcli123 = nr123.run(napalm_cli, commands=["show run"])
# print_result(napalmcli123)


# netmikoip123 = nr123.run(netmiko_send_command, command_string="show run")
# print_result(netmikoip123)
# result123 = nr123.run(netmiko_send_command, command_string="show ip int br")
# print_result(result123)

# cfgs123 = input("Enter the config lines with ,: ")
# newcfgs = cfgs123.split(",")
# netmikoip123 = nr123.run(netmiko_send_config, config_commands=newcfgs)
# print_result(netmikoip123)

netmikoip123 = nr123.run(netmiko_send_config, config_file=r"C:\Users\spsp1\Documents\python_folder_files\cmd_list.txt")
print_result(netmikoip123)



