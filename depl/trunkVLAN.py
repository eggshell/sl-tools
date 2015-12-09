#!/usr/bin/python

import getpass
import requests
import SoftLayer
import sys

# authenticate SoftLayer client
username = raw_input("Please enter your SoftLayer username: ")
api_key  = getpass.getpass("Please enter your SoftLayer API key: ")
client   = SoftLayer.Client(username=username, api_key=api_key)

hw_mgr  = SoftLayer.HardwareManager(client)
net_mgr = SoftLayer.NetworkManager(client)

# create masks to only grab needed information from objects
hw_mask   = "mask[id,hostname]"
nics_mask = "mask[id,networkComponents.id]"
vlan_mask = "mask[id,name]"

# find Neutron vlan
vlans = net_mgr.list_vlans(mask=vlan_mask)
for vlan in vlans:
    if "NEUTRON" in vlan["name"].upper():
        neutron_vlan = vlan["id"]

# find correct servers to open VLAN trunk to
servers = hw_mgr.list_hardware(mask=hw_mask)
keywords = ['CONTROLLER', 'CTL', 'KVM01', 'KVM02', 'KVM001', 'KVM002', 'KVM1', 'KVM2', 'QKR', 'VYATTA', 'MGW']
bootstrap_hosts = []

for server in servers:
    found = False
    found = any(keyword in server['hostname'].upper() for keyword in keywords)
    if boolean == True:
        bootstrap_hosts.append(server)

for host in bootstrap_hosts:
    nics  = hw_mgr.get_hardware(host["id"],mask=nics_mask)
    for nic in nics["networkComponents"]:
        url = 'https://' + username + ':' + api_key + '@api.service.softlayer.com/rest/v3/SoftLayer_Network_Component/' + str(nic["id"]) + '/addNetworkVlanTrunks.json'
        data = '{"parameters":[[{"id": ' + str(neutron_vlan) + '}]]}'
        response = requests.post(url, data=data)
