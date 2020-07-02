import requests
r = requests.get('https://www.s-m.com.sa/')
print(r.text)
print(r.content)