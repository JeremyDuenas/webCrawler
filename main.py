import threading
from queue import Queue
from spider import Spider
from domain import *
from webCrawler import *

PROJECT_NAME = 'thenewboston'
HOMEPAGE = 'https://thenewboston.com/'
DOMAIN_NAME = getDomainName(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8

queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawlPage(threading.current_thread().name, url)
        queue.task_done()

# Create worker threads (will die when main exits)
def createWorkers():
    for _ in range(NUMBER_OF_THREADS): #_ = disregards value
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Each queued link is a new job
def createJobs():
    for link in fileToSet(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# check if there are items in the queue, if so crawl them
def crawl():
    queuedLinks = fileToSet(QUEUE_FILE)
    if len(queuedLinks) > 0:
        print(str(len(queuedLinks)) + ' links in the queue')
        createJobs()

createWorkers()
crawl()
