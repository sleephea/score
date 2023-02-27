import requests


def SubmitUnitData(formData, cookie):
    base_url = "http://103.239.153.109/sdjyweb/proxy/qdaio-ggjy/d3/d32501/updateHc40"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "Cookie": cookie,
    }

    response = requests.post(base_url, headers=headers, data=formData)  # 发送请求，并返回数据
    print(response.text)
    return response.text
