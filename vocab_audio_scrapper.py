import requests
godan_path = '/home/kokurou/Documents/日本語/Genki 1 - う verbs.txt'
try:
    godan_file = open(godan_path,'r')
except IOError:
    print('Could not read or open file')
