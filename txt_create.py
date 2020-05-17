import save_file
from bs4 import BeautifulSoup
from ex import p_red, p_green, p_blue

def templ_main():
    return '''+->
| {}
+->
Posted on Wattpad: {}
<--- Description --->
{}
<--- References --->
Wattpad: {}
Wattpad Downloader: https://github.com/Hell13Cat/WPD'''

def templ_ch():
    return '''+->
| {}
+->
{}'''

def m(book):
    p_green("[I] Saving in txt...")
    info_book = templ_main().format(book["title"], book["authors"], book["description"], book["source"])
    save_file.save_txt_info(book["id"] + " - " + book["title"], info_book)
    chapters = book["characters"]
    chapter_count = 0
    for capter in chapters:
        chapter_count += 1
        print('[{c_num}/{c_all}] Saving "{chapter_title}": {chapter_id}'.format(c_num=str(chapter_count), c_all=str(len(chapters)), chapter_title=capter["title"], chapter_id=capter["id"]))
        chapter_text = ""
        title = capter["title"]
        text = capter["text"]
        text = text.replace("<br>", "\n")
        soup = BeautifulSoup(text, 'html5lib')
        tags = soup.find_all('img', src=True)
        for ii in range(len(tags)):
            img_tag_url = (tags[ii])["src"]
            save_file.save_url_name("#" + str(chapter_count) + "~" + str(ii + 1) + ".jpg", book["id"] + " - " + book["title"], img_tag_url)
            img_tag = soup.select_one("img:nth-of-type(1)")
            img_tag.decompose()
        tags = soup.find_all("p")
        for tag in tags:
            chapter_add = "\n\n" + tag.text
            chapter_text += chapter_add
        save_file.save_txt(book["id"] + " - " + book["title"], "#" + str(chapter_count) + " " + title + ".txt", templ_ch().format(capter["title"], chapter_text))
    p_green("[I] Saved to txt")
