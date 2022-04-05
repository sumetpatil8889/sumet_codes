## HOW TO CLEAR IP OSPF WITH SSH TIMING COMMAND!!!


from getpass import getpass
from netmiko import ConnectHandler, file_transfer
# to initiate connection we need this plugin

username123 = input("Enter the username: \n")
print("Please enter the password first for the script to run successfully\n")
password_123 = getpass()

list_ip = ["192.168.1.117"]
for device_ip in list_ip:

    device123 = {
        "device_type": "cisco_ios",
        "ip": device_ip,
        "username": username123,
        "password": password_123,
        "port": 22
    }

    ssh123 = ConnectHandler(**device123)
    cmd123 = ssh123.send_command_timing("clear ip ospf process")

    if "Reset" in cmd123:
        input123 = input(f"Please enter yes/no to proceed with clearing ospf process for {device_ip}: ")
        if "yes" in input123:
            ssh123.write_channel("yes\n")
            final123 = ssh123.send_command("show ip ospf  neighbor detail | i up")
            print(final123)
        else:
            print("ok! please run the script again whenever you want to clear the ospf process!!")
    else:
        print("Ospf is yet to configured!!!")
