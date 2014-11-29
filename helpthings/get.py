import http.cookiejar
import urllib.request
import os

header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0',
	'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate'
}
url = 'http://www.amazon.cn/'
cj = http.cookiejar.MozillaCookieJar()
cj.load(os.path.join(os.path.expanduser("~"), "AppData\Roaming\Mozilla\Firefox\Profiles\70o562vh.default\cookies.sqlite"))
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open(url)
urlop = urllib.request.urlopen(url, timeout = 8)
data = urlop.read().decode('utf-8')
# data = data.encoding('utf-8')
print(data)