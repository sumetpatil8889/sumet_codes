from netmiko import ConnectHandler
import re  # inbuilt of python
import csv
import os
from netmiko.snmp_autodetect import SNMPDetect


snmp123 = input("Enter the snmp sting: ")

multidevice123 = ["192.168.1.151", "192.168.1.152"]

for xyz in multidevice123:

    snmp12345 = SNMPDetect(xyz, snmp_version="v3", user="snmpuser123", auth_key= snmp123, auth_proto="sha", encrypt_proto="aes128", encrypt_key= snmp123)
    device_type = snmp12345.autodetect()
    print(device_type)

    router = {
        "device_type": device_type,
        "ip": xyz,
        "username": "admin",
        "password": "cisco",
    }

    ssh123 = ConnectHandler(**router)

    # device_name = ssh123.find_prompt()
    # device_name = device_name.strip("#")
    # ssh123.send_config_set(["snmp-server community cisco123"])
    # snmp123 = ssh123.send_command("show run | i snmp")
    # print(f"{snmp123} on device {device_name}")

    # !!! v2c community string
    # ________________________
    # snmp-server community cisco123snmp
    # v3 config
    #------------
    # snmp-server group group3 v3 priv
    # snmp-server user snmpuser123 group group3 v3 auth sha cisco123 priv aes 128 cisco123
    # !!!


    output123 = ssh123.send_command("show version")
    output456 = ssh123.send_command("show inventory")
    output789 = ssh123.send_command("show interfaces")

    #
    #regex construction
    # by default it starts with "^" and ends with "$ >> ' ^.....$ '

    #https://regex101.com/ - you can use this to see if you are able to find the placeholder and its result


    regexuptime123 = re.compile(r"uptime\sis\s(.+)")  # This is a query >> (r"uptime\sis\s(\S)")
    # If you want to run this query over on this variable >> output123, how will you do that?
    # \s >> stands for spaces in between, (\S) >>  stands for one digit or char of the output we want.
    # To get the entire output we use (\S+)
    # And most important if you want everything after the placeholder in this case which is "uptime is "
    # then use (.+) and when there are multiple spaces you can use >> \s+ or you can try copying and paste as it is in the
    # regex query

    uptime123 = regexuptime123.findall(output123)
    # you use regexuptime123 variable which refers to the query of getting the uptime in line 18
    # and run it on the output123 variable with the findall command where it finds the query output on the entire
    # output of the show version and gets the uptime

    regexhostname123 = re.compile(r"(.+)\suptime\sis")
    hostname123 = regexhostname123.findall(output123)

    # BELOW ARE THE THREE WAYS YOU CAN GET THE SERIAL NUMBER OF THE DEVICE
    # regexserial123 = re.compile(r"Processor\sboard\sID\s(.+)")
    # serial123 = regexserial123.findall(output123)

    # regexserial123 = re.compile(r"PID: CISCO7206VXR      , VID:    , SN: (.+)")
    # serial123 = regexserial123.findall(output456)

    regexserial123 = re.compile(r"PID:\sCISCO7206VXR\s+,\sVID:\s+,\sSN:\s(.+)")
    serial123 = regexserial123.findall(output456)

    regexmgmtip123 = re.compile(r"\sInternet\saddress\sis\s(.+)/")
    mgmtip123 = regexmgmtip123.findall(output789)

    regeximageip123 = re.compile(r"System\simage\sfile\sis\s(.+)")
    image123 = re.findall(regeximageip123, output123)  # YOU CAN ALSO GET THE RESULT IN THIS WAY USING "re.findall()"

    print(f"uptime of the device {hostname123[0]} with Management IP {mgmtip123[0]} and serial number {serial123[0]} is: {uptime123[0]}")
    print(f"The image for the respective device {hostname123[0]} is stored at {image123[0]}")

    file123 = os.path.isfile(r"C:\Users\spsp1\Documents\python_folder_files\regexauto.csv")
    if not file123:
        with open(r"C:\Users\spsp1\Documents\python_folder_files\regexauto.csv", "w", newline="") as sumetcsv:
            mycustomfieldnames123 = ["HOSTNAME", "UPTIME", "SERIAL", "MGMT IP", "IMAGE PATH"]
            write123 = csv.DictWriter(sumetcsv, fieldnames=mycustomfieldnames123)
            write123.writeheader()
            write123.writerow({
                                "HOSTNAME": hostname123[0],
                                "UPTIME": uptime123[0],
                                "SERIAL": serial123[0],
                                "MGMT IP": mgmtip123[0],
                                "IMAGE PATH": image123[0]
            })

    if file123:
        with open(r"C:\Users\spsp1\Documents\python_folder_files\regexauto.csv", "a", newline="") as sumetcsv:
            mycustomfieldnames123 = ["HOSTNAME", "UPTIME", "SERIAL", "MGMT IP", "IMAGE PATH"]
            write123 = csv.DictWriter(sumetcsv, fieldnames=mycustomfieldnames123)
            #write123.writeheader()
            write123.writerow({
                                "HOSTNAME": hostname123[0],
                                "UPTIME": uptime123[0],
                                "SERIAL": serial123[0],
                                "MGMT IP": mgmtip123[0],
                                "IMAGE PATH": image123[0]
            })

