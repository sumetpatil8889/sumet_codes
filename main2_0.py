# 1. first you should start with import statements
import xlrd
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetmikoTimeoutException, NetmikoAuthenticationException, SSHException

# device_ip123 = list(input("Please enter the IP of the device where you want to send the command:\n"))
# device_ip123 = input("Enter the ip of the device: ")
# print("Please enter the password: ")
# password123 = getpass()

# read_ip123 =  r"C:\Users\spsp1\Documents\python_folder_files\list_ips.txt"
# open_ip123 = open(read_ip123)
# openread123 = open_ip123.read().splitlines()
# list_ip = ["192.168.1.154", "192.168.1.155"]


# getting data imported from Excel
Workbook123 = xlrd.open_workbook_xls(r"C:\Users\spsp1\Documents\python_folder_files\Python_WS.xls")
sheet123 = Workbook123.sheet_by_name("NY_Branch")

for xyz in range(1, sheet123.nrows):
    Excel_hostname123 = sheet123.row(xyz)[0].value
    # print(Excel_hostname123)
    Excel_ip123 = sheet123.row(xyz)[1].value
    # print(Excel_ip123)
    Excel_UN123 = sheet123.row(xyz)[2].value
    # print(Excel_UN123)
    Excel_pw123 = sheet123.row(xyz)[3].value
    # print(Excel_pw123)
    Excel_dt123 = sheet123.row(xyz)[4].value
    # print(Excel_dt123)
    Excel_conf123 = sheet123.row(xyz)[5].value
    New_Excel_conf123 = Excel_conf123.splitlines()
    # print(New_Excel_conf123)

    # 2. second step is to write the dictionary to login to the devices
    device123 = {
        "device_type": Excel_dt123,
        "ip": Excel_ip123,
        "username": Excel_UN123,
        "password": Excel_pw123,
        "port": 22
    }

    # 3. Create a pipe/session with the box which will throw all these attributes toward the box to login to the device
    # also configuring the try and catch exception method

    try:
        ssh123 = ConnectHandler(**device123)
    except NetmikoTimeoutException:
        print("Timeout error " + Excel_hostname123 + " " + Excel_ip123)
        break
    except NetmikoAuthenticationException:
        print("Password did not work, try running the program again " + Excel_hostname123 + " " + Excel_ip123)
    except SSHException:
        print("SSH is not working " + Excel_hostname123 + " " + Excel_ip123)

    # 4. Send the command to the device with the help  of the ConnectHandler object "ssh123"

    # sendcmd123 = ssh123.send_command("show run")
    # sendcmd1234 = ssh123.send_config_set(["router ospf 1", "network 0.0.0.0 0.0.0.0 area 0"])

    # 5 send command from file
    # sendcmd1235 = ssh123.send_config_from_file(r"C:\Users\spsp1\Documents\python_folder_files\cmd_list.txt")
    sendcmd1235 = ssh123.send_config_set(New_Excel_conf123)

    # print(sendcmd123)
    print(sendcmd1235)

    # 6 create a hostname
    host123 = ssh123.find_prompt()
    newhost123 = host123.strip("#")

    # 7 create a file and save the config in it

    directory123 = r"C:\Users\spsp1\Documents\python_folder_files\save_config_"
    save_conf_file123 = open(directory123 + " " + newhost123 + " " + ".txt", "a")

    # 8 clear ip ospf

    # sendcmd12356 = ssh123.send_command_timing("clear ip ospf process")
    # if "Reset" or "reset" in sendcmd12356:
    #     sendcmd123567 = input("Do you want to proceed further? Press <yes/no> \n")
    #     if "yes" in sendcmd123567:
    #         ssh123.write_channel("yes\n")
    #         clear_ospf_123 = ssh123.send_command("show ip ospf neighbor detail | i up")
    #         print("ospf neighborship for this device: " + clear_ospf_123)
    #
    #     else:
    #         print("Sorry! you can try later!!")
    # else:
    #     print("Ospf is not configured!!")

    # save_conf_file123.write(sendcmd123)
    save_conf_file123.write(sendcmd1235)

    # #8 scp file transfer
    # scp_enable123 = ssh123.send_config_set("ip scp server enable")
    # scp_cmd123 = ssh123.send_command("debug ip scp")
    # print(" I AM GOING TO DO FT!!!")
    # push123 = file_transfer(ssh123, source_file="R0.txt", dest_file="new_R0.txt", file_system="disk0:/", disable_md5= False, direction="put", overwrite_file= True )
    # print(push123)
