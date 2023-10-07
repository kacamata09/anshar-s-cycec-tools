import socket
from . import geo_location as geoloc

def ip_checker(domain, isgeoloc) -> list:
    'Function return ipv4 from domain'
    data = {}
    
    # ipv4 = socket.gethostbyname(domain)
    # print(f"domain : {domain}")
    # print(f"ipv4 : {ipv4}")

    ### ipv4 addresses
    # ip = socket.getaddrinfo(domain, None)
    # ip_addresses = socket.getaddrinfo(domain, port=None)
    ip_addresses = socket.getaddrinfo(domain, port=None, family=socket.AF_INET)
    arr_ipv4 = [ip[4][0] for ip in ip_addresses]
    print(f'Domain : {domain}')
    print('List ipv4 :')

    # data['domain'] = domain
    # data['list_info_ip'] = []

    for ip in arr_ipv4:
        print(f'    - {ip}')
        if isgeoloc:
            data_geo = geoloc.get_geoloc(ip)
            # data['list_info_ip'].append(data_geo)
    
    # return data
        




