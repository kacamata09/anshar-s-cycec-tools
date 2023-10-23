import socket

def port_checker(port, target_host, client):
    result = client.connect_ex((target_host, port))
    print(result )
    if result == 0:
        print(f"Port {port} open at {target_host}")
    # else:
    #     print(f"Port {port} tertutup pada {target_host}")


def port_scan(domain):
    print(domain)
    # ip_address = socket.getaddrinfo(domain, port=None, family=socket.AF_INET)
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as client:
        while True:
            spam = input('Do you want spam? y / n: ')
            if spam.lower() in ('n', 'no'):
                target_port = int(input("Port target: "))
                port_checker(target_port, domain, client)
                break
            elif spam.lower() in ('y', 'yes'):
                min_port = int(input("Min port target: "))
                max_port = int(input("Max port target: "))
                port_range = range(min_port, max_port)
                # timeout = 2
                print(port_range)
                for port in port_range:
                    port_checker(port, domain, client)
                break
            else:
                print("Please type y / n")

