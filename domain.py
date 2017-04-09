from urllib.parse import urlparse

# get domain name (example.com)
def getDomainName(url):
    try:
        results = getSubDomainName(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''
# Get sub domain name (name.example.com)
def getSubDomainName(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
