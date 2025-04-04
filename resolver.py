import socket
import argparse

def resolve(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            value = line.strip()
            if value:
                try:
                    # Determine if the input is a hostname or an IP
                    if value.replace(".", "").isdigit():  # Simple check for an IP address
                        hostname = socket.gethostbyaddr(value)[0]
                        outfile.write(f"{value},{hostname}\n")
                    else:
                        ip = socket.gethostbyname(value)
                        outfile.write(f"{value},{ip}\n")
                except (socket.gaierror, socket.herror):
                    outfile.write(f"{value},Unable to resolve\n")

def main():
    parser = argparse.ArgumentParser(description="Resolve hostnames to IP addresses and vice versa.")
    parser.add_argument("-i", "--input", required=True, help="Input file containing hostnames or IPs.")
    parser.add_argument("-o", "--output", required=True, help="Output file for resolved results.")
    args = parser.parse_args()
    
    resolve(args.input, args.output)

if __name__ == "__main__":
    main()
