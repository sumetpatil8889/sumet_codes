from getpass import getpass

from napalm import get_network_driver

driver123 = get_network_driver("ios")
ios123 = driver123("192.168.1.128", input("username: "), getpass())

# 1 ssh connection done
ios123.open()

print("Next will be the config load")
# 2 does scp, copy the config to flash drive of the cisco device
#ios123.load_merge_candidate(filename="R1.txt")
ios123.load_replace_candidate("R0.txt")

print("Next will be the config compare")
# 3 once you copy, then compare the newly copied config with the running config in the device
diff123 = ios123.compare_config()

print("Next will be the output")
# 4 This will show if anything missing fromconfig then it will show in + symbol, and it will add it or something that needs to be removed from the running config will show in the minus symbol and will remove it
print(diff123)

# if found a length then below changes will happen
if len(diff123):
    answer1234 = input("do you want to commit it now? yes/no?")
    if answer1234 == "yes":
        print("Entering to Global config push...")
        ios123.commit_config()
        # To commit the config we need to have archive path configurd on the box so that it can save backup config file in the archive path so that we can use to rollback if we need to
        print("config push done!!!")

# whatever changes you were going to make it will discard it
else:
    print("No changes required!!!")
    ios123.discard_config()

# rollback
answer123 = input("do you want to rollback? yes/no?")
if answer123 == "yes":
    ios123.rollback()
else:
    print("No rollback required!!!")
ios123.close()

## NETMIKO + REGEX --> FETCH AND COUNTERS
## SCHEDULE LIBRARY ---> EVERY MONDAY 8 PM
## SMTPLIB ---> SEND MAIL TO YOU

# when you want to user smtplib - you have to activate allow less secure apps on security section

# GET CONFIG VIA NAPALM MODULE - get_config
# PUSH LOGGING HOST 1.1.1.1 - via NETMIKO
# AUTO EMAIL PUSH --> SMTP LIB

# YOU CAN ALSO SCHEDULE THIS SCHEDULE LIB