import os
from googlesearch import search

def read_links():
    d = {}
    if not os.path.exists('C:\\Users\\pvshe\\PycharmProjects\\DataHarvester\\DataCollection\\Data\\links.csv'):
        return d
    with open('C:\\Users\\pvshe\\PycharmProjects\\DataHarvester\\DataCollection\\Data\\links.csv', 'r') as linkfile:
        data = [line[:-1].split(',') for line in linkfile]
        for line in data:
            d[line[0]] = line[1:]
    return d

def write_links(data):
    if os.path.exists('Data\\links.csv'):
        mode = 'a'
    else:
        mode = 'w'
    with open('Data\\links.csv', mode) as linkfile:
        linkfile.write(','.join(data) + '\n')
