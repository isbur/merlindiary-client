import requests
from bs4 import BeautifulSoup

# test session
s = requests.Session()

r = s.get("http://merlindiary.ru/login")
soap = BeautifulSoup(r.text, 'html.parser')
print(r)

r = s.post("http://merlindiary.ru/site/logout")
print(r)

headers = {
    "Content-Type":"application/x-www-form-urlencoded"
}
payload = {
    "postData": {
        "mimeType": "application/x-www-form-urlencoded",
        "params": [
            {
                "name": "LoginForm[username]",
                "value": "oim177"
            },
            {
                "name": "LoginForm[password]",
                "value": "merlin010"
            }
        ]
    }
}
r = s.post("http://merlindiary.ru/login", headers = headers, json=payload)
soap = BeautifulSoup(r.text, 'html.parser')
print(r)

[print(attr, i) for attr, i in r.request.__dict__.items()]
[print(attr, i) for attr, i in r.request.body.request.__dict__.items()]