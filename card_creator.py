import urllib.request as urllib2
from bs4 import BeautifulSoup
import urllib

import os
from anki.storage import Collection


import json
import pandas as pd
import html5lib

import inflections as inf

anki_home = '/home/kokurou/.local/share/Anki2/User 1'
anki_collection_path = os.path.join(anki_home,'collection.anki2')
col = Collection(anki_collection_path)

class CardCreator:
    def __init__(self, keyword, meaning):
        self.keyword = keyword
        self.meaning = meaning
        
    def create(self):
        # opening the search page
        page_html = urllib2.urlopen('https://jisho.org/search/'+urllib.parse.quote(self.keyword))
        total_soup = BeautifulSoup(page_html,'html.parser')
        # get the type of word being fetched, what verb, what adjective
        word_type = ' '.join(total_soup.find('div',{'class':'meaning-tags'}).get_text().split()[:2])
        print(word_type)
        if word_type.split()[1] == 'verb':
            if word_type == 'Godan verb':
                dict = inf.godan_inflections(self.keyword)
                deck = col.decks.by_name('Genki 1 - Godan verbs')
            elif word_type == 'Ichidan verb':
                dict = inf.ichidan_inflections(self.keyword)
                deck = col.decks.by_name('Genki 1 - Ichidan verbs')
            modelVerb = col.models.by_name('Verbs')
            col.decks.select(deck['id'])
            col.decks.current()['mid'] = modelVerb['id']
            note = col.new_note(modelVerb)
            field = 0
            print(len(note.fields))
            for i in dict.keys():
                note.fields[field] = dict[i]
                field += 1
            note.fields[field] = self.meaning
            col.add_note(note, deck['id'])

        elif word_type == 'I-adjective (keiyoushi)':
            dict = inf.i_inflections(self.keyword)
            pass
        elif word_type == 'Na-adjective (keiyodoshi),':
            dict = inf.na_inflections(self.keyword)
            pass

    

keyword = input('Enter the keyword to conjugate\n')
meaning = input('Enter the meaning\n')
p1 = CardCreator(keyword=keyword, meaning=meaning)
p1.create()