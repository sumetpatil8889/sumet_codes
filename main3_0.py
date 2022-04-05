from netmiko import redispatch
import time
from netmiko import ConnectHandler
import logging


logging.basicConfig(filename='netmiko_global.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

device_123 = {
    "device_type": "terminal_server",
    "ip": "172.28.140.201",
    "username": "sumet",
    "password": "CBOsc*1989",
    "port": 22
}

ssh123 = ConnectHandler(**device_123)
output123 = ssh123.send_command("ip r")
print(output123)
print("*********THIS IS AN UBUNTU BASTION**********")

ip123 = ["192.168.1.168"]
for xyz in ip123:
    user123 = "admin"
    ssh123.write_channel("ssh -l " + user123 + " " + xyz + "\n")
    start = 0
    end = 4
    while start < end:
        ssh123.write_channel(input("Enter the password for " + xyz + ":") + "\n")
        time.sleep(1)
        output1234 = ssh123.read_channel()
        if "#" in output1234 or ">" in output1234:
            print("Login is successful!!!")
            break
        else:
            start += 1
    redispatch(ssh123, device_type="cisco_ios")
    cmds_list = ["do show ip int br", "do show run", "do show clock"]
    for cmds in cmds_list:
        new_cmd123 = ssh123.send_config_set(cmds)
        print(new_cmd123)