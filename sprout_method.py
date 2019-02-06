import urllib.request
import operator
import re

def perform():
    url = 'http://www.gutenberg.org/files/11/11-0.txt'
    response = urllib.request.urlopen(url)
    data = response.read()
    txt = data.decode('utf-8')
    txt = re.compile('[\!“”\‘’,\.\?\(\);:\[\]]').sub('', txt)
    txt = re.compile('-').sub(' ', txt)
    txt = txt.lower()
    words = txt.split()
    cwords = {}
    for word in words:
        if word in cwords:
            cwords[word] = cwords[word] + 1
        else:
            cwords[word] = 1
    o_words = {}
    for word in cwords:
        if cwords[word] >= 10:
            if len(word) == 7:
                o_words[word] = cwords[word]
    d = o_words
    o_words = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
    glength = 0
    for k, v in o_words:
        if len(k) > glength:
            glength = len(k)
    for line in lines_to_print(glength, o_words):
        print(line)

def lines_to_print(glength, o_words):
    lines = []
    for k, v in o_words:
        s = ' ' * (glength - len(k))
        if v < 10:
            s = s + ' '
        lines.append(k + ': ' + s + str(v))
    return lines
