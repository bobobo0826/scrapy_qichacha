from urllib import request as request
import datetime
import requests

# 构建了两个代理Handler，一个有代理IP，一个没有代理IP
httpproxy_handler = request.ProxyHandler({"http": "212.22.86.107:3130"})
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3128.0 Mobile Safari/537.36'
}
# 定义一个代理开关
proxySwitch = True
# 通过 request.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
# 根据代理开关是否打开，使用不同的代理模式
opener = request.build_opener(httpproxy_handler)

start_time = datetime.datetime.now()  # 开始训练计时
url = "https://www.qichacha.com/gongsi_area.shtml?prov=AH&p=3"
req = request.Request(url, headers=headers)

# 使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理。
try:
    response = opener.open(req)
    print(response.read())
except Exception as e:
    print("网址打开失败", e)


# 就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
# urllib2.install_opener(opener)
# response = urlopen(request)

end_time = datetime.datetime.now()  # 开始训练计时
print((end_time-start_time).seconds, " seconds")

