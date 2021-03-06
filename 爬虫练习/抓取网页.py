# -*- coding: utf-8 -*-
import requests
import re
import json
import time
from requests.exceptions import RequestException 

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        #print(response.status_code)
        return None
    except RequestException:
        
        return None
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
    response = requests.get(url,headers = headers)
    if response.status_code==200:
        return response.text
    return None
    '''

def parse_one_page(html):
    my_re ='<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>'
    items = re.findall(my_re,str(html),re.S)
    for item in items:
        yield{
                'index': item[0],
                'image': item[1],
                'title': item[2],
                'actor': item[3].strip()[3:],
                'time': item[4].strip()[5:],
                'score': item[5] + item[6]
                }
        

def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_acsii=False+'/n'))

def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    #print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__=='__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)
'''
'<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>'
'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>'
'''