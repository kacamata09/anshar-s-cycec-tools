import socket
import argparse


def add_arg():
    'Add argument in python execute'
    parser = argparse.ArgumentParser(description="-----ip_checker help-----")

    parser.add_argument(
        "-u", "--url", action="store", help="Add url or domain"
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="See version from ip_checker",
        version="ip_checker version : 0.1",
    )

    args = parser.parse_args()

    if args.url == None:
        print(
            """------------------------SHOULD ADD DOMAIN---------------------------
You should add domain with argument -u <DOMAIN> atau --url <DOMAIN>
or show HELP with argument -h"""
        )
    else:
        ip_checker(args.url)


def ip_checker(domain):
    'Function return ipv4 from domain'
    # ipv4 = socket.gethostbyname(domain)
    # print(f"domain : {domain}")
    # print(f"ipv4 : {ipv4}")


    ### ipv4 addresses
    # ip = socket.getaddrinfo(domain, None)
    ip_addresses = socket.getaddrinfo(domain, port=None)
    ip_addresses = socket.getaddrinfo(domain, port=None, family=socket.AF_INET)
    arr_ipv4 = [ip[4][0] for ip in ip_addresses]
    print(f'Domain : {domain}')
    print('List ipv4 :')
    for ip in arr_ipv4:
        print(f'    - {ip}')


if __name__ == "__main__":
    add_arg()
