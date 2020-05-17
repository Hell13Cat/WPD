from bs4 import BeautifulSoup
import requests as req
import cfscrape
import sys
import os
import ex
import re
import shutil
import save_file
import requests
from ex import p_red, p_green, p_blue

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

def create_list(list_url, type_save):
    try:
        os.rename("downloads","downloads_temp")
    except:
        aa = 00
    sessionreq = get_session()
    resp = sessionreq.get(list_url)
    soup = BeautifulSoup(resp.text, 'html5lib')
    storys_url = ""
    count_url = 0
    id_list = []
    match = re.search(r'\d+', list_url)
    url_id = match.group()
    tags = soup.find_all("h1")
    list_name = (tags[0]).text
    p_green("[I] " + (tags[0]).text + " list")
    tags = soup.find_all("a", href=True)
    for tag in tags:
        if (("on-navigate" and "story/") in str(tag)) and ("img" not in str(tag)):
            count_url += 1
            add_url = "https://www.wattpad.com" + tag["href"] + " "
            match = re.search(r'\d+', add_url)
            url_id = match.group()
            id_list.append(url_id)
            storys_url += add_url
            print("[" + str(count_url) + "] " + tag.text + " added to list. Url: https://www.wattpad.com" + tag["href"])
    p_green("[I] Redirect to download script")
    os.system("python scrape.py "+ type_save + " " + storys_url)
    p_green("[I] Directory Organization...")
    try:
        os.mkdir(os.getcwd() + "/downloads")
    except:
        aa = 0
    try:
        os.mkdir(os.getcwd() + "/lists")
    except:
        aa = 0
    try:
        os.mkdir(os.getcwd() + "/lists/" + url_id + " - " + save_file.rename_valid_f(list_name))
    except:
        aa = 0
    list_dir = os.listdir(path=os.getcwd() + "/downloads")
    for file_d in list_dir:
        if file_d.split(" ")[0] in id_list:
            try:
                shutil.copytree(os.getcwd() + "/downloads/" + file_d, os.getcwd() + "/lists/" + url_id + " - " + save_file.rename_valid_f(list_name) + "/" + file_d)
            except:
                aa = 00
            try:
                shutil.copy(os.getcwd() + "/downloads/" + file_d, os.getcwd() + "/lists/" + url_id + " - " + save_file.rename_valid_f(list_name) + "/")
            except:
                aa = 00
    shutil.rmtree(os.getcwd() + "/downloads")
    try:
        os.rename("downloads_temp","downloads")
    except:
        aa = 00
    p_green("[I] List Folder Ready")
    p_green("[I] " + list_name + " downloaded")


def create_profile(nickname, type_save):
    p_green("[I] Reading lists from " + nickname + " are added to the queue...")
    session = requests.session()
    session.headers['User-Agent'] = ''
    lists_url = 'https://www.wattpad.com/api/v3/users/{nickname}/lists?limit=100'
    list_json = session.get(lists_url.format(nickname=nickname)).json()
    count_all = list_json["total"]
    list_prep = list_json["lists"]
    count_one = 0
    list_url_ready = []
    for list_one in list_prep:
        count_one += 1
        print ("[{count_one}/{count_all}] The {name} list is added to the queue : {id}". format(count_all=count_all, count_one=count_one, name=list_one["name"], id=list_one["id"]))
        list_url_ready.append("https://www.wattpad.com/list/" + str(list_one["id"]))
    for down_url in list_url_ready:
        create_list(down_url, type_save)
    p_green("[I] All reading lists saved")
    

def main():
    p_blue("[?] What format to save the book(fb2, txt)?")
    while True == True:
        type_save = input("[>")
        if type_save == "fb2":
            aa = 0
            break
        elif type_save == "txt":
            aa = 0
            break
        else:
            aa = 0
    if sys.argv[1] == "list":
        if sys.argv[2:]:
            list_urls = sys.argv[2:]
        else:
            list_urls = sys.stdin    
        for list_url in list_urls:
            create_list(ex.redirect_get(list_url), type_save)
    if sys.argv[1] == "profile":
        nickname = sys.argv[2]    
        create_profile(nickname, type_save)
if __name__ == '__main__':
    main()














