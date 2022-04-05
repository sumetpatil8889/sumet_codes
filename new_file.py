from napalm import get_network_driver
driver123 = get_network_driver("ios")
ios123 = driver123("192.168.1.116", "admin", "cisco")
ios123.open()  # initialize ssh connection
print(ios123)
ios123.close()
