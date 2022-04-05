# so you want to pull info with regex and use it or store it in a csv file

from netmiko import ConnectHandler
import re
import os
from getpass import getpass
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException, AuthenticationException, SSHException
import csv
from csv import DictWriter

i = 0

while i < 4:
    try:
        enter123 = input("Please enter '(yes)' to proceed and '(no)' to quit: ")
        if enter123 == "yes":
            ip123 = input("Enter the IP address of the device to which you want to connect: ")
            username123 = input("Enter the username of the device to which you want to connect: ")
            print("Enter the password of the device to which you want to connect: ")
            password123 = getpass()

            device123 = {
                "device_type": "cisco_ios",
                "ip": ip123,
                "username": username123,
                "password": password123,
                "port": 22,
            }

            ssh123 = ConnectHandler(**device123)
            img123 = ssh123.send_command("show version")
            img_path123 = re.compile(r"System image file is (.+)")
            new_img_path123 = re.findall(img_path123, img123)
            print(f"The directory where the system's image is stored is: {new_img_path123[0]}")

            hostname123 = re.compile(r"(.+)\suptime")
            new_hostname123 = re.findall(hostname123, img123)
            print(f"Hostname of the device: {new_hostname123[0]}")

            ipaddr123 = ssh123.send_command("show interfaces GigabitEthernet 0/0")
            ip123 = re.compile(r"Internet address is (.+)/24")
            new_ip123 = re.findall(ip123, ipaddr123)
            print(f"MGMT_IP of the device: {new_ip123[0]}")

            ver123 = re.compile(r"(.+), RELEASE SOFTWARE")
            new_ver123 = re.findall(ver123, img123)
            print(f"version of the device: {new_ver123[0]}")

            file123 = os.path.isfile(r"C:\Users\spsp1\Documents\python_folder_files\new_regex123.csv")
            if not file123:
                with open(r"C:\Users\spsp1\Documents\python_folder_files\new_regex123.csv", "w", newline="") as newcsv:
                     mycustomfields123 = ["HOSTNAME", "VERSION", "MGMT_IP", "IMAGE_PATH"]
                     dict_write123 = csv.DictWriter(newcsv, fieldnames=mycustomfields123)
                     dict_write123.writeheader()
                     dict_write123.writerow({
                         "HOSTNAME": new_hostname123[0],
                         "VERSION": new_ver123[0],
                         "MGMT_IP": new_ip123[0],
                         "IMAGE_PATH": new_img_path123[0],
                        })
            if file123:
                with open(r"C:\Users\spsp1\Documents\python_folder_files\new_regex123.csv") as newcsv:
                    mycustomfields123 = ["HOSTNAME", "VERSION", "MGMT_IP", "IMAGE_PATH"]
                    dict_write123 = csv.DictWriter(newcsv, fieldnames=mycustomfields123)
                    #dict_write123.writeheader()
                    dict_write123.writerow({
                        "HOSTNAME": new_hostname123[0],
                        "VERSION": new_ver123[0],
                        "MGMT_IP": new_ip123[0],
                        "IMAGE_PATH": new_img_path123[0],
                    })


        elif enter123 == "no":
            print("Rerun the script next time again from the beginning to get the output!! Thank you!!!")
            break

        elif enter123 != "yes":
            i = i + 1
            if i == 4:
                print("You have reached maximum number of attempts, please try again!!!")
                break

    except NetMikoAuthenticationException:
        print("Wrong password try again please!!!")
    except NetMikoTimeoutException:
        print("Due to wrong info entered session has timed out try again please !!!")
    except AuthenticationException:
        print("Authentication error try again please!!!")
    except SSHException:
        print("please configure SSH to try again!!!")
    except ValueError:
        print("Please check if you have entered the correct info or not!!!")

