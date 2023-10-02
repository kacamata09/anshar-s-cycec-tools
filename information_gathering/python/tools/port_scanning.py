import socket

def port_checker(port):
    # global target_host
    result = client.connect_ex((target_host, port))
    if result == 0:
        print(f"Port {port} open at {target_host}")
    # else:
    #     print(f"Port {port} tertutup pada {target_host}")

target_host = input("Input IP Address target: ")

with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as client:
    while True:
        spam = input('Do you want spam? y / n: ')
        if spam.lower() in ('n', 'no'):
            target_port = int(input("Port target: "))
            port_checker(target_port)
            break
        elif spam.lower() in ('y', 'yes'):
            min_port = int(input("Min port target: "))
            max_port = int(input("Max port target: "))
            port_range = range(min_port, max_port)

            # timeout = 2
            for port in port_range:
                port_checker(port)
            break
        else:
            print("Please type y / n")

