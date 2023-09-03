import whois
# def argument(parser):
#     'argument from ip_checker'




def whois_check(domain) -> list:
    'Function return whois info from domain'
    info = whois.whois(domain)
    # print(info)
    for key, value in info.items():
        print(f'{key} : {value}')
    
   




