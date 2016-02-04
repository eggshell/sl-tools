#!/usr/bin/python

import getpass
import requests
import SoftLayer
import sys

# authenticate SoftLayer client
username = raw_input("Please enter your SoftLayer username: ")
api_key  = getpass.getpass("Please enter your SoftLayer API key: ")
client   = SoftLayer.Client(username=username, api_key=api_key)

url = 'https://' + username + ':' + api_key +'@api.service.softlayer.com/rest/v3/SoftLayer_Account/setVlanSpan.json'
data = '{"parameters":["True"]}'
response = requests.post(url, data=data)
print response
