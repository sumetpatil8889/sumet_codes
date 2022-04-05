# I want to create a script using netmiko which will log in and apply the configs to the device
# For that I need one Excel sheet first, and I will use the one I already have


#1. import right modules or libraries

from netmiko import ConnectHandler
import xlrd
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException, SSHException, AuthenticationException
import time
from netmiko import ConnectHandler, redispatch
from getpass import getpass
import netmiko

def write_config_from_excel(ssh123):
    wb123 = xlrd.open_workbook_xls(r"C:\Users\spsp1\Documents\python_folder_files\Python_WS.xls")
    ws123 = wb123.sheet_by_name("NY_Branch")

    for xyz in range(1, ws123.nrows):
        # hostname123 = ws123.row(xyz)[0].value
        # ip123 = ws123.row(xyz)[1].value
        # username123 = ws123.row(xyz)[2].value
        # password123 = ws123.row(xyz)[3].value
        # device_type123 = ws123.row(xyz)[4].value
        config123 = ws123.row(xyz)[5].value
        new_config123 = config123.splitlines()

        hostname123 = ssh123.find_prompt()
        ip123 = input("Enter the IP for the device to which you want to login to the device: ")
        username123 = input("Enter the username of the device to which you want to login to the device: ")
        print("Enter the password of the device to which you want to login to the device: ")
        password123 = getpass()
        # 4. now you take all this info and shove it into the session for the device from where you want to pull the info or update the config to
        ssh123.write_channel("ssh " + username123 + "@" + ip123 + "\n")
        time.sleep(1)
        ssh123.write_channel(password123 + "\n")
        redispatch(ssh123, device_type="cisco_ios")

        try:
            ssh123.send_config_set(new_config123)
            print(f" device :{hostname123} {ip123} \n {ssh123.send_command('show ip ospf neighbor')} \n")

        except NetMikoAuthenticationException:
            print("Netmiko Auth exception")
        except AuthenticationException:
            print("Auth exception")
        except SSHException:
            print("SSH exception")
        except NetMikoTimeoutException:
            print("Timeout exception")
        return 0