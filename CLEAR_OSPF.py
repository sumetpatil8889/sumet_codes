from getpass import getpass
from netmiko import ConnectHandler, redispatch
import time

def CLEAR_OSPF(ssh123):
    # 3. Now I am into the Ubuntu next step is to get the username and password and important info to get into the device you want to log in
    #
    ip123 = input("Enter the IP for the device to which you want to login to the device: ")
    username123 = input("Enter the username of the device to which you want to login to the device: ")
    print("Enter the password of the device to which you want to login to the device: ")
    password123 = getpass()
    # 4. now you take all this info and shove it into the session for the device from where you want to pull the info or update the config to
    ssh123.write_channel("ssh " + username123 + "@" + ip123 + "\n")
    time.sleep(1)
    ssh123.write_channel(password123 + "\n")
    redispatch(ssh123, device_type="cisco_ios")
    print(ssh123.send_command("show ip ospf  neighbor detail  | i up"))
    show123 = ssh123.send_command("show ip ospf neighbor")
    print(show123)


    clear_ospf123 = ssh123.send_command_timing("clear ip ospf process")
    print("should show output here: " + clear_ospf123)
    if "Reset" in clear_ospf123:
        yes123 = input("Enter yes/no to proceed further to clear the ospf process: ")
        if "yes" in yes123:
            ssh123.write_channel("yes\n")
        else:
            print("OK!! please re-run the script whenever you want to reset the OSPF process!!")
    else:
        print("no ospf in device!")
    show_cleared_ospf123 = ssh123.send_command("show ip ospf  neighbor detail  | i up")

    return show_cleared_ospf123