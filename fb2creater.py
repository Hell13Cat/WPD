











import pickle


def filel(name):
 file = open(os.getcwd() + "/data/" + name, "rb")
 res = pickle.load(file)
 return res


templateimg = '''<image l:href="#{name}"/>'''


templatecharacter = '''<section>
<title><p>{title}</p></title>
{text}
</section>'''


templatebinary = '''<binary id="{name}" content-type="image/{type}">
{base)</binary>'''


template = '''<?xml version="1.0" encoding="utf-8"?> 
<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" xmlns:l="http://www.w3.org/1999/xlink">
<description>
<title-info>
<book-title>{namebook}</book-title>
<coverpage>
<image l:href="#cover.jpg"/></coverpage>
<lang>ru</lang>
<src-lang>ru</src-lang>
</title-info>
<document-info>
<author>
<nickname>{nickname}</nickname>
</author>
<program-used>Wattpad Downloader</program-used>
</document-info>
</description>
<body>
<title><p>{namebook}</p></title>
{annotation}
{characters}
</body>
{binarys}
<binary id="cover.jpg" content-type="image/jpeg">{cover)</binary>
</FictionBook>'''



#template.format(namebook, annotation, nickname, characters, binarys)
#templateimg.format(name)
#templatecharacter.format(title,  text)
#templatebinary(name, type, binary)













