import os

# every website crawled is a separate directory
def createProjectDirectory(directory):
    if not os.path.exists(directory):
        print('Creating project directory ' + directory)
        os.makedirs(directory)

# create a new file

def writeFile(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# create queue and crawled files

def createDataFiles(projectName, baseUrl):
    queue = projectName + '/queue.txt'
    crawled = projectName + '/crawled.txt'
    if not os.path.isfile(queue):
        writeFile(queue, baseUrl)
    if not os.path.isfile(crawled):
        writeFile(crawled, '')

# add data onto an existing file
def appendToFile(path,data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# delete the contents of a file
def deleteFileContents(path):
    with open(path, 'w'):
        pass

# read a file and convert each line to set items
def fileToSet(fileName):
    results = set()
    with open(fileName, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

# iterate through a set, each item will be a new line in the fileName
def setToFile(links, file):
    deleteFileContents(file)
    for link in sorted(links):
        appendToFile(file, link)
