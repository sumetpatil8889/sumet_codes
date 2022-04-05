## NOW SEE IF YOU CAN GET THE CONFIG OUTPUT BY TELLING WHICH DEVICE IT BELONGS TO WITH THE DEVICE IP AND ITS NAME!!!


from netmiko import ConnectHandler   # to initiate connection we need this plugin
from getpass import getpass

username123 = input("Enter the username: \n")
print("Please enter the password first for the script to run successfully\n")
password_123 = getpass()

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

    device_name123 = ssh123.find_prompt()
    #>> YOU STRIP '#' FROM THE DEVICE NAME

    device_name123 = device_name123.strip("#")
    out123 = ssh123.send_command("show run")
    print("CONFIG FOR DEVICE: " + device_name123 + " DEVICE_IP: " + device_ip)
    print(out123)
