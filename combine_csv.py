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
            print(df.info(verbose=True))
            dfs.append(df)
    
    return pd.concat(dfs)

# print(combine_csv())