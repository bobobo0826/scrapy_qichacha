
import urllib.request
import re

def getProxy():
    httpproxy_handler = urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(httpproxy_handler)
    url = "http://192.168.117.96:5010/get/"

    # url="http://api.ip.data5u.com/dynamic/get.html?order=facac5444919f53d283037d813d3bc83&sep=3"
    req = urllib.request.Request(url=url)
    response = opener.open(req)
    ips = response.read().decode('utf8').replace("\n", "")
    # print("ips=============", ips)
    return ips
