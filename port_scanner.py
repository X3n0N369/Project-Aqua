import socket


def scan_port(target_ip, port):
    try:
       
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)  # Timeout for connection attempt
        
       
        result = s.connect_ex(('https://zkzfrghv.eu2.ctfio.com/', port))
        if result == 0:  # If successful
            print(f"Port {port} is OPEN")
            
        s.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")


target = 'https://zkzfrghv.eu2.ctfio.com/' 
ports = range(20, 1025)  

print(f"Scanning {target}...\n")
for port in ports:
    scan_port(target, port)