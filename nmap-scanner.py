import nmap

def main():
    print("==== Advanced Python Nmap Scanner ====")
    ip = input("Enter IP to scan: ")

    # Create scanner object
    nm = nmap.PortScanner()

    print(f"\nScanning {ip}...\n")

    # Scan ports 1–1024 with version detection
    nm.scan(ip, '1-1024', '-sV')

    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()

            for port in sorted(ports):
                port_info = nm[host][proto][port]
                print(f"[+] Port {port} ({port_info['name']}) is {port_info['state']} — Service: {port_info.get('product', 'Unknown')}")


if __name__ == "__main__":
    main()
