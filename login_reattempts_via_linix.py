import time
from netmiko import ConnectHandler, redispatch
from getpass import getpass


device123 = {
    "device_type": "linux",
    "ip": "172.28.113.55",
    "username": "sumet",
    "password": "CBOsc*1989",
    "port": 22
}

ssh123 = ConnectHandler(**device123)
ipadd123 = ssh123.send_command("ip r")
print(ipadd123)
print("THIS IS UBUNTU SERVER")

username123 = input("Enter the username: ")

device_list = ["192.168.1.112", "192.168.1.113"]

for device_ip in device_list:
    ssh123.write_channel("ssh -l " + username123 + " " + device_ip + "\n")
    start = 0
    end = 4
    while start < end:
        print("Enter the password: ")
        ssh123.write_channel(getpass() + "\n")

        time.sleep(1)
        ## THIS COMMAND IS VERY IMPORTANT AS AFTER YOU ENTER A WRONG PASSWORD THEN IT WILL TAKE ANOTHER
        # 1 SECOND TO GIVE A NEW ATTEMPT TO TRY#########

        output123 = ssh123.read_channel()
        if "#" in output123:
            print("Login is successful!!!")
            break
        else:
            start += 1
    redispatch(ssh123, device_type="cisco_ios")
    cmd_list123 = ["do show ip int br", "do show clock"]
    for xyz in cmd_list123:
        new_cmd123 = ssh123.send_config_set(xyz)
        print(new_cmd123)