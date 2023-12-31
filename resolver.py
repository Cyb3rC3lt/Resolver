#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys
import os

class Resolver:

 # Process a file
 if (os.path.isfile(sys.argv[1])):

    with open(sys.argv[1]) as ips:
     nonblankips = filter(None, (ip1.rstrip() for ip1 in ips))
     for ip in nonblankips:
        ip = ip.rstrip('\n')
        cmd = "nslookup " + ip
        try:
          nslookup = subprocess.run(
              ["sh", "-c", cmd],
              text=True,
              stdout=subprocess.PIPE,
              check=True)
        except subprocess.CalledProcessError as e:
          print('{} : {}'.format(ip, "Unable to resolve this IP"))
          continue
        
        nslookup = nslookup.stdout.split('\n')
        hostnamesplit = nslookup[0].split('=')
        hostname = hostnamesplit[1][:len(hostnamesplit[1])-1] 
        print('{} : {}'.format(ip, hostname))  
 
 # Process single IPs  
 else:
    for ip in sys.argv[1:]:
        cmd = "nslookup " + ip
        try:
          nslookup = subprocess.run(
              ["sh", "-c", cmd],
              text=True,
              stdout=subprocess.PIPE,
              check=True)
        except subprocess.CalledProcessError as e:
          print('{} : {}'.format(ip, "Unable to resolve this IP"))
          continue

        nslookup = nslookup.stdout.split('\n')
        hostnamesplit = nslookup[0].split('=')
        hostname = hostnamesplit[1][:len(hostnamesplit[1])-1]
        print('{} : {}'.format(ip, hostname))
