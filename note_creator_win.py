#!/usr/bin/env python3
import urllib.request as urllib2
from bs4 import BeautifulSoup
import urllib

import os
import argparse

from anki.storage import Collection

import pandas as pd

import inflections as inf

anki_home = r'C:\Users\user\AppData\Roaming\Anki2\User 1'

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
        if 'verb' in word_type:
            if word_type == 'Godan verb':
                dict = inf.godan_inflections(self.keyword)
                deck = col.decks.by_name('Genki 1 - Godan verbs')
            elif word_type == 'Ichidan verb,':
                dict = inf.ichidan_inflections(self.keyword)
                deck = col.decks.by_name('Genki 1 - Ichidan verbs')
            modelVerb = col.models.by_name('Verbs')
            col.decks.select(deck['id'])
            col.decks.current()['mid'] = modelVerb['id']
            note = col.new_note(modelVerb)
            field = 0
            for i in dict.keys():
                note.fields[field] = dict[i]
                field += 1
            note.fields[field] = self.meaning
            col.add_note(note, deck['id'])
        if 'adjective' in word_type:
            if word_type == 'I-adjective (keiyoushi)':
                dict = inf.i_inflections(self.keyword)
                deck = col.decks.by_name('Genki 1 - い adjectives')
            elif word_type == 'Na-adjective (keiyodoshi),':
                dict = inf.na_inflections(self.keyword)
                deck = col.decks.by_name('Genki 1 - な adjectives')
            modelAdj = col.models.by_name('Adjectives')
            col.decks.select(deck['id'])
            col.decks.current()['mid'] = modelAdj['id']
            note = col.new_note(modelAdj)
            field = 0
            for i in dict.keys():
                note.fields[field] = dict[i]
                field += 1
            note.fields[field] = self.meaning
            col.add_note(note, deck['id'])

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create notes for the entered japanese vocabulary in Anki')
    parser.add_argument('-k','--keyword', help='Keyword to create notes on')
    parser.add_argument('-m','--meaning', help='Meaning of the keyword')
    parser.add_argument('-f', '--file',help='Path of text file to ready from')
    args = parser.parse_args()
    if args.file:
        file = open(args.file, encoding='utf-8-sig',mode='r')
        for line in file:
            pairs = line.rstrip().split(',')
            p1 = CardCreator(keyword=pairs[0],meaning=pairs[1])
            p1.create()
    else:
        p1 = CardCreator(keyword=args.keyword, meaning=args.meaning)
        p1.create()