from PAM30 import PAMIE
ie = PAMIE()
s = 40
while s :
	s = str(s)
	ie.navigate('http://jpkc.nwpu.edu.cn/jpkc2005/03/resources2014/PPT88/%%E6%%8E%%A7%%E5%%88%%B688-%s.ppt'%s)
	s =int(s)
	s-=1
# ie.navigate(r'http://jpkc.nwpu.edu.cn/jpkc2005/03/resources2014/PPT88/%E6%8E%A7%E5%88%B688-02.ppt')
# ie.navigate(r'http://jpkc.nwpu.edu.cn/jpkc2005/03/resources2014/PPT88/%E6%8E%A7%E5%88%B688-03.ppt')
# ie.navigate(r'http://jpkc.nwpu.edu.cn/jpkc2005/03/resources2014/PPT88/%E6%8E%A7%E5%88%B688-04.ppt')
# ie.navigate(r'http://jpkc.nwpu.edu.cn/jpkc2005/03/resources2014/PPT88/%E6%8E%A7%E5%88%B688-05.ppt')
# ie.navigate(r'http://jpkc.nwpu.edu.cn/jpkc2005/03/resources2014/PPT88/%E6%8E%A7%E5%88%B688-06.ppt')
# ie.navigate(r'http://jpkc.nwpu.edu.cn/jpkc2005/03/resources2014/PPT88/%E6%8E%A7%E5%88%B688-07.ppt')
# ie.navigate(r'http://jpkc.nwpu.edu.cn/jpkc2005/03/resources2014/PPT88/%E6%8E%A7%E5%88%B688-08.ppt')
# ie.navigate(r'http://jpkc.nwpu.edu.cn/jpkc2005/03/resources2014/PPT88/%E6%8E%A7%E5%88%B688-09.ppt')
#print ie.cookieGet()
# ie.buttonExists('btnSure')
# ie.setTextBox('zjh','2011300020')
# ie.setTextBox('mm','dq012369')
# ie.clickButton('btnSure')
# ie.navigate('http://jw.nwpu.edu.cn/jxpgXsAction.do?oper=listWj')
# #ie.executejavaScript("javascript:submitMe()") 
# ie.clickButtonImage(u'0000000076#@1989000019#@吴立言#@学生课堂教学评价问卷#@机械原理与设计#@0520130')