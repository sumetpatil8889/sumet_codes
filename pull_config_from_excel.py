from netmiko import ConnectHandler
from netmiko.ssh_exception import SSHException, NetmikoAuthenticationException, NetmikoTimeoutException
import xlrd


#getting data from excel
workbook123 = xlrd.open_workbook_xls(r"C:\Users\spsp1\Documents\python_folder_files\Python_WS.xls")
sheet123 = workbook123.sheet_by_name("NY_Branch")

for xyz in range(1, sheet123.nrows):
    excel_hostname123 = sheet123.row(xyz)[0].value
    excel_ip123 = sheet123.row(xyz)[1].value
    excel_username123 = sheet123.row(xyz)[2].value
    excel_password123 = sheet123.row(xyz)[3].value
    excel_device_type123 = sheet123.row(xyz)[4].value
    excel_config123 = sheet123.row(xyz)[5].value
    new_excel_config123 = excel_config123.splitlines()


# second step is to write the dictionary to login to the device

    device123 = {
        "device_type": excel_device_type123,
        "ip": excel_ip123,
        "username": excel_username123,
        "password": excel_password123,
        "port": 22
    }
    try:
        ssh123 = ConnectHandler(**device123)
        config123 = ssh123.send_config_set(new_excel_config123)
        print(config123)
    except NetmikoAuthenticationException:
        print("WRONG PASSWORD " + excel_hostname123 + " " + excel_ip123)
    except NetmikoTimeoutException:
        print("DEVICE IS UNREACHABLE " + excel_hostname123 + " " + excel_ip123)
    except SSHException:
        print("SSH DISABLED " + excel_hostname123 + " " + excel_ip123)