import requests as req
import cfscrape
from colorama import Fore, Back, Style, init

def files(setting, filen):
	file = open(os.getcwd() + "/data/" + filen, "wb")
	pickle.dump(setting, file)
def get_session():
 session = req.Session()
 session.headers = { 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language':'ru,en-US;q=0.5',
'Accept-Encoding':'gzip, deflate, br',
'DNT':'1',
'Connection':'keep-alive',
'Upgrade-Insecure-Requests':'1',
'Pragma':'no-cache',
'Cache-Control':'no-cache'}
 return cfscrape.create_scraper(sess=session)


def refu(url):
    sessionreq = get_session()
    resp = sessionreq.get(url, allow_redirects=False)
    try:
        return ["1", resp.headers["Location"]]
    except:
        return ["0", url]

def redirect_get(url):
    red = 1
    history = []
    while red == 1:
        a = refu(url)
        if a[0] == "0":
            red = 0
            red_url = a[1]
        else:
            url = a[1]
    return red_url

def p_red(text): 
    init(autoreset=True)
    print(Back.RED + text)

def p_green(text): 
    init(autoreset=True)
    print(Back.GREEN + text)

def p_blue(text): 
    init(autoreset=True)
    print(Back.BLUE + text)

