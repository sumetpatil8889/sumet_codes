# in naplam it is going to import get_network_driver
import napalm_ios_ad
import napalm_prog_2
from napalm_prog_2 import get_network_driver
import json

driver123 = get_network_driver("ios")
ios123 = driver123("192.168.1.171", "admin","cisco")
ios123.open()  # initialize ssh connection
output111 = ios123.get_facts()
print(output111)
# output1234 = ios123.get_arp_table()
# output12345 = ios123.get_interfaces()
# output123 = ios123.ping(source="192.168.1.171", destination="8.8.8.8", count=10)

# dumps123 = json.dumps(output123, sort_keys=True, indent=4)
# dumps1234 = json.dumps(output1234, sort_keys=True, indent=4)
# dumps12345 = json.dumps(output12345, sort_keys=True, indent=4)

dumps111 = json.dumps(output111, sort_keys=True, indent=4)

# print(dumps123)
# print(dumps1234)
# print(dumps12345)

print(dumps111)
#capture
with open("get_info.txt", "w") as f:
	f.write(dumps111)
	# f.write(dumps123)
	#f.write(dumps1234)
	#f.write(dumps12345)
ios123.close()


#!!! NETMIKO |  PARAMIKO | PARAMIKO | NORNIR | SCRAPLI
#---> nornir ---> nornir_napalm
#---> limitation ---> 4-5 vendors support only
#---> napalm ---> NETMIKO -- ssh ---> cisco
#---> output ---> dictionary format
#---> certain readymade functions of NAPALM: compare, rollback, configpush
#!!!






