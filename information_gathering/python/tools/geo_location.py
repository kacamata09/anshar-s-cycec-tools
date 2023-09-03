import requests
import json


def argument(parser):
    'argument from geo location'
    parser.add_argument(
        "-gl", "--geoloc", action="store_true", help="Add geo location each ipv4 address, this works if use information gathering number two"
    )


def get_geoloc(ip):
        'Function get geo location from ip'
        
        ### info ip_address
        url_geo = f'https://ipinfo.io/{ip}/json'
        resp_geo = requests.get(url_geo)
        geolocation = resp_geo.json()
        
        for key, value in geolocation.items():
            # geolocation[i]
            print(f"        {key} : {value}")
        
        return geolocation

        # url_geo = f'https://geolocation-db.com/jsonp/{ip}'
        # resp_geo = requests.get(url_geo)
        # geolocation = resp_geo.content.decode()
        # geolocation = geolocation.split("(")[1].strip(")")
        # print(json.loads(geolocation))
