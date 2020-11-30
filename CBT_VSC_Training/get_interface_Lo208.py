import requests
import json
from pprint import pprint

url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=Loopback208"

payload={}
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

#api_data = response.json()
#print("/" * 50)
#pprint(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
#print("/" * 50)
#if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == 'if-state-up' :
#  print('Interface is up')