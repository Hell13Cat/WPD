#!/usr/bin/env python3

import sys
import io
import re

import requests
import dateutil.parser
import smartypants
import save_file, html_create, fb2_create, txt_create


session = requests.session()
session.headers['User-Agent'] = ''
API_STORYINFO = 'https://www.wattpad.com/api/v3/stories/' #9876543?drafts=0&include_deleted=1
API_STORYTEXT = 'https://www.wattpad.com/apiv2/storytext' # ?id=23456789
API_CHAPTERINFO = 'https://www.wattpad.com/apiv2/info' # ?id=23456789
API_GETCATEGORIES = 'https://www.wattpad.com/apiv2/getcategories'
ILLEAGAL_FILENAME_CHARACTERS = str.maketrans(r'.<>:"/\|?*^', '-----------')
categories = session.get(API_GETCATEGORIES).json()
categories = {int(k): v for k, v in categories.items()}


def download_story(story_id):
    storyinfo = session.get(API_STORYINFO + story_id, params={'drafts': 1, 'include_deleted': 1}).json()
    story_title = storyinfo['title']
    story_description = storyinfo['description']
    story_createDate = dateutil.parser.parse(storyinfo['createDate'])
    story_modifyDate = dateutil.parser.parse(storyinfo['modifyDate'])
    story_author = storyinfo['user']['name']
    story_categories = [categories[c] for c in storyinfo['categories'] if c in categories]
    story_rating = storyinfo['rating'] # TODO: I think 4 is adult?
    story_cover = session.get(storyinfo['cover']).content
    save_file.save_bytes(story_title, "cover.jpg", story_cover)
    story_url = storyinfo['url']

    print('[I] Story "{story_title}": {story_id}'.format(story_title=story_title, story_id=story_id))

    book = {}
    book["title"] = story_title
    book["authors"] = story_author
    book["categories"] = story_categories
    book["description"] = story_description
    book["url"] = story_url
    book["'publisher"] = "Wattpad Downloader"
    book["source"] = story_url
    book["rating"] = story_rating
  
    characters = []
    countsp = 0
    countspa = len(storyinfo["parts"])
    for part in storyinfo['parts']:
        countsp += 1
        chapter_title = part['title']

        if part['draft']:
            print('[{c_num}/{c_all}] Skipping "{chapter_title}": {chapter_id}, part is draft'.format(c_num=countsp, c_all=countspa, chapter_title=chapter_title, chapter_id=chapter_id))
            continue

        if 'deleted' in part and part['deleted']:
            print('[{c_num}/{c_all}] Skipping "{chapter_title}": {chapter_id}, part is deleted'.format(c_num=countsp, c_all=countspa, chapter_title=chapter_title, chapter_id=chapter_id))
            continue

        chapter_id = part['id']

        chapter_modifyDate = dateutil.parser.parse(part['modifyDate'])

        print('[{c_num}/{c_all}] Downloading "{chapter_title}": {chapter_id}'.format(c_num=countsp, c_all=countspa, chapter_title=chapter_title, chapter_id=chapter_id))

        chapter_html = session.get(API_STORYTEXT, params={'id': chapter_id, 'output': 'json'}).json()['text']
        chapter_html = smartypants.smartypants(chapter_html)


        section = {}
        section["text"] = chapter_html
        section["title"] = chapter_title
        section["id"] = chapter_id
        characters.append(section)
    book["characters"] = characters
    print("[?] What format to save the book(html, fb2, txt)?")
    while True == True:
        type_save = input("[>")
        if type_save == "html":
            html_create.m(book)
            break
        elif type_save == "fb2":
            fb2_create.m(book)
            break
        elif type_save == "txt":
            txt_create.m(book)
            break
        else:
            aa = 0
    


def get_story_id(url):
    match = re.search(r'\d+', url)
    if not match:
        return None

    url_id = match.group()
    storyinfo_req = session.get(API_STORYINFO + url_id)
    if storyinfo_req.ok:
        return url_id

    chapterinfo_req = session.get(API_CHAPTERINFO, params={'id': url_id})
    if not chapterinfo_req.ok:
        return None
    story_url = chapterinfo_req.json()['url']
    story_id = re.search(r'\d+', story_url).group()
    return story_id


def main():
    if sys.argv[1:]:
        story_urls = sys.argv[1:]
    else:
        story_urls = sys.stdin

    for story_url in story_urls:
        story_id = get_story_id(story_url)
        if story_id:
            download_story(story_id)
        else:
            print('ERROR: could not retrieve story', story_url)


if __name__ == '__main__':
    main()
