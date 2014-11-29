#!/usr/bin/env python
# coding=utf-8
# author:huhuhushan

from sys import argv
from os import makedirs, unlink, sep
from os.path import dirname, exists, isdir, splitext
from string import replace, find, lower
from htmllib import HTMLParser
from urllib import urlretrieve
from urlparse import urlparse, urljoin
from formatter import DumbWriter, AbstractFormatter
from cStringIO import StringIO

class Retriever(object): # download web pages
    def __init__(self, url):
        self.url = url
        self.file = self.filename(url)
        
    def filename(self, url, deffile='index.html'):
        parsedurl = urlparse(url, 'http:', 0) #parse path
        path = parsedurl[1] + parsedurl[2]
        ext = splitext(path)
        if ext[1] == '': #no file, use default
            if path[-1] == '/':
                path += deffile
            else:
                path += '/' + deffile
        ldir = dirname(path) #local directory
        print ldir + '#############'
        if sep != '/':
            #os-indep path seprator
            ldir = replace(ldir, '/', sep)
        if not isdir(ldir):     #create archive dir if nec.
            if exists(ldir):
                unlink(ldir)
            makedirs(ldir)
        print ldir
        return path

    def download(self):
        try:
            retval = urlretrieve(self.url, self.file)
        except IOError:
            retval = ('*** ERROR: invalid URL "%s"' %\
                     self.url,)
        return retval

    def parseAndGetLinks(self):
        # parse HTML, save links
        self.parser = HTMLParser(AbstractFormatter(\
            DumbWriter(StringIO())))
        self.parser.feed(open(self.file).read())
        self.parser.close()
        return self.parser.anchorlist

class Crawler(object):
    #mange entire crawling process
    count = 0         # static download page counter

    def __init__(self, url):
        self.q = [url]
        self.seen = []
        self.dom = urlparse(url)[1]

    def getPage(self, url):
        r = Retriever(url)
        retval = r.download()
        if retval[0] == '*':
            # error situation, do not parse
            return
        Crawler.count += 1
        print '\n(', Crawler.count, ')'
        print 'URL:', url
        print 'FILE:', retval[0]
        self.seen.append(url)

        links = r.parseAndGetLinks() # get and process links
        for eachlink in links:
            if eachlink[:4] != 'http' and \
               find(eachlink, '://') == -1:
                eachlink = urljoin(url, eachlink)
            print '*', eachlink

            if find(lower(eachlink), 'mailto:') != -1:
                print '....discarded, mailto link'
                continue
            
            if eachlink not in self.seen:
                if find(eachlink, self.dom) == -1:
                    print '....discarded not in domin'
                else:
                    if eachlink not in self.q:
                        self.q.append(eachlink)
                        print '..new added to Q'
                    else:
                        print '....discarded, already in Q'
            else:
                print '....discarded, already processed'

    def go(self):
        #process links in queue
        while self.q:
            url = self.q.pop()
            self.getPage(url)

def main():
    if len(argv) > 1:
        url = argv[1]
    else:
        try:
            url = raw_input('Enter starting URL: ')
        except (KeyboardInterrupt, EOFError):
            url = ''
            if not url:
                return 
        robot = Crawler(url)
        robot.go()

if __name__ == '__main__':
    main()