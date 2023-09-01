import socket
import argparse
import requests
import json

def add_arg():
    'Add argument in python execute'
    parser = argparse.ArgumentParser(description="-----ip_checker help-----")

    parser.add_argument(
        "-u", "--url", action="store", help="Add url or domain"
    )

    parser.add_argument(
        "-gl", "--geoloc", action="store_true", help="Add geo location each ipv4 address"
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
        try:
            ip_checker(args.url, args.geoloc)
        except socket.gaierror:
            print('----------- =========  ERROR DOMAIN  ========= -----------')
            print('Domain you entered maybe wrong, please enter correct domain')



def ip_checker(domain, geoloc):
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
        if geoloc:
            get_geoloc(ip)

        

def get_geoloc(ip):
        'Function get geo location from ip'
        ### info ipaddr
        url_geo = f'https://ipinfo.io/{ip}/json'
        resp_geo = requests.get(url_geo)
        geolocation = resp_geo.json()
        
        for key, value in geolocation.items():
            # geolocation[i]
            print(f"        {key} : {value}")

        # url_geo = f'https://geolocation-db.com/jsonp/{ip}'
        # resp_geo = requests.get(url_geo)
        # geolocation = resp_geo.content.decode()
        # geolocation = geolocation.split("(")[1].strip(")")
        # print(json.loads(geolocation))




if __name__ == "__main__":
    add_arg()
