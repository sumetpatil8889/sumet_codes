from getpass import getpass

from napalm import get_network_driver

driver123 = get_network_driver("ios")
ios123 = driver123("192.168.1.128", input("Username:"), getpass())
ios123.open()
ios123.load_replace_candidate(
    filename=r"C:\Users\spsp1\Documents\python_folder_files\cisco_config.txt")  # This cmd sends the file to the dir of the device and save it as a candidate config
diff123 = ios123.compare_config()  # This command is to compare the running config with the candidate config
if len(diff123):  # This will give the number if there are any differences in the file
    print(diff123)
    change123 = input("Do you want to proceed to make the observed changes?")
    if change123 == "yes":
        print("Entering to Global Config...")
        ios123.commit_config()  # commit the changes or differences it observed after comparing the config file with the running config. If the output shows
        # + sign in front of the config that means that the candidate config file has some extra config that is going to be added into the device and if it had - sign in front of the config
        # that means it is removed from the running config because it was not present in the candidate config file
        print("done, config push is done!!!")
    else:
        print("OK! Will not make any changes!!!")
else:
    print("No changes required")
ios123.discard_config()  # This will discard the changes as the output of the len(diff123) is 0 return value

answer123 = input(
    "Do you want to rollback the config? yes/no?")  # This will give the opportunity to rollback the changes
if answer123 == "yes":
    ios123.rollback()
else:
    print("No rollback required!!!")
ios123.close()  # This to close the connection to the
