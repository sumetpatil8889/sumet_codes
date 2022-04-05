from netmiko import ConnectHandler, redispatch
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException, SSHException, AuthenticationException
import time
from getpass import getpass

device123 = {
    "username": "linux",
    "password": "123",
    "ip": "192.168.1.127",
    "device_type": "terminal_server",
    "port": 22
}

ssh123 = ConnectHandler(**device123)
print(" I AM LOGGED INTO MY UBUNTU LINUX SERVER!!! NON-AUTHORIZED USERS ARE NOT ALLOWED TO LOG INTO THE DEVICE!!!")

start = 0
end = 4

while start < end:
    # SO NOW I AM INTO THE SERVER AND NOW I NEED TO GET INTO THE CISCO IOS DEVICE!!!
    # SO FIRST THING WOULD BE TO CONNECT TO THE DEVICE WITH THE USERNAME AND PASSWORD!!!
    try:
        ip123 = input("Enter the IP of the device to which you wanted to connect: ")
        username123 = input("Enter the username: ")
        password123 = getpass()
    except NetMikoAuthenticationException:
        print("WRONG PASSWORD!!! PLEASE TRY AGAIN!!!")
    except NetMikoTimeoutException:
        print("TIMEOUT PLEASE TRY AGAIN!!!")
    except SSHException:
        print("SSH EXCEPTION PLEASE TRY AGAIN")
    except AuthenticationException:
        print("AUTHENTICATION EXCEPTION PLEASE TRY AGAIN!!!")

    if username123 == "admin123" and password123 == "admin123":
        ssh123.write_channel("ssh " + username123 + "@" + ip123 + "\n")
        time.sleep(1)
        ssh123.write_channel(password123 + "\n")
        print(ssh123.send_command("show ip int br"))
        redispatch(ssh123, device_type="cisco_ios")
        print(ssh123.send_config_set("logging host 12.12.12.12"))
        break
    else:
        print("WRONG CREDS PLEASE TRY AGAIN!!!")
        start = start + 1

print("PLEASE RE-RUN THE SCRIPT YOU HAVE REACHED TO MAXIMUM TRIALS!!!")