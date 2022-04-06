import re
import time
from getpass import getpass
from netmiko import ConnectHandler, redispatch
from netmiko.ssh_exception import SSHException, AuthenticationException, NetMikoAuthenticationException, NetMikoTimeoutException
# First thing is first need to create a list for IPs of the devices where you want to run the script
list_of_devices_IPs = ["192.168.1.177", "192.168.1.180", "192.168.1.181", "192.168.1.182", "192.168.1.183", "192.168.1.184"]

i = 0
j = 3
while i < j:
    ubuntu123 = "192.168.1.117"
    ubuntu_un = input("Enter the username and password to login to the Ubuntu server:\n")
    password = getpass()
    device_123 = {
                  "device_type": "linux",
                  "ip": ubuntu123,
                  "username": ubuntu_un,
                  "password": password,
                  "port": 22
                 }

    if ubuntu_un == "linux" and password == "123":
        # Now we need to create an object which will get all these parameters that we passed in the dictionary and send it to
        # the devices

        # Need Connect handler object to do it

        ssh123 = ConnectHandler(**device_123)
        output123 = ssh123.send_command("ip addr")
        regex_output123 = re.compile(r"inet\s(\S+)\sbrd\s")
        new_reg_123 = regex_output123.findall(output123)
        print(f"Logged into the Linux and the IP of the Linux Bastion server is : {new_reg_123[0]}")

        # (\S+) - will get what you want exactly meaning the entire word or address before any space
        # (+.) - will give everything from there till the end in that line
        # (\s) - stands for space
        # output123 = ssh123.send_command("ip addr")
        # reg123 = re.compile(r"Here you need to enter the regular expression")
        # new_out123 = reg123.findall(output123) > output is in the list form
        # print(new_out123[0])

        start = 0
        end = 3

        while start < end:
            try:
                username123 = input("Enter the username for the router: \n")
                pw123 = getpass()
                ip123 = input("enter the IP of the router: \n")

            except NetMikoTimeoutException:
                print("Please try again timed out!")
            except SSHException:
                print("SSH exception issue!")
            except NetMikoAuthenticationException:
                print("Netmiko SSH Exception, wrong password!")
            except AuthenticationException:
                print("Authentication exception, wrong creds")

            if username123 == "admin" and pw123 == "cisco" and (ip123 in list_of_devices_IPs):
                ssh123.write_channel(f"ssh {username123}@{ip123}\n")
                time.sleep(1)
                read123 = ssh123.read_channel()
                if "yes" in read123:
                    yes123 = input("Please enter yes to proceed: ")
                    if "yes" in yes123:
                        ssh123.write_channel("yes\n")
                        time.sleep(1)
                        ssh123.write_channel(pw123 + "\n")
                        time.sleep(1)
                        output1234 = ssh123.send_command("show ip int br")
                        print(output1234)
                        break
                    else:
                        new_yes_123 = input("Do you want to try it for a different device? ")
                        if new_yes_123 == "yes":
                            pass
                        else:
                            break
                else:
                    ssh123.write_channel(pw123 + "\n")
                    time.sleep(1)
                    print(ssh123.send_command("show ip int br"))
                    redispatch(ssh123, device_type="cisco_ios")
                    print(ssh123.send_command("do show run | i username"))
                    print(ssh123)
                    break
            else:
                print("Either username/password/IP is wrong! Please try again!")
                start = start + 1

        print("program done!")
        break
    else:
        print("Either username or password is wrong! Please try again!")
        i = i + 1


### Important points to remember is to make sure you dont forget about the
# 1. write_channel and read channel
# 2. ssh123.write_channel(ssh admin@x.x.x.x)
#     time.sleep(1) > this is important too
# 3. ssh123.read_channel to read the output of the above command and check if "yes"is present in it
# 4. Then most important dont forget about to enter "yes\n" via ssh123.write_channe("yes\n") this is to get the next
#    promt that is for password
# 5. Finally after time.sleep(1) ssh123.write_channel(pw123 + "\n")
#     time.sleep(1) and get the output via variable

""" This program is a good example to learn 
1. regex with the re module, 
2. try and exception, 
3. login reattempts, 
4. how to login first time to any device, 
5. make sure your device is configured with ssh config
6. redispatch
7. Loops while and for
8. conditional statements
9. read channel and write channel
10. time
11. Connect handler
12. getpass 
 
 R1>
R1>enable 
R1#configure terminal 
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#
R1(config)#ip domain-name Technig.com
R1(config)#crypto key generate rsa 
The name for the keys will be: R1.Technig.com
Choose the size of the key modulus in the range of 360 to 2048 for your
  General Purpose Keys. Choosing a key modulus greater than 512 may take
  a few minutes.

How many bits in the modulus [512]: 1024
% Generating 1024 bit RSA keys, keys will be non-exportable...[OK]

R1(config)#
*Mar 1 0:5:57.974:  %SSH-5-ENABLED: SSH 1.99 has been enabled 
R1(config)#
R1(config)#username Admin password Technig
R1(config)#line vty 0 4
R1(config-line)#login local 
R1(config-line)#transport input ssh 
R1(config-line)#exit
R1(config)#ip ssh version 2
R1(config)#ip ssh authentication-retries 3
R1(config)#
R1(config)#ip ssh time-out 120
R1(config)#exit
R1#

 """