from bs4 import BeautifulSoup
import requests as req
import cfscrape
import sys
import os
import ex


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

def create_list(list_url):
    sessionreq = get_session()
    resp = sessionreq.get(list_url)
    soup = BeautifulSoup(resp.text, 'html5lib')
    storys_url = ""
    count_url = 0
    tags = soup.find_all("a", href=True)
    for tag in tags:
        if (("on-navigate" and "story/") in str(tag)) and ("img" not in str(tag)):
            count_url += 1
            add_url = "https://www.wattpad.com" + tag["href"] + " "
            storys_url += add_url
            print("[" + str(count_url) + "] " + tag.text + " added to list. Url: https://www.wattpad.com" + tag["href"])
    print("[I] Redirect to download script")
    os.system("python scrape.py " + storys_url)

def main():
    if sys.argv[1:]:
        list_urls = sys.argv[1:]
    else:
        list_urls = sys.stdin    
    for list_url in list_urls:
        create_list(ex.redirect_get(list_url))
if __name__ == '__main__':
    main()














