from email import header
import requests

query = input()
url = f'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd={query}'

dic ={
    'user-agent' : 'your user-agent'
}
resp = requests.get(url,headers=dic)

print(resp)
with open("result.html", mode="w", encoding="utf-8") as f:
    f.write(resp.text)
