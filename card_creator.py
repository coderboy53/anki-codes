import urllib.request as urllib2
import urllib
from bs4 import BeautifulSoup

import os
from anki.storage import Collection


import json
import pandas as pd
import html5lib

import inflections

anki_home = '/home/kokurou/.local/share/Anki2/User 1'
anki_collection_path = os.path.join(anki_home,'collection.anki2')
col = Collection(anki_collection_path)

class CardCreator:
    def __init__(self, keyword):
        self.keyword = keyword
    def generate_inflections(word_type, keyword):
        
        pass
        
    def create(self):
        # opening the search page
        page_html = urllib2.urlopen('https://jisho.org/search/'+urllib.parse.quote(self.keyword))
        total_soup = BeautifulSoup(page_html,'html.parser')
        # get the type of word being fetched, what verb, what adjective
        word_type = ' '.join(total_soup.find('div',{'class':'meaning-tags'}).get_text().split()[:2])
        if word_type == 'Godan verb':
            pass
        elif word_type == 'Ichidan verb':
            pass
        elif word_type == 'I-adjective (keiyoushi)':
            pass
        elif word_type == 'Na-adjective (keiyodoshi),':
            print(word_type)
            pass

    

keyword = input('Enter the keyword to conjugate\n')
p1 = CardCreator(keyword=keyword)
p1.create()