#encoding: 'UTF-8'
import re
import urllib.request
import urllib


from collections import deque

def saveFile(data,savepath):	
	f_obj = open(savepath, 'w')
	f_obj.write(data)
	f_obj.close()

queue = deque()
visited = set()

index = "http://www.liaoxuefeng.com"
url = "http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868200605560b1bd3c660bf494282ede59fee17e781000"#http://news.dbanotes.net/

queue.append(url)
cnt = 0
while queue:
	url = queue.popleft()
	visited |= {url}

	print('已经抓取：' + str(cnt) + '  正在抓取<---' + url)
	cnt += 1
	# urlop = urllib.request.urlopen(url, timeout = 2)
	try:
		urlop = urllib.request.urlopen(url, timeout = 2)
	except:
		continue	
	if 'html' not in urlop.getheader('Content-Type'):
	    continue
	try:
		# data = urlop.read().decode('UTF-8')
		data = urlop.read().decode('UTF-8')
		savepath = 'd:\\temp' + str(cnt) + '.kk'
		saveFile(data, savepath)
	except:
		continue

	# linkre = re.compile(r'class="title".+?href="(.+?)"')
	linkre = re.compile(r'<a href="(.+?)">')
	# print(linkre.findall(data))
	# linkre = index + linkre
	for x in linkre.findall(data):
		# print(x)
		if 'wiki' in x:
		    y = index + x
			# str(y)
		    if y not in visited:
		        queue.append(y)
		        # print('加入队列---->' + y)


