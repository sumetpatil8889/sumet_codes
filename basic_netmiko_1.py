## This is just a basic template of how to log in to the device with ssh and get the show run config with netmiko
from netmiko import ConnectHandler   # to initiate connection we need this plugin

#list_ip = ["192.168.1.115", "192.168.1.116", "192.168.1.117", "192.168.1.118", "192.168.1.119"]
list_ip = ["192.168.1.125"]
for device_ip in list_ip:
    device123 = {
        "device_type": "arista_eos",
        "ip": device_ip,
        "username": "admin123",
        "password": "admin123",
        "port": 22
    }
    ssh123 = ConnectHandler(**device123)
    ssh123.send_command("enable", expect_string=r"#")
    out123 = ssh123.send_config_set(["show run", "logging host 5.5.5.5"])
    print(out123)
