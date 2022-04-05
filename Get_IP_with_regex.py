from netmiko import ConnectHandler   # to initiate connection we need this plugin
import re
list_ip = ["192.168.1.116", "192.168.1.117", "192.168.1.115", "192.168.1.118", "192.168.1.119"]
for device_ip in list_ip:
    device123 = {
        "device_type": "cisco_ios",
        "ip": device_ip,
        "username": "admin",
        "password": "cisco",
        "port": 22
    }
    ssh123 = ConnectHandler(**device123)
    outname123 = ssh123.find_prompt()
    outname123 = outname123.strip("#")
    out123 = ssh123.send_command("show ip int brief")
    regexname123 = re.compile(r"Ethernet0/0                (\S+)")
    newname123 = re.findall(regexname123, out123)
    print(f"Device name: {outname123} and its management IP is: {newname123[0]}")