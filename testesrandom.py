#!/bin/python3  
import os 
import ipaddress
from getmac import get_mac_address

online = 0
for host in ipaddress.IPv4Network('192.168.1.0/24'):
  response = os.system("ping -c 1 " + str(host) + " > /dev/null 2>&1")
  if response == 0:
    print (str(host)+ " está online!" + get_mac_address(str(ip=host)))
    online=online+1
