#!/usr/bin/env python3
import urllib.request as urllib2
from bs4 import BeautifulSoup
import urllib

import os
import argparse

from anki.storage import Collection

import pandas as pd

import inflections as inf

import furigana_gen as fg

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
        if 'verb' in word_type:
            deck = col.decks.by_name('Genki - Verbs')
            if word_type == 'Godan verb':
                dict = inf.godan_inflections(self.keyword)
            elif word_type == 'Ichidan verb,':
                dict = inf.ichidan_inflections(self.keyword)
            modelVerb = col.models.by_name('Verbs')
            col.decks.select(deck['id'])
            col.decks.current()['mid'] = modelVerb['id']
            note = col.new_note(modelVerb)
            field = 0
            for i in dict.keys():
                note.fields[field] = fg.add_furigana(dict[i])
                field += 1
            note.fields[field] = self.meaning
            col.add_note(note, deck['id'])
        elif 'adjective' in word_type:
            print("adjective")
            deck = col.decks.by_name('Genki - Adjectives')
            if word_type == 'I-adjective (keiyoushi)':
                dict = inf.i_inflections(self.keyword)
            elif word_type == 'Na-adjective (keiyodoshi),':
                dict = inf.na_inflections(self.keyword)
            modelAdj = col.models.by_name('Adjectives')
            col.decks.select(deck['id'])
            col.decks.current()['mid'] = modelAdj['id']
            note = col.new_note(modelAdj)
            field = 0
            for i in dict.keys():
                note.fields[field] = fg.add_furigana(dict[i])
                field += 1
            note.fields[field] = self.meaning
            col.add_note(note, deck['id'])
        else:
            print("other")
            deckVocab = col.decks.by_name('Genki - Vocab')
            modelVocab = col.models.by_name('Basic (and reversed card)')
            col.decks.select(deckVocab['id'])
            col.decks.current()['mid'] = modelVocab['id']
            note = col.new_note(modelVocab)
            note.fields[0] = fg.add_furigana(self.keyword)
            note.fields[1] = self.meaning
            col.add_note(note, deckVocab['id'])

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create notes for the entered japanese vocabulary in Anki')
    parser.add_argument('-k','--keyword', help='Keyword to create notes on')
    parser.add_argument('-m','--meaning', help='Meaning of the keyword')
    parser.add_argument('-f','--file',help='Input file in CSV format')
    args = parser.parse_args()
    if args.keyword and args.meaning:
        p1 = CardCreator(keyword=args.keyword, meaning=args.meaning)
        p1.create()
    elif args.file:
        keywords = pd.read_csv(args.file)
        print(keywords.columns)
        for _, rows in keywords.iterrows():
            print(rows['Keyword'],rows['Meaning'])
            p1 = CardCreator(keyword=rows['Keyword'],meaning=rows['Meaning'])
            p1.create()