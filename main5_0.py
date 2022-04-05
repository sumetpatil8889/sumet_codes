#telnet_lib script

import telnetlib
import time
HOST = "192.168.1.167"
user = "admin"
pass1 = "cisco"

tn123 = telnetlib.Telnet(HOST)
tn123.read_until(b"Username:")
tn123.write(user.encode("ascii") + b"\n")  # or tn123.write(b("admin"))
tn123.read_until(b"Password:")
tn123.write(pass1.encode("ascii") + b"\n")  # or tn123.write(pass1.encode("utf8"))

# telnet successful

tn123.write(b"term len 0 \n")
tn123.write(b"show run \n")
time.sleep(2)
out123 = tn123.read_very_eager().decode("ascii")
print(out123)