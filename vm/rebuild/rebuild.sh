#!/usr/bin/env bash
# author - david
# Script for use _after_ rebuilding VMs

# help msg
if [[ ("$#" -eq 1) && ("$1" == "-h")  ]]; then
  echo "Script for use _after_ rebuilding VMs"
  echo "Usage:"
  echo "./rebuild.sh (-p) IP1 IP2 IP3"
  echo "  -p - used if you're doing package install,"
  echo "       will retrieve all packages on provided IPs."
  echo "  -h - with no IPs will display this text."
  exit 0
fi

# num of args check
# if less than 4 args and the first is -p then bad news
if [[ "$#" -lt 4 && "$1" == "-p" ]]; then
  echo "Argument error, not enough IPs provided"
  echo "Correct usage: \"./rebuild.sh (-p) IP1 IP2 IP3\""
  exit 1
fi

# if greater than 3 and no -p bad news
if [[ "$#" -gt 3 && "$1" != "-p" ]]; then
  echo "Error with arguments. Please provide the IP addresses associated with your nodes."
  echo "Correct usage: \"./rebuild.sh (-p) IP1 IP2 IP3\""
  exit 1
fi

# valid IP check
for arg in "$@"
do
  if ! [[ "$arg" =~  ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]] && [[ "$arg" != "-p" ]]; then
    echo "$arg is not an IP address."
    exit 1
  fi
done

# Allow for unauthenticated packages
for arg in "$@"
do
  if [[ "$arg" != "-p" ]]; then
    ssh-keygen -R "$arg"
    if [[ "$1" == "-p" ]]; then
      ssh "$arg" bash -c "'echo \"APT::Get::AllowUnauthenticated \"true\";\" >> /etc/apt/apt.conf.d/99myauth; apt-get update;'"
    fi
  fi
done
