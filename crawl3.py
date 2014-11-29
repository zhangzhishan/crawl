#!/usr/bin/env python
# coding=utf-8
# author:huhuhushan

from sys import argv
from os import makedirs, unlink, sep
from os.path import dirname, exists, isdir, splitext
from urllib.request import urlretrieve, urlopen
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from time import sleep

class Retriever(object): # download web pages
    def __init__(self, url):
        self.url = url
        self.file = self.filename(url)
        
    def filename(self, url, deffile='index.html'):
        parsedurl = urlparse(url, 'http:', 0) #parse path
        print(parsedurl)
        path = parsedurl[1] + parsedurl[2] +'/'
        print(path)
        ext = splitext(path)
        print(ext)
        print(path[-1])
        if ext[1] == '': #no file, use default
            if path[-1] == '/':
                path += deffile
            else:
                path += '/' + deffile

        print(path)

        ldir = dirname(path) #local directory
        print(ldir + '#############')
        if sep != '/':
            #os-indep path seprator
            ldir.replace('/', sep)
            #ldir = replace(ldir, '/', sep)
        if not isdir(ldir):     #create archive dir if nec.
            if exists(ldir):
                unlink(ldir)
            makedirs(ldir)
        print(ldir)
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
        try:
            urlop = urlopen(self.url, timeout = 2)
            data = urlop.read().decode('utf-8', 'ignore')
            soup = BeautifulSoup(data)
            links = []
            for link in soup.find_all('a'):
                print(link)
                #print('why you can go in ^^^^^^',link.get('href'))
                if link.get('href'):
                    #print('here get the href',link.get('href'))
                    if link.get('href')[:10] != 'javascript' and link.get('href') != '#':
                        links.append(link.get('href'))

            print(links)
            return links
        except:
            print('****bad url:')
            print(self.url)
            sleep(1)
        #self.parser = HTMLParser(AbstractFormatter(\
            #DumbWriter(StringIO())))
        #print(type(open(self.file, encoding="utf-8")))
        #self.parser.feed(open(self.file, encoding="utf-8").read())
        #self.parser.close()
        #return self.parser.anchorlist

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
        print('\n(', Crawler.count, ')')
        print('URL:', url)
        print('FILE:', retval[0])
        self.seen.append(url)

        links = r.parseAndGetLinks() # get and process links
        if links == '':
            return
        for eachlink in links:
            if eachlink[:4] != 'http' and \
               eachlink.find('://') == -1:
                eachlink = urljoin(url, eachlink)
            print('*', eachlink)

            if eachlink.lower().find('mailto:') != -1:
                print('....discarded, mailto link')
                continue
            
            if eachlink not in self.seen:
                if eachlink.find(self.dom) == -1:
                    print('....discarded not in domin')
                else:
                    if eachlink not in self.q:
                        self.q.append(eachlink)
                        print('..new added to Q')
                    else:
                        print('....discarded, already in Q')
            else:
                print('....discarded, already processed')

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
            url = input('Enter starting URL: ')
        except (KeyboardInterrupt, EOFError):
            url = ''
            if not url:
                return
        if url[:4] != 'http':
            url = 'http://' + url
        robot = Crawler(url)
        robot.go()

if __name__ == '__main__':
    main()
