# -*- coding: utf-8 -*-

import urllib.request

import urllib.parse

import socket
import urllib.error

import http.cookiejar




'''
response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))
print(type(response))


print(response.status)#返回结果的状态码,200表示请求成功,404表示页面未找到
print(response.getheaders())#返回响应的头信息
print(response.getheader('Server'))#获取了响应头中的Server值结果是nginx.意思是服务器是用Ngin搭建的
'''
'''
#data参数
#http://httpbin.org，它可以提供 HTTP 请求测试
data = bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post',data = data)
print(response.read())
'''
'''
#timeout参数
try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
'''

'''
#Request
request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
'''
'''
#Request
url ='http://httpbin.org/post'
headers ={
        'User-Agent':'Mozilla/4.0 (compatible; Mise 5.5; Windows NT)',
        'Host': 'httpbin.org'
        }
dict = {
        'name':'Germey'
        }
data = bytes(urllib.parse.urlencode(dict),encoding='utf8')
req = urllib.request.Request(url=url,data=data,headers=headers,method='POST')
#req = urllib.request.Request(url=url,data=data,method='POST')
#req.add_header( 'User-Agent','Mozilla/4.0 (compatible; Mise 5.5; Windows NT)')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
'''
'''
#验证
username = 'username'
password = 'password'
url = 'http://localhost:5000/'

p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auther_handler = urllib.request.HTTPBasicAuthHandler(p)
opener = urllib.request.build_opener(auther_handler)
5
try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except urllib.error.URLError as e:
    print(e.reason)
'''
'''
#代理
proxy_handler = urllib.request.ProxyHandler({
        'http':'http://127.0.0.1:9743',
        'https':'https://127.0.0.1:9743'
        })
opener = urllib.request.build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    print(e.reason)
'''
'''
#cookies
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name+" = "+item.value)
'''
'''
#将cookies保存到文件
filename = 'cookies.txt'
#cookie = http.cookiejar.MozillaCookieJar(filename)#将 Cookies 保存成 Mozilla 型 浏览器的 Cookies格式
cookie = http.cookiejar.LWPCookieJar(filename)#保存成 libwww-perl(LWP）格式的 Cookies 文件
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)
'''
#生成了 Cookies 文件后，怎样从文件中读取并利用
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))
