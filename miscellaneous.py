from bs4 import BeautifulSoup


def beautify(r):
    '''
    :param r (result of requests.get())
    '''
    return BeautifulSoup(r.text, "html.parser")


def get_properties(obj):
    [print(attr) for attr, i in obj.__dict__.items()]


def get_csrf_token(r):
    return beautify(r).find_all(name="meta", attrs={"name":"csrf-token"})[0]['content']


def sprint(obj):
    [print(attr, i) for attr, i in obj.__dict__.items()]
