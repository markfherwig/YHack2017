from os import listdir
import pandas as pd
import numpy as np

def combine_csv():
    files = listdir('.')
    dfs = []
    for filename in files:
        print(filename)
        if filename.split('.')[-1] == 'csv':
            df = pd.read_csv(filename, index_col='time')
            #print(df)
            # print(df.info(verbose=True))
            dfs.append(df)
    
    combined = pd.concat(dfs)
    combined.sort_index(inplace=True)
    return combined.dropna(subset=['subreddit', 'title', 'score', 'num_comments'])

df = combine_csv()
df.to_csv('submissions.csv')
print(df)