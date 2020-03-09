from bs4 import BeautifulSoup

def login(s):
    r1 = s.get("http://merlindiary.ru/login")
    soap = BeautifulSoup(r1.text, 'html.parser')

    data = {
        "_csrf": soap.input['value'],
        "LoginForm[username]":"oim177",
        "LoginForm[password]":"merlin010"
    }

    r2 = s.post("http://merlindiary.ru/login", data = data)