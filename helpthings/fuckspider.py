import urllib.request
import urllib
import re

from collections import deque

queque = deque()
visited = set()

url = "http://news.dbanotes.net" 
cnt = 0

while queque:
	url = queque.popleft()
	urlop = urllib.request.urlopen(url)
	visited |= {url}
	cnt += 1
	url
