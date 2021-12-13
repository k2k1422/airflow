import requests

URL = 'https://httpbin.org/uuid'


def fetch_data(url, no_of_request):
    for _ in range(no_of_request):
        with requests.get(url) as response:
            print(response.json()['uuid'])