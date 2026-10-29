import requests
url = "http://127.0.0.1:8000/product"
data = {'name': 'gun', 'price': 500, 'stock':20}
r=  requests.post(url, json=data)
print (r.json())
