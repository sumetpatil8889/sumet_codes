## HOW TO USE TRY AND EXCEPTION ##
from getpass import getpass
from netmiko import ConnectHandler, file_transfer
# to initiate connection we need this plugin
from netmiko.ssh_exception import NetmikoTimeoutException, NetmikoAuthenticationException, SSHException



list_ip = ["192.168.1.112", "192.168.1.113"]
for device_ip in list_ip:

    username123 = input("Enter the username: \n")
    print("Please enter the password first for the script to run successfully\n")
    password_123 = getpass()

    device123 = {
        "device_type": "cisco_ios",
        "ip": device_ip,
        "username": username123,
        "password": password_123,
        "port": 22
    }

    ssh123 = ConnectHandler(**device123)
    cmd123 = ssh123.send_config_from_file(r"C:\Users\spsp1\Documents\python_folder_files\cmd_list.txt")
    print(cmd123)
