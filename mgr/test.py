import requests

def send_get_request(url):
    try:
        # 发送GET请求
        response = requests.get(url)
        # 检查响应状态码
        response.raise_for_status()
        # 解析JSON格式的响应数据
        data = response.json()
        # 打印响应数据
        print(data)
    except requests.exceptions.RequestException as e:
        # 处理请求异常
        print("Error:", e)

# 定义请求的URL
url = 'http://127.0.0.1/api/mgr/orders?action=list_order'

# 发送GET请求并打印响应数据
send_get_request(url)



