from email import header
import requests

# 转换用resp.encode('utf-8')
query = input()
url = f'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd={query}'

dic ={
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
}
resp = requests.get(url,headers=dic)

print(resp)
with open("result.html", mode="w", encoding="utf-8") as f:
    f.write(resp.text)#拿到网页源代码
