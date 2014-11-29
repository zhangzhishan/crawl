#!/usr/bin/python
# -*- coding: ascii -*-

#import os
#import subprocess
#baidu = r'I:\Users\sbsb\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\???\?????.lnk'
#baidu2 = r'I:\Users\sbsb\AppData\Roaming\Microsoft\Windows\"Start Menu"\Programs\???\?????.lnk'
#file = r'I:\Users\sbsb\Desktop\ReadMe.txt'
#baidu3 = 'dir'
##ps = subprocess.Popen(baidu, shell = True)
##status = subprocess.call(baidu3,shell = True)
##ps.wait()
##os.system(baidu2)
##os.system('dir')
##os.system()
#for t in range(2):
#	pid = os.fork()
#	print('-')
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'

