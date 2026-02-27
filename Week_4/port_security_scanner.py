devices = [ 
("192.168.1.10", [22, 80, 443]),
("192.168.1.11", [21, 22, 80]), 
("192.168.1.12", [27, 80, 3389]),
("192.168.1.13", [30, 80, 2385]),
("192.168.1.14", [31, 80, 3974]),
("192.168.1.15", [23, 80, 109]),
("192.168.1.16", [20, 80, 1347]),
("192.168.1.17", [15, 80, 355]),
]

risky_ports = [21, 23, 3389]

total_risks = 0

print(f"Would you like to run Port Checker?")
proceed = input("Please type 'YES' to run: ")
if proceed == "YES":
    print(f'Scanning network devices...')
    
    for ips, ports in devices:
        for port in ports:
            if port in risky_ports:
                print(f"WARNING:", ips, "has", port, "open!")
                total_risks += 1    
    print(f"Total risky ports open: {total_risks}")
    print(f'Port Checker complete. Exiting...')

else: 
    print(f'Exiting...')