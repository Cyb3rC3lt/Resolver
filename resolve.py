#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys
import os

class Lookup:

 if (os.path.isfile(sys.argv[1])):
    with open(sys.argv[1]) as ips:
     for ip in ips:
        ip = ip.rstrip('\n')
        cmd = "nmblookup -A " + ip + "| sed -n 2p | cut -d ' ' -f1 | xargs"
        nmblookup = subprocess.run(
            ["sh", "-c", cmd],
            text=True,
            stdout=subprocess.PIPE,
            check=True)
        hostname = nmblookup.stdout.split('\n')
        print('{} : {}'.format(ip, hostname[0]))

 else:
    for ip in sys.argv[1:]:
        cmd = "nmblookup -A " + ip + "| sed -n 2p | cut -d ' ' -f1 | xargs"
        nmblookup = subprocess.run(
            ["sh", "-c", cmd],
            text=True,
            stdout=subprocess.PIPE,
            check=True)
        hostname = nmblookup.stdout.split('\n')
        print('{} : {}'.format(ip, hostname[0]))
