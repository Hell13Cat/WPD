import requests
import os

def rename_valid(text):
    extension = (text.split("."))[-1]
    text = ".".join((text.split("."))[0:-1])
    char_del = '''/\:|*"?+!><.@%'''
    for num in range(len(char_del)):
        text = text.replace(char_del[num], "_")
    text = text.replace("\n", "")
    return text + "." + extension

def rename_valid_f(text):
    char_del = '''/\:|*"?+!><.@%'''
    for num in range(len(char_del)):
        text = text.replace(char_del[num], "_")
    text = text.replace("\n", "")
    return text

def dirs_create(name):
    root_dir = os.getcwd()
    try:
        os.mkdir(root_dir + "/downloads")
    except:
        aa = 0
    try:
        os.mkdir(root_dir + "/downloads/" + rename_valid_f(name))
    except:
        aa = 0
    try:
        os.mkdir(root_dir + "/downloads/" + rename_valid_f(name) + "/img")
    except:
        aa = 0
    try:
        os.mkdir(root_dir + "/downloads/" + rename_valid_f(name) + "/chapters")
    except:
        aa = 0

def file_name(story, name):
    root_dir = os.getcwd()
    return root_dir + "/downloads/" + rename_valid_f(story) + "/img/" + rename_valid(name)

def save_url_name(names, story, urldown):
    dirs_create(story)
    f=open(file_name(story, names) ,"wb")
    ufr = requests.get(urldown)
    f.write(ufr.content)
    f.close()

def save_bytes(story, name, bit):
    dirs_create(story)
    file = open(file_name(story, name), "wb")
    file.write(bit)
    file.close()

def save_txt(story, name, text):
    dirs_create(story)
    root_dir = os.getcwd()
    file = open(root_dir + "/downloads/" + rename_valid_f(story) + "/chapters/" + rename_valid(name), "w")
    file.write(text)
    file.close()

def save_txt_info(story, text):
    dirs_create(story)
    root_dir = os.getcwd()
    file = open(root_dir + "/downloads/" + rename_valid_f(story) + "/info.txt", "w")
    file.write(text)
    file.close()

def save_url(name, url):
    return 0
