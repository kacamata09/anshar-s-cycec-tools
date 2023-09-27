import requests

def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        if response.status_code == 200:
            data = response.json()
            return data['ip']
        else:
            return "Gagal mendapatkan IP publik."
    except Exception as e:
        return str(e)

public_ip = get_public_ip()
print("IP Publik Anda adalah:", public_ip)
