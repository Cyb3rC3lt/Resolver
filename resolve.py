#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys
import os

class Lookup:

 if (os.path.isfile(sys.argv[1])):
    with open(sys.argv[1]) as hosts:
     for host in hosts:
        host = host.rstrip('\n')
        cmd = "nmblookup -A " + host + "| sed -n 2p | cut -d ' ' -f1 | xargs"
        nmblookup = subprocess.run(
            ["sh", "-c", cmd],
            text=True,
            stdout=subprocess.PIPE,
            check=True)
        split = nmblookup.stdout.split('\n')
        print('{} : {}'.format(host, split[0]))

 else:
    for host in sys.argv[1:]:
        cmd = "nmblookup -A " + host + "| sed -n 2p | cut -d ' ' -f1 | xargs"
        nmblookup = subprocess.run(
            ["sh", "-c", cmd],
            text=True,
            stdout=subprocess.PIPE,
            check=True)
        split = nmblookup.stdout.split('\n')
        print('{} : {}'.format(host, split[0]))