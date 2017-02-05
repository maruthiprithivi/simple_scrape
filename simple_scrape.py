from bs4 import BeautifulSoup
import urllib2
from urllib2 import urlopen
# from urllib2 import requests
import random


def LoadUserAgents(uafile):
    """
    uafile : string
        path to text file of user agents, one per line
    """
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1-1])
    random.shuffle(uas)
    return uas

def agentRandomiser(inputFile):
    # agent_list = LoadUserAgents(inputFile)
    # agent_list = open(inputFile, 'rb')
    random_agent = random.choice(agent_list)
    return random_agent

agent_list = LoadUserAgents("agent_list.txt")
# agent = agentRandomiser(agent_list)

"""
App Name -  chrome dev editor
Search query - chrome%20dev%20editor
"""

app_name = "slack"
search_url = "https://play.google.com/store/search?q="
app_url = "https://play.google.com"

url1 = urllib2.Request(search_url + app_name, headers={ 'User-Agent': agentRandomiser(agent_list) })
search_html = urlopen(url1).read()
soup1 = BeautifulSoup(search_html, "html.parser")
first_a = soup1.find('a', attrs={"class":"card-click-target"})
get_href = first_a.get('href')

url2 = urllib2.Request(app_url + get_href, headers={ 'User-Agent': agentRandomiser(agent_list) })
app_html = urlopen(url2).read()
soup2 = BeautifulSoup(app_html, "html.parser")
app_category = soup2.find('span', attrs={"itemprop":"genre"}).get_text()

print app_category
