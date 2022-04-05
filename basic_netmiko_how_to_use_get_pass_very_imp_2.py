## This is just a basic template of how to login to the device with ssh and get the show run config with netmiko

from netmiko import ConnectHandler   # to initiate connection we need this plugin
from getpass import getpass

username123 = input("Enter the username: \n")
print("Please enter the password first for the script to run successfully\n")
password_123 = getpass()

#### THIS IS VERY IMPORTANT### PLEASE YOU NEED TO TURN ON THE EMULATOR FOR EACH
# PROGRAM SEPARATELY!!! YOU NEED TO GO IN RUN >> EDIT CONFIG>> TURN ON THE EMULATOR

list_ip = ["192.168.1.112", "192.168.1.113"]
for device_ip in list_ip:
    device123 = {
        "device_type": "cisco_ios",
        "ip": device_ip,
        "username": username123,
        "password": password_123,
        "port": 22
    }
    ssh123 = ConnectHandler(**device123)
    out123 = ssh123.send_command("show run")
    print(out123)
