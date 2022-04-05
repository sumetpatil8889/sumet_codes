from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config, netmiko_commit, netmiko_send_command, netmiko_file_transfer, netmiko_save_config
import time
from nornir_utils.plugins.functions import print_result


start = time.time()
print(f'"start time: "{start}')

nr123 = InitNornir("configs11.yml")
nr1234 = InitNornir("configs12.yml")
nr12345 = InitNornir("configs13.yml")

# cisco_output123 = nr123.run(netmiko_file_transfer, source_file="R123.txt", dest_file="copied_file11.txt")
# juniper_output123 = nr1234.run(netmiko_file_transfer, source_file="R456.txt", dest_file="juniper123_file11.txt")
# arista_output123 = nr12345.run(netmiko_file_transfer, source_file="R789.txt", dest_file="arista_file11.txt")


cisco_output123 = nr123.run(netmiko_send_config, config_file=r"C:\Users\spsp1\Documents\python_folder_files\cisco123_cmd_list.txt")
juniper_output123 = nr1234.run(netmiko_send_config, config_file=r"C:\Users\spsp1\Documents\python_folder_files\junos123_cmd_list.txt")
arista_output123 = nr12345.run(netmiko_send_config, config_file=r"C:\Users\spsp1\Documents\python_folder_files\arista123_cmd_list.txt")

print_result(arista_output123)
print_result(cisco_output123)
print_result(juniper_output123)

end = time.time()
print(f'"end time: "{end}')
print(f'"end - start: " {(end - start)}')









######################################
# aaa authorization exec default local
# ssh123.send_command("enable", expect_string=r"#")
##


########################################
# from nornir_utils.plugins.functions import print_result
# from nornir_napalm.plugins.tasks import napalm_get, napalm_cli, napalm_ping, napalm_configure, napalm_validate


### Same program with just netmiko and file transfer modules
# from netmiko import ConnectHandler, file_transfer

# device123 = {
#             "device_type": "arista_eos",
#             "ip": "192.168.1.125",
#             "port": 22,
#             "username": "admin123",
#             "password": "admin123"
# }
# ssh123 = ConnectHandler(**device123)
# ssh123.send_command("enable", expect_string=r"#")
#arista_output123 = file_transfer(ssh123, source_file="R789.txt", dest_file="arista_file11.txt", disable_md5="True", overwrite_file=True)

# device12 = {
#             "device_type": "juniper_junos",
#             "ip": "192.168.1.133",
#             "port": 22,
#             "username": "admin123",
#             "password": "admin123"
# }
# ssh12 = ConnectHandler(**device12)
#juniper_output123 = file_transfer(ssh12, source_file="R456.txt", dest_file="juniper123_file11.txt", file_system="/var/tmp/", disable_md5="True", overwrite_file=True)

# netmiko123 = nr123.run(netmiko_file_transfer, source_file="R0.txt", dest_file="copied_file12345.txt")
# netmiko123 = nr123.run(netmiko_send_command, command_string="show version")
# print_result(netmiko123)

# device1 = {
#             "device_type": "cisco_ios",
#             "ip": "192.168.1.128",
#             "port": 22,
#             "username": "admin123",
#             "password": "admin123"
# }
# ssh1 = ConnectHandler(**device1)
# cisco_output123 = file_transfer(ssh1, source_file="R123.txt", dest_file="copied_file11.txt", file_system="flash0:/", disable_md5="True", overwrite_file=True)