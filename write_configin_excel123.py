# I want to create a script using netmiko which will log in and apply the configs to the device
# For that I need one Excel sheet first, and I will use the one I already have


#1. import right modules or libraries

from netmiko import ConnectHandler
import xlwt
from netmiko import ConnectHandler, redispatch
from getpass import getpass
import netmiko
from CLEAR_OSPF import CLEAR_OSPF
from write_config_from_excel import write_config_from_excel
import time
#

def write_configin_excel123(ssh123):
    ip123 = input("Enter the IP for the device to which you want to login to the device: ")
    username123 = input("Enter the username of the device to which you want to login to the device: ")
    print("Enter the password of the device to which you want to login to the device: ")
    password123 = getpass()
    # 4. now you take all this info and shove it into the session for the device from where you want to pull the info or update the config to
    ssh123.write_channel("ssh " + username123 + "@" + ip123 + "\n")
    time.sleep(1)
    ssh123.write_channel(password123 + "\n")
    redispatch(ssh123, device_type="cisco_ios")

    # list_ip = ["192.168.1.115", "192.168.1.116", "192.168.1.117"]
    #
    # for ip123 in list_ip:
    #     device123 = {
    #         "device_type": "cisco_ios",
    #         "username": "admin",
    #         "password": "cisco",
    #         "ip": ip123,
    #         "port": 22
    #     }

    # ssh123 = ConnectHandler(**device123)

    new_wb123 = xlwt.Workbook()
    sheetnm123 = new_wb123.add_sheet("Mumbai_Branch " + ip123)
    row = 0
    col = 0

    show_run123 = ssh123.send_command("show run")
    show_run123 = show_run123.splitlines()

    for xyz in show_run123:
        sheetnm123.write(row, col, xyz)
        row = row + 1
        new_wb123.save(r"C:\Users\spsp1\Documents\python_folder_files\new_script123" + ip123 + ".xls")

    print("SCRIPT IS DONE!!!")
    return 0
