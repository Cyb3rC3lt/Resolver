# Resolver
A simple Python utility to help you resolve internal IPs to Hostnames via the dns server in resolv.conf. It's just a wrapper around nslookup.

It can take a single IP, multiple IPs or a file of IPs.

`resolver.py 192.168.23.44`

`resolver.py 192.168.23.44 192.168.23.45`

`resolver.py targets.txt`


