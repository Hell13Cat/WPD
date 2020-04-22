













from bs4 import BeautifulSoup
import re
import requests as req
import cfscrape
import os
import pickle



def files(setting, filen):
	file = open(os.getcwd() + "/data/" + filen, "wb")
	pickle.dump(setting, file)
def get_session():
 session = req.Session()
 session.headers = { 'Host':'www.wattpad.com',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language':'ru,en-US;q=0.5',
'Accept-Encoding':'gzip, deflate, br',
'DNT':'1',
'Connection':'keep-alive',
'Upgrade-Insecure-Requests':'1',
'Pragma':'no-cache',
'Cache-Control':'no-cache'}
 return cfscrape.create_scraper(sess=session)


os.system("clear")
sessionreq = get_session()
storyurl = "https://www.wattpad.com/story/145147050-нет-игры-нет-жизни-no-game-no-life/parts"
resp = sessionreq.get(storyurl)
soup = BeautifulSoup(resp.text, 'html5lib')
titlestory = (soup.title.string).split(" - ")
del titlestory[-1]
authorstory = titlestory[-1]
del titlestory[-1]


headtag = soup.select_one("head:nth-of-type(1)")
headtag.decompose()
tags = soup.find_all(['script'])
for ii in range(len(tags)):
 scripttag = soup.select_one("script:nth-of-type(1)")
 scripttag.decompose()

infobook = {}
bookurl = {}
bookcharacters = {}
bookbinary = {}
bookurlurl = []
bookurlname = []

print("----\n" + (" - ".join(titlestory)) + "\n----Автор----\n" + authorstory + "\n----Описание----")
infobook["title"] = " - ".join(titlestory)
infobook["author"] = authorstory
tags = soup.find_all("h2")
for tag in tags:
 if "description" in str(tag):
  print(tag.text)
  infobook["description"] = tag.text
files(infobook, "infobook")
tags = soup.find_all("a", href=True)
for tag in tags:
 if "navigate-part" in str(tag):
  bookurlurl.append("-> https://www.wattpad.com" + tag["href"])
  bookurlname.append((tag.text).replace("\n", ""))
  #print((tag.text).replace("\n", ""))
  #print("https://www.wattpad.com" + tag["href"])
bookurl["name"] = bookurlname
bookurl["url"] = bookurlurl






















