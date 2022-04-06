from getpass import getpass
from netmiko import ConnectHandler

# First thing is first need to create a list for IPs of the devices where you want to run the script
list_of_devices_IPs = ["192.168.1.177", "192.168.1.180", "192.168.1.181", "192.168.1.182", "192.168.1.183"]

username = input("Enter the username for login:\n")
password = getpass()

# Second thing is Create a dictionary
for IP123 in list_of_devices_IPs:
    device_123 = {
                  "device_type": "cisco_ios",
                  "ip": IP123,
                  "username": username,
                  "password": password,
                  "port": 22
                 }

    # Now we need to create an object which will get all these parameters that we passed in the dictionary and send it to
    # the devices

    # Need Connect handler object to do it

    ssh123 = ConnectHandler(**device_123)
    ssh123.send_config_from_file(r"C:\Users\spsp1\PycharmProjects\Python_Auto_Practice\config_file_to_load_the config.txt")
    output123 = ssh123.send_config_set("do show ip int brief")
    print(output123)