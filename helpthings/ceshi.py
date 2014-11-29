import urllib.request
import urllib.parse
import http.cookiejar

def GetUrlRequest(iUrl, iStrPostData):
	url = iUrl
	user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/30.0.1599.114 Chrome/30.0.1599.114 Safari/537.36'
	values = {'Submit':'%C8%AB%B2%BF%E4%AF%C0%C0','ZC':'11','XQ':'%D2%BB%D0%A3%C7%F8'}
	headers = {'User-Agent':user_agent}

	data = urllib.parse.urlencode(iStrPostData).encode(encoding = 'UTF8')
	req = urllib.request.Request(url,data,headers)
	response = urllib.request.urlopen(req)
	the_page = response.read().decode('UTF8')
	return the_page

#cookie
cookie = http.cookiejar.CookieJar()
cookieProc = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookieProc)
urllib.request.install_opener(opener)

#login info
strLoginInfo = {
	'userName_label':'2011300020',
	'password_label':'wqnmlgb'
}
urlLogin = 'htte://self.nwpu.edu.cn'
print('登录结果：' + str(GetUrlRequest(urlLogin, strLoginInfo)))