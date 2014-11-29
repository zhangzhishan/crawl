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

url = "http://news.dbanotes.net"#http://news.dbanotes.net/

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

	linkre = re.compile(r'class="title".+?href="(.+?)"')
	for x in linkre.findall(data):
		if 'http' in x and x not in visited:
		    queue.append(x)
		    print('加入队列---->' + x)


