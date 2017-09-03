# coding=utf-8
from re import search
from time import sleep
from urllib2 import build_opener
from sendemail import send
from config import options

# 个人中心url
url = 'https://campus.alibaba.com/myJobApply.htm'
while (True):
    opener = build_opener()
    opener.addheaders.append((
        'Cookie', options['cookies']
    ))

    res = opener.open(url)
    res = res.read().replace('\t', '').replace(' ', '').replace('\n', '')
    # 提取状态
    matches = search(r'<trclass=[\"\']content-new-top[\"\']>(.*?)</tr>', res)
    status = search(r'statusType=[\"\'](.*?)[\"\']', matches.group())

    if (status):
        status = status.group(1)
        if status != '面试中':
            send(status)
            break
        else:
            sleep(options['time'])
