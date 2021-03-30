# -*- coding: utf-8 -*-
import requests
import re
'''
#抓取网页
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
r = requests.get('https://www.zhihu.com/explore',headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles = re.findall(pattern,r.text)
print(titles)
'''
'''
#抓取二进制数据
try:
    r = requests.get('https://github.com/favicon.ico')
except requests.ConnectionError as e:
    print(e.reason)
else:
    print(r.text)
    print(r.content)
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)
'''
'''
#添加headers
#r = requests.get('https://www.zhihu.com/explore')
#print(r.text)
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
r = requests.get('https://www.zhihu.com/explore',headers=headers)
print(r.text)
'''
'''
#post请求
data = {'name':'germey','age':'22'}
r = requests.post('http://httpbin.org/post',data=data)
print(r.text)
'''
'''
#响应
r = requests.get('http://www.jianshu.com')
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)
print(type(r.history),r.history)
'''
'''
#高级应用————文件上传
files = {'file':open('favicon.ico','rb')}
r = requests.post('http://httpbin.org/post',files=files)
print(r.text)
'''
'''
#高级应用————Cookies
r = requests.get('https://www.baidu.com')
print(r.cookies)
for key,value in r.cookies.items():
    print(key,'=',value)
'''
'''
headers={
        
        'Cookie':'_zap=f54d873c-0954-4743-8774-7c5a44eda0af; _xsrf=6nlSKyVuzZGSI29XmgNqiEHitxm0TjII; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1581694470; d_c0="APBWxj0p0RCPTjE15K-GO7CyaiMbeoFeYSw=|1581694470"; capsion_ticket="2|1:0|10:1581694470|14:capsion_ticket|44:MzE5MTAzZDAxYWI0NGU2YmE2YmE3MzIwZGY3ZThkYWI=|0220a1cf11b90c4ef8d735bff8a4bf7108dee67c2e4642c92437fd23c465ddd8"; l_n_c=1; r_cap_id="YjdkOTYxMmM0YzUyNDViNGJlNjI4NmRiYjA0OWIyMWI=|1581694472|040d333f2888805e52abac851fb6cbedcb97b8ca"; cap_id="ZDA3NWViNDNjMzY4NDlkY2FiNmQxY2Y5MDlmMGNiNzg=|1581694472|0bddefe84ed8bc68a9bc3425f0b5e242f6040c1a"; l_cap_id="MWU0ZGZjMDFiMzY5NDY1NDk4NDRhZmNiNmQ1MDhlNWQ=|1581694472|96a0597df2666187bc537c572deb6050972f99c2"; n_c=1; z_c0=Mi4xb3VtYUNnQUFBQUFBOEZiR1BTblJFQmNBQUFCaEFsVk5EQXcwWHdBN2lnMnlkTlZMQW1aamhTZVRwdTJTRGFsYWZR|1581694476|ba16e11e76a35f75ace121243c12efbc36bdd0d1; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1581694478; KLBRSID=ca494ee5d16b14b649673c122ff27291|1581694479|1581694470',
        'Host':'www.zhihu.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
        }
r = requests.get('https://www.zhihu.com',headers=headers)
print(r.text)
'''
'''
#会话维持
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
'''
#代理设置
proxies = {
        'http':'socks5://user:password@host:port',
        'https':'socks5://user:password@host:port'
        }
requests.get('https://www.taobao.com',proxies=proxies)
