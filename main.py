import logging
from getpass import getpass

from netmiko import ConnectHandler
from netmiko.ssh_exception import NetmikoTimeoutException, NetmikoAuthenticationException, SSHException

logging.basicConfig(filename='ospfts.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# password_123 = input("Enter the admins' password for the devices:\n")
# Above command will not be able to encrypt the password, so we need to use getpass function


print("Please enter the password first for the script to run successfully\n")
password_123 = getpass()
list_ip = ["192.168.1.154"]

# open_list123 = open("C:\\Users\\spsp1\\Documents\\python_folder_files\\list_ips.txt")
# new_openlist123 = open_list123.read().splitlines()


for device_ip in list_ip:
    device123 = {
        "device_type": "cisco_ios",
        "ip": device_ip,
        "username": "admin",
        "password": password_123,
        # This is a getpass function to encrypt the password to stay invisible while you are typing
        "port": 22  # Here no need of comma
    }
    try:
        ssh123 = ConnectHandler(**device123)
    except NetmikoTimeoutException:
        print("Time out observed on " + device_ip)
        continue
    except NetmikoAuthenticationException:
        print("Not Authenticated " + device_ip)
        continue
    except SSHException:
        print("SSH disabled on " + device_ip)
        continue

    # enable_scp123 = ssh123.send_config_set("ip scp server enable")
    # scp_debug123 = ssh123.send_command("debug ip scp")
    # print("********** I AM GOING TO DO REMOTE TRANSFER OF THE FILE**********")
    # push123 = file_transfer(ssh123, source_file="R0.txt", dest_file="copied_file.txt", disable_md5="False", direction="put", overwrite_file=True)
    # print(push123)
    #
    # hostname123 = ssh123.find_prompt()
    # newhost123 = hostname123.strip("#")
    # print("pushing configs to " + newhost123 + " " + device_ip)
    # selectoption123 = input("Please enter the file name for device " + newhost123 + " device ip " + device_ip + ":\n")
    # output123 = ssh123.send_config_from_file(selectoption123)

    # how to get the hostname of the device, but we will get the output in Name#, so if you want to remove
    # the "#" then you need to use strip method. There are three types of strip method
    # - .strip("#"), .lstrip(), .rstrip() i.e- left and right strip()
    # you can also use slicing if x is a list then [:-1] or [len(x)-1]

    # print(hostname123)

    # print("""
    # Please choose one of the files from the file list below:
    # 1.R1.txt
    # 2.R0.txt
    # """)

    # filepath123 = "C:\\Users\spsp1\\Documents\\python_folder_files\\backup_"
    # opennewfile123 = open(filepath123 + device_ip + "_" + newhost123 + "_" + ".txt", "a")
    # opennewfile123.write(output123)
    # output123_1 = ssh123.send_config_set(["router ospf 1", "network 0.0.0.0 0.0.0.0 area 0"])
    # print(output123_1)
    showclivariable = ["show ip int br", "show clock", "show ip protocol"]
    for xyz in showclivariable:
        output123 = ssh123.send_command(xyz)
        print(output123)
    ssh123.send_config_from_file  # this is a combination of the send_config_set + open command sent to the devices

    # print(output123)

    # show_command_list = ["show ip protocol", "show ip ospf neighbor", "show run"]
    # for new_cmds in show_command_list:
    #     output123_1 = ssh123.send_command(new_cmds)
    #     # This command is just to send a single command at a time
    #     print(output123_1)
    #     opennewfile123.write(output123_1)
    #
    # clear_ospf123 = ssh123.send_command_timing("clear ip ospf process")
    # print(clear_ospf123)
    #
    # if "Reset" or "reset" in clear_ospf123:
    #     user123 = input("Please decide if you want to proceed with the clearing the process now! <yes/no>?\n")
    #     if "yes" in user123:
    #         push_cmd_123 = ssh123.write_channel("yes\n")
    #         show_cmd_123 = ssh123.send_command("show ip ospf neighbor detail | i up")
    #         print(show_cmd_123)
    #     else:
    #         print("Alright you can do it later!!")
    # else:
    #     print("There is no ospf configured on this device")

print("######******___SCRIPT COMPLETED___******######")

## Nornir author has done is he combined concurrent module with netmiko module
## you can also use concurrent module and napalm module
## concurrent module with scrappy module
## All these things are to automate multiple devices at the same time
