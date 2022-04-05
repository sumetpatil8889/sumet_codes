import json

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config, netmiko_commit, netmiko_send_command, netmiko_file_transfer, netmiko_save_config
from nornir_utils.plugins.tasks.files import write_file
from nornir_utils.plugins.functions import print_result

nr123 = InitNornir("configs11.yml")
# nr1234 = InitNornir("configs12.yml")
# nr12345 = InitNornir("configs13.yml")

version123 = (nr123.run(netmiko_send_command, command_string="show run"))
# version1234 = (nr1234.run(netmiko_send_command, command_string="show configuration | display set"))
# version12345 = (nr12345.run(netmiko_send_command, command_string="show run"))


# cisco_print123 = (nr123.run(netmiko_send_config, config_file=r"C:\Users\spsp1\Documents\python_folder_files\cisco123_cmd_list.txt"))
# print_result(cisco_print123)

cisco_config123 = open(r"C:\Users\spsp1\Documents\python_folder_files\cisco_ios_config.txt", "w")
#print_result(version123)

cisco_config123 = open(r"C:\Users\spsp1\Documents\python_folder_files\cisco_ios_config.txt", "a")
cisco_config123.write(str(version123))
#cisco_config123.write(str(cisco_config123))

# junos_config123 = open(r"C:\Users\spsp1\Documents\python_folder_files\junos_config.txt", "w")
# junos_print123 = (nr1234.run(netmiko_send_config, config_file=r"C:\Users\spsp1\Documents\python_folder_files\junos123_cmd_list.txt"))
# print_result(version1234)
# print_result(junos_print123)
# junos_config123 = open(r"C:\Users\spsp1\Documents\python_folder_files\junos_config.txt", "a")
# junos_config123.write(str(version1234))
#
# arista_config123 = open(r"C:\Users\spsp1\Documents\python_folder_files\arista_eos_ios_config.txt", "w")
# arista_print123 = (nr12345.run(netmiko_send_config, config_file=r"C:\Users\spsp1\Documents\python_folder_files\arista123_cmd_list.txt"))
# print_result(version12345)
# print_result(arista_print123)
# arista_config123 = open(r"C:\Users\spsp1\Documents\python_folder_files\arista_eos_ios_config.txt", "a")
# arista_config123.write(str(version12345))
# arista_config123.write(str(arista_print123))

