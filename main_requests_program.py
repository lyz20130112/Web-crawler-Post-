from email import header
import requests
import datetime  # 用于获取当前时间


# 询问用户选择日志语言
while True:
    lang_choice = input("请选择日志语言（1-中文，2-英文）：")
    if lang_choice in ["1", "2"]:
        break
    print("输入无效，请重新选择（1或2）")


query = input("请输入搜索关键词：")
url = f'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd={query}'

dic = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

resp = requests.get(url, headers=dic)

print(f"响应状态码：{resp.status_code}")

# 保存搜索结果到result.html
with open("result.html", mode="w", encoding="utf-8") as f:
    f.write(resp.text)


# 生成对应语言的日志内容
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
if lang_choice == "1":
    # 中文日志
    log_info = f"[{current_time}] 搜索关键词：{query}，响应状态码：{resp.status_code}，请求成功\n"
else:
    # 英文日志
    log_info = f"[{current_time}] Search keyword: {query}, Response status code: {resp.status_code}, Request successful\n"


# 追加写入日志到log.txt
with open("log.txt", mode="a", encoding="utf-8") as log_f:
    log_f.write(log_info)

print("日志已记录到log.txt")
