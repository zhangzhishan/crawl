#! /usr/bin/env python3

import urllib.parse
import urllib.request

url = 'http://www.renren.com'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {
'act' : 'login',
'login[email]' : 'yzhang@i9i8.com',
'login[password]' : '123456'
}
headers = { 'User-Agent' : user_agent }

data = urllib.parse.urlencode(values).encode(encoding = 'UTF8')
req = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(req)
the_page = response.read()

print(the_page.decode("utf8"))