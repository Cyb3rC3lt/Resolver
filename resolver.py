import socket
import argparse

def resolve(value):
    try:
        if value.replace(".", "").isdigit():  # Simple check for an IP address
            hostname = socket.gethostbyaddr(value)[0]
            print(f"{value} -> {hostname}")
        else:
            ip = socket.gethostbyname(value)
            print(f"{value} -> {ip}")
    except (socket.gaierror, socket.herror):
        print(f"{value} -> Unable to resolve")

def resolve_from_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            value = line.strip()
            if value:
                try:
                    if value.replace(".", "").isdigit():
                        hostname = socket.gethostbyaddr(value)[0]
                        outfile.write(f"{value},{hostname}\n")
                    else:
                        ip = socket.gethostbyname(value)
                        outfile.write(f"{value},{ip}\n")
                except (socket.gaierror, socket.herror):
                    outfile.write(f"{value},Unable to resolve\n")

def main():
    parser = argparse.ArgumentParser(description="Resolve hostnames to IP addresses and vice versa.")
    parser.add_argument("value", nargs="?", help="Single hostname or IP to resolve.")
    parser.add_argument("-i", "--input", help="Input file containing hostnames or IPs.")
    parser.add_argument("-o", "--output", help="Output file for resolved results.")
    args = parser.parse_args()
    
    if args.value:
        resolve(args.value)
    elif args.input and args.output:
        resolve_from_file(args.input, args.output)
    else:
        print("Error: Provide either a single value or both -i and -o for file processing.")

if __name__ == "__main__":
    main()
