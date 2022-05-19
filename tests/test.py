import requests
import json

def test(url):
    req = requests.get(url)
    print(req.json()['result'])

if __name__ == "__main__":
    test("http://127.0.0.1:5000/?name=Nikolay&age=25")
    test("http://127.0.0.1:5000/?name=Sam&age=77")
    test("http://127.0.0.1:5000/?name=Ila&age=18")
    test("http://127.0.0.1:5000/?name=Nil&age=9")
    test("http://127.0.0.1:5000/?name=Olaf&age=10")