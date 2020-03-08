import unittest
from bs4 import BeautifulSoup
import requests



class TestMerlinSession(unittest.TestCase):

    def test_main(self):
        self.assertEqual(
            requests.get("http://merlindiary.ru").status_code,
            200
        )
    
    def test_login(self):
        s = requests.Session()
        r1 = s.get("http://merlindiary.ru/login")
        soap = BeautifulSoup(r1.text, 'html.parser')

        data = {
            "_csrf": soap.input['value'],
            "LoginForm[username]":"oim177",
            "LoginForm[password]":"merlin010"
        }

        r2 = s.post("http://merlindiary.ru/login", data = data)
        self.assertEqual(
            r2.status_code,
            200
        )