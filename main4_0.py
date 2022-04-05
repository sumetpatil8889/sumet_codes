from netmiko import ConnectHandler
import time


# First step create a connection with the box

device123 ={
    "device_type": "cisco_ios",
    "ip": "192.168.1.161",
    "username": "admin",
    "password": "cisco",
    "port": 22
}

ssh123 = ConnectHandler(**device123)

#  Then check how we can send the command and get the output to check if the interface is up or not

var123 = 1
while var123 == 1:
    interface = input("Enter the interface name to turn it up: \n")

    getint123 = ssh123.send_command("show ip interface " + interface)
    command123 = "interface " + interface

    if "down" in (getint123.splitlines()[0]):
        print("Turning up the interface")
        ssh123.send_config_set([command123, "no shutdown"])
    else:
        print(f"interface {interface} is already up!!!")

    newoutput123 = ssh123.send_command("show ip int br")
    print(newoutput123)