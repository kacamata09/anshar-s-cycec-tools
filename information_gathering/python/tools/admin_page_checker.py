import requests

def admin_page_check(domain):
    'return if found admin page'
    admin_urls = [
        "admin/",
        "login/",
        "admin/login/",
        "administrator/",
        "admin-panel/",
        "wp-admin/",
        "wp-login.php/",
        "cpanel/",
        "c-panel/",
        "phpmyadmin/",
        "administrator/",
        "backend/"
    ]

    target_url = domain

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for admin_url in admin_urls:
        url_to_check = 'https://' + target_url + '/' + admin_url
        try:

            response = requests.get(url_to_check, headers=headers)
            # response = requests.get(url_to_check)

            if response.status_code == 200:
                print(f"Admin page found: {url_to_check}")
            else:
                print(f"Not found: {url_to_check}")
            
        except requests.ConnectTimeout:
            print(f'Connection to domain {domain} timed out...')
            exit(0)

