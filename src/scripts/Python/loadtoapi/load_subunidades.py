import requests


url = 'http://localhost:5000/liveapi/v01/subunidade/'
r = requests.get(url)
dados = r.json()
total = len (dados)

for i in dados:
    post_url = "http://127.0.0.1:5000/api/v01/subunidade/"+i["codigo"]
    print (i)
    response = requests.post(post_url, data=i)
    print (post_url)
    print (response)
    print (response.json())
