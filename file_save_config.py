## HOW TO SAVE THE CONFIG IN A FILE##
from getpass import getpass
from netmiko import ConnectHandler   # to initiate connection we need this plugin
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
    try:
        ssh123 = ConnectHandler(**device123)

    except NetmikoTimeoutException:
        print("NO RESPONSE FROM THE DEVICE: " + device_ip)
        continue
    except NetmikoAuthenticationException:
        print("PASSWORD INCORRECT FOR THE DEVICE: " + device_ip)
        continue
    except SSHException:
        print("SSH DISABLED FOR THE DEVICE: " + device_ip)
        continue

    device_name123 = ssh123.find_prompt()
    # >> YOU STRIP '#' FROM THE DEVICE NAME
    device_name123 = device_name123.strip("#")

    # THIS IS HOW YOU CREATE A DIR FIRST AND THEN USE THE OPEN COMMAND TO SAVE THE FILE AND THEN WRITE IN THAT FILE
    file123 = r"C:\Users\spsp1\Documents\python_folder_files\backup_"
    newfile123 = open(file123 + device_name123 + " " + device_ip + " " + ".txt", "a")
    out123 = ssh123.send_command("show run")
    newfile123.write(out123)



