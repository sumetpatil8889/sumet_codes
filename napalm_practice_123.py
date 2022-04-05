# Let us write a script where we can pull the commands from Excel sheet and apply to multiple devices using napalm
# Use regex to pull a particular info from the device
# Compare the config using napalm and find out the difference
# Update it accordingly as per the difference
#  Add try and exception


import xlrd
# start slowly think what would be the first thing you would do?
from napalm import get_network_driver
import json
from netmiko.ssh_exception import AuthenticationException, SSHException, NetMikoAuthenticationException, NetMikoTimeoutException
import re
import netmiko
from netmiko import ConnectHandler

start = 0
end = 4
while start < end:
        try:
            print("Please enter the requested info below: ")
            user123 = input("Enter the username: ")
            pass123 = input("Enter the password: ")
            if user123 == "admin123" and pass123 == "admin123":
                # second thing would be to use the driver and assign it to a reference object
                ios123 = get_network_driver("ios")

                # Now what???? you have to create an ssh session, so how will you do it? But before that we need to send the attributes too
                new_ios123 = ios123("192.168.1.128", username=user123, password=pass123)

                # session was open
                new_ios123.open()

                # created workbook
                wb123 = xlrd.open_workbook_xls(r"C:\Users\spsp1\Documents\python_folder_files\napalm.xls")
                sheet123 = wb123.sheet_by_name("Sheet1")

                # Now we need to read the content from the Excel file
                read_sheet123 = sheet123.row(0)[0].value

                # now send the config to the device
                new_ios123.load_merge_candidate(config=read_sheet123)

                # config compared
                check_config123 = new_ios123.compare_config()

                # print the difference in config
                print(check_config123)

                if check_config123:
                    get_request123 = input("DO YOU WANT TO PROCEED FURTHER TO MAKE CHANGES NOW???")
                    if "yes" or "YES" in get_request123:
                        print("pushing the config now!!!")
                        new_ios123.commit_config()
                    else:
                        print("OK!! No changes done for now")
                        new_ios123.discard_config()

                else:
                    print("All good!!! No need of any updates and changes to be done!!")

                rollback123 = input("DO you want to roll back???")

                if "yes" or "YES" in rollback123:
                    new_ios123.rollback()
                else:
                    print("OK!! NO roll backs")

                # netmiko regex
                device123 = {
                    "username": "admin123",
                    "password": "admin123",
                    "device_type": "cisco_ios",
                    "ip": "192.168.1.128"
                }

                ssh123 = ConnectHandler(**device123)
                ver123 = ssh123.send_command("show version")
                re123 = re.compile('System image file is\s(.+)')
                dir123 = re.findall(re123, ver123)
                print(dir123)

                # napalm output
                image123 = new_ios123.get_facts()
                new_img123 = json.dumps(image123)
                print(new_img123)

                # session closed
                new_ios123.close()

            else:
                start = start + 1
                if start == 4:
                    print("Run the script again. You have reached max attempts!!!")
                    break

        except NetmikoAuthenticationException:
            print("Wrong pw!!!")
        except AuthenticationException:
            print("Wrong pw!!!")
        except BadAuthenticationType:
            print("Bad Authentication")
        except SSHException:
            print("SSH exception")
        except PartialAuthentication:
            print("Partial AUth!!!")
        except PasswordRequiredException:
            print("Password required!!!")
        except NetMikoTimeoutException:
            print("Netmiko Timeout due to wrong info entered!!!")



