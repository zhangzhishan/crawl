import urllib.request
import re
f = urllib.request.urlopen('http://jpkc.nwpu.edu.cn/jpkc2005/03/jiaoxueziyuan-006-002.asp')
regex = r'\d+'
line = str(f.read())
fp = open('1.html','w')
fp.write(line)
fp.close()

reobj = re.compile(regex)
match = reobj.search(line)
if match:
	result = match.group()
for i in range(1,400):
	f = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'%result)
	regex = r'\d+'
	line = str(f.read())
	reobj = re.compile(regex)
	match = reobj.search(line)
	if match:
		result = match.group()
	print(result)



