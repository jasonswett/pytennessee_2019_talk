import urllib.request
import operator
import re

def count_words():
    url = 'http://www.gutenberg.org/files/11/11-0.txt'
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    text = re.compile('[\!“”\‘’,\.\?\(\);:\[\]]').sub('', text)
    text = re.compile('-').sub(' ', text)
    text = text.lower()
    words = text.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1

    words_appearing_once = []

    for word in word_counts:
        if word_counts[word] == 1:
            words_appearing_once.append(word)

    words_appearing_once.sort()
    for word in words_appearing_once:
        print(word)

count_words()
