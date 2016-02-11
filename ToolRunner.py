import logging
import os
import string
import sys

import SoftLayer
# TODO: import custom modules depl.py and maint.py when converted from bash

class ToolRunner(object):
    def __init__(self):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    def get_config(self):
        home_dir    = os.path.expanduser("~")
        sl_config_path = home_dir + "/.softlayer"

        try:
            sl_config = open(sl_config_path, 'r')
        except IOError as e:
            logging.error("\tDependencies not met. Please run:")
            logging.info("\t$ pip install -r requirements.txt\n"
                         "\t$ slcli setup\n"
                         "\tExiting with error code 1")
            sys.exit(1)

        return sl_config

    def get_client(self, sl_config):
        username = api_key = None
        found = False

        while found is not True:
            line = sl_config.readline()
            if "username = " in line:
                username = line.replace("username = ", "")
            elif "api_key = " in line:
                api_key = line.replace("api_key = ", "")
                found = True
        # TODO: add exceptions and logging for client authentication
        client = SoftLayer.Client(username=username, api_key=api_key)
        return client

    def get_choice(self):
        choice = raw_input("What would you like to do?\n"
                           "1) Bootstrap Deployer\n"
                           "2) Generate SSH Config File\n"
                           "3) Copy Deployer Key to All Nodes\n"
                           "4) Test SSH Connectivity to All Nodes\n"
                           "5) Trunk Additional VLAN\n"
                           "6) Enable VLAN Spanning\n"
                           "7) Bootstrap Deployer\n"
                           "8) OS Reload Servers\n")
        operation = int(choice)

        if operation > 7 or operation < 1:
            logging.error("\tThat is not a valid choice")
        # TODO: call functions from depl and maint modules 
        elif operation == 1:
            print "Bootstrap Deployer"
        elif operation == 2:
            print "Generate SSH Config File"
        elif operation == 3:
            print "Copy Deployer Key to All Nodes"
        elif operation == 4:
            print "Test SSH Connectivity to All Nodes"
        elif operation == 5:
            print "Trunk Additional VLAN"
        elif operation == 6:
            print "Enable VLAN Spanning"
        elif operation == 7:
            print "Bootstrap Deployer"
        elif operation == 8:
            print "OS Reload Servers"

        return operation 

# TODO: finish running logic
runner = ToolRunner()
config = runner.get_config()
client = runner.get_client(config)
runner.get_choice()
