from bs4 import BeautifulSoup
import urllib2
from urllib2 import urlopen
# from urllib2 import requests
import random


def LoadUserAgents(inputFile):
    uas = []
    with open(inputFile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1-1])
    random.shuffle(uas)
    return uas

def agentRandomiser(inputList):
    randomAgent = random.choice(inputList)
    return randomAgent

def loadHtml(inputUrl):
    url = urllib2.Request(inputUrl, headers={ 'User-Agent': agentRandomiser(agentList) })
    inputHtml = urlopen(url).read()
    soup = BeautifulSoup(inputHtml, "html.parser")
    return soup

def getHref(inputUrl):
    soup = loadHtml(inputUrl)
    firstA = soup.find('a', attrs={"class":"card-click-target"})
    getHref = firstA.get('href')
    return getHref

def getGenre(inputUrl):
    soup = loadHtml(inputUrl)
    appGenre = soup.find('span', attrs={"itemprop":"genre"}).get_text()
    return appGenre

def loadApps(inputFile):
    listApps = []
    apps = open(inputFile, 'r')
    for app in apps:
        if len(app.split()) > 1:
            app = app.replace(' ','%20')
        else:
            app
        listApps.append(app)
    return listApps


"""
App Name -  chrome dev editor
Search query - chrome%20dev%20editor
"""

# appName = "slack"
searchUrl = "https://play.google.com/store/search?q="
appUrl = "https://play.google.com"
appsList = loadApps('app_list.txt')
agentList = LoadUserAgents('agent_list.txt')
genreList = open('app_genre_list.csv', 'w')

for appName in appsList:
    appHref = getHref(searchUrl + appName)
    appGenre = getGenre(appUrl + appHref)
    genreOut = appName + ", " + appGenre
    genreList.write(genreOut)
# print appsList
# print type(appsList)

# print appName, appGenre

genreList.close()
