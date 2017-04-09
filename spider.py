from urllib.request import urlopen
from linkFinder import LinkFinder
from webCrawler import *

class Spider:
    # Class variables (Shared among all instances)
    projectName = ''
    baseUrl = ''
    domainName = ''
    queueFile = ''
    crawledFile = ''
    queueSet = set()
    crawledSet = set()

    def __init__(self, projectName, baseUrl, domainName):
        Spider.projectName = projectName
        Spider.baseUrl = baseUrl
        Spider.domainName = domainName
        Spider.queueFile = Spider.projectName + '/queue.txt'
        Spider.crawledFile = Spider.projectName + '/crawled.txt'
        self.boot()
        self.crawlPage('First spider', Spider.baseUrl)

    #convention for static methods
    @staticmethod
    def boot():
        createProjectDirectory(Spider.projectName)
        createDataFiles(Spider.projectName, Spider.baseUrl)
        Spider.queue = fileToSet(Spider.queueFile)
        Spider.crawled = fileToSet(Spider.crawledFile)

    @staticmethod
    def crawlPage(threadName, pageUrl):
        if pageUrl not in Spider.crawled:
            print(threadName + ' now crawling ' + pageUrl)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            Spider.addLinksToQueue(Spider.gatherLink(pageUrl))
            Spider.queue.remove(pageUrl)
            Spider.crawled.add(pageUrl)
            Spider.updateFiles()

    @staticmethod
    def gatherLink(pageUrl):
        htmlString = ''
        try:
            response = urlopen(pageUrl)
            if response.getheader('Content-Type') == 'text/html':
                htmlBytes = response.read()
                htmlString = htmlBytes.decode("utf-8")
            finder = LinkFinder(Spider.baseUrl, pageUrl)
            finder.feed(htmlString)
        except:
            print('Error: Can not crawl page')
            return set()
        return finder.pageLinks()

    @staticmethod
    def addLinksToQueue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domainName not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def updateFiles():
        setToFile(Spider.queue, Spider.queueFile)
        setToFile(Spider.crawled, Spider.crawledFile)
