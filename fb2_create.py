import base64
import os
from bs4 import BeautifulSoup
import requests
import save_file
from ex import p_red, p_green, p_blue

def templ_char():
    return '''<title><p>{title}</p></title>
{text}'''


def templ_bin():
    return '''<binary id="{name}" content-type="image/jpeg">{base}</binary>'''


def templ():
    return '''<?xml version="1.0" encoding="utf-8"?> 
<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" xmlns:l="http://www.w3.org/1999/xlink">
<description>
<title-info>
<author>
<last-name>{nickname}</last-name>
</author>
<book-title>{namebook}</book-title>
<annotation>
<p>{annotation}<br>Downloaded with Wattpad Downloader</br>
GitHub: https://github.com/Hell13Cat/WPD</p>
</annotation>
<coverpage>
<image l:href="#cover.jpg"/></coverpage>
<lang>ru</lang>
<src-lang>ru</src-lang>
</title-info>
<document-info>
<program-used>Wattpad Downloader: https://github.com/Hell13Cat/WPD</program-used>
</document-info>
</description>
<body>
{characters}
</body>
{binarys}
<binary id="cover.jpg" content-type="image/jpeg">{cover}</binary>
</FictionBook>'''

def base64_get(url):
    ufr = requests.get(url)
    return str(base64.b64encode(ufr.content))[2:-1]

def chapter_gen(text):
    image = ""
    soup = BeautifulSoup(text, 'html5lib')
    tags = soup.find_all('img', src=True)
    if len(tags) != 0:
        for span in soup.select('img'):
            img_tag_url = str(span["src"])
            img_name = (img_tag_url.split("/"))[-1] + ".jpg"
            meta = soup.new_tag('image')
            meta.attrs['l:href'] = "#" + img_name
            span.insert_after(meta)
            span.unwrap() 
            image += templ_bin().format(name=img_name, base=base64_get(img_tag_url))
    return {"image":image, "text":str(soup).replace("<html><head></head><body>", "").replace("</body></html>", "")}



def m(book):
    p_green("[I] Saving in fb2...")
    root_dir = os.getcwd()
    try:
        os.mkdir(root_dir + "/downloads")
    except:
        aa = 0
    chapters = book["characters"]
    binary = ""
    chapters_text = ""
    chapter_count = 0
    for chapter in chapters:
         chapter_count += 1
         print('[{c_num}/{c_all}] Generation "{chapter_title}": {chapter_id}'.format(c_num=str(chapter_count), c_all=str(len(chapters) + 1), chapter_title=chapter["title"], chapter_id=chapter["id"]))
         capt = chapter_gen(chapter["text"])
         chapters_text += templ_char().format(title=chapter["title"], text=capt["text"])
         binary += capt["image"]
    p_green('[{c_all}/{c_all}] Meta and information generation'.format(c_all=str(len(chapters) + 1)))
    ready_book = templ().format(link=book["source"], namebook=book["title"], annotation=book["description"], nickname=str(book["authors"]), characters=chapters_text, binarys=binary, cover=base64_get(book["cover"]))
    file = open(root_dir + "/downloads/" + str(book["id"]) + " - " + save_file.rename_valid_f(book["title"]) + ".fb2", "w")
    file.write(ready_book)
    file.close()
    p_green("[I] Saved to fb2")