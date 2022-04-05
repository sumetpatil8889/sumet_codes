from napalm import get_network_driver  # These drivers are to handle the ssh
import json

driver123 = get_network_driver("ios")  # We get the driver of ios type
ios123 = driver123("192.168.1.128", "admin123", "admin123")
ios123.open()

output12 = ios123.ping(destination="8.8.8.8", count=10)
output123 = ios123.get_interfaces()
output1234 = ios123.get_arp_table()
output12345 = ios123.get_facts()


# for xyz in output123:
#     print(xyz)

dumps12 = json.dumps(output12, sort_keys=True, indent=4)
dumps123 = json.dumps(output123, sort_keys=True, indent=4)
dumps1234 = json.dumps(output1234, sort_keys=True, indent=4)
dumps12345 = json.dumps(output12345, sort_keys=True, indent=4)

print(dumps12)
print(dumps123)
print(dumps1234)
print(dumps12345)

#capture
with open("get_facts.txt", "w") as f:
    f.write(dumps12)
    f.write(dumps123)
    f.write(dumps1234)
    f.write(dumps12345)

ios123.close()
