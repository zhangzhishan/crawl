import urllib.request
import http.cookiejar
import os
import gzip
import re

# head: dict of header
url = 'http://www.zhihu.com/'
def getXSRF(data):
    cer = re.compile('name="_xsrf" value="(.*)"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]

def ungzip(data):
    try:
        data = gzip.decompress(data)
        print("ok")
    except :
        print("no")
    return data
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
    'Accept-Encoding': 'gzip. deflate'
}

opener = gerOpener(header)
uop = opener.open(url, timeout = 1000)
data = uop.read()
data = ungzip(data)
_xsrf = getXSRF(data.decode())
url += 'login'
id = ''
password = ''
postDict = {
    '_xsrf': _xsrf,
    'email': id,
    'password': password,
    'rememberme': 'y'
}
postData = urllib.parse.urlencode(postDict).encode()
uop = opener.open(url, postData)
data = uop.read()
data = ungzip(data)

print(data.decode())
