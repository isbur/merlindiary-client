from bs4 import BeautifulSoup
import requests


class Merlin:

    s = ""

    def __init__(self):
        self.s = requests.Session()


    def login(self):
        r1 = self.s.get("http://merlindiary.ru/login")
        soap = BeautifulSoup(r1.text, 'html.parser')

        data = {
            "_csrf": soap.input['value'],
            "LoginForm[username]":"oim177",
            "LoginForm[password]":"merlin010"
        }

        r2 = self.s.post("http://merlindiary.ru/login", data = data)

        return r2