## So I am going to write the script to log in to the cisco devices via linux console server

#1. so the first thing as always need to import the appropriate libraries
import time

from netmiko import ConnectHandler, redispatch
from getpass import getpass
import netmiko
from CLEAR_OSPF import CLEAR_OSPF
from write_config_from_excel import write_config_from_excel
from write_configin_excel123 import write_configin_excel123

#2. Now log in to the console server

device123 = {
    "device_type": "terminal_server",
    "ip": "192.168.1.127",
    "username": "linux",
    "password": "123",
    "port": 22

}
ssh123 = ConnectHandler(**device123)
print("###########THIS IS MY UBUNTU SERVER!!! ONLY AUTHORIZED USERS ARE ALLOWED TO LOG IN TO THE DEVICE###############")

# new_ospf123 = CLEAR_OSPF(ssh123)
# print(new_ospf123)

# new_config_from_excel123 = write_config_from_excel(ssh123)

new_write_config_in_excel123 = write_configin_excel123(ssh123)