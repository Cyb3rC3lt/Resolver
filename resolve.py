#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys
import os

class Resolver:

 if (os.path.isfile(sys.argv[1])):
    with open(sys.argv[1]) as ips:
     for ip in ips:
        ip = ip.rstrip('\n')
        cmd = "nslookup " + ip + " | awk '{print $4}' | sed 's/.$//'"
        nslookup = subprocess.run(
            ["sh", "-c", cmd],
            text=True,
            stdout=subprocess.PIPE,
            check=True)
        hostname = nslookup.stdout.split('\n')
        if ("fin" in hostname):
            print('{} : {}'.format(ip, "Unable to resolve this IP"))
        else:
            print('{} : {}'.format(ip, hostname[0]))
     sys.exit()
 else:
    for ip in sys.argv[1:]:
        cmd = "nslookup " + ip + " | awk '{print $4}' | sed 's/.$//'"
        nslookup = subprocess.run(
            ["sh", "-c", cmd],
            text=True,
            stdout=subprocess.PIPE,
            check=True)
        hostname = nslookup.stdout.split('\n')
        if ("fin" in hostname):
            print('{} : {}'.format(ip, "Unable to resolve this IP"))
        else:
            print('{} : {}'.format(ip, hostname[0]))
