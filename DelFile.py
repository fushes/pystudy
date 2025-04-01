import requests, sys
url = 'https://2022.ipchaxun.com/'
proxy = {
    'http' : 'http://120.42.46.226:6666',
    'https' : 'http://120.42.46.226:6666'
}
try:
    response = requests.get(url, proxies=proxy, timeout=30)
    print(response.content.decode('utf-8'))
except requests.exceptions.ConnectionError:
    print('超时')