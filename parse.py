import pandas as pd
import requests
import json
import re
import sys

import pprint

def get_words(text):
    return re.compile('\w+').findall(text)

pp = pprint.PrettyPrinter(indent=2)

def read_file(filename):
    file = open(filename)
    raw_data = file.read()
    lines = raw_data.split('\n')

    keep = ['id', 'created_utc', 'title', 'selftext', 'num_comments', 'score', 'subreddit']

    data = []
    for line in lines:
        if line.isspace():
            continue
        try:
            parsed = json.loads(line)
            #pp.pprint(parsed)
            data.append({x: y for x, y in parsed.items() if x in keep})
        except json.decoder.JSONDecodeError:
            pass
    print(str(len(data)) + ' lines read')
    return data

def search_data(data, slist):
    data_string = (data['title'] + " " + data['selftext']).lower()
    words = get_words(data_string)
    matches = []
    for s in slist:
        if (len(s.split()) > 1 and s.lower() in data_string) or s.lower() in words:
            matches.append(s)
    return matches

def filter_data(data, slist):
    filtered = []
    for item in data:
        matches = search_data(item, slist)
        if len(matches) != 0:
            item['matches'] = matches
            filtered.append(item)
    return filtered

def get_top():
    file = open('top-200-cryptos.txt')
    data = file.read()
    split = data.split('\n')
    return split

def filter_by_crypto(filename):
    sample = read_file(filename)
    cryptos = get_top()
    all_crypto = filter_data(sample, cryptos)
    return all_crypto

def filter_and_save(filename):
    data = filter_by_crypto(filename)
    if len(data) == 0:
        print("No data")
        return
    df = pd.DataFrame(data)
    df['time'] = pd.to_datetime(df['created_utc'], unit='s')
    df.drop(['created_utc'], axis=1, inplace=True)
    df.set_index('time', inplace=True)
    df.to_csv(filename+'.csv')

if len(sys.argv) > 1:
    filter_and_save(sys.argv[1])