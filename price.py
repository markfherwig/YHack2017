import pandas as pd
import numpy as np

import requests as rq
import pprint

from functools import reduce

pp = pprint.PrettyPrinter(indent=4)

def crypto_api():
	r = rq.get('https://min-api.cryptocompare.com').json()
	available = r['AvailableCalls']['Price']
	for call, description in available.items():
		print(call)
		print(description['Info']['Description'])
		#pp.pprint(description)

def explain_api(name):
	r = rq.get('https://min-api.cryptocompare.com').json()
	available = r['AvailableCalls']['Price']
	pp.pprint(available[name])

def check_limit():
	base_url = 'https://min-api.cryptocompare.com/stats/rate'
	times = ['/hour', '/minute', '/second']
	for time in times:
		url = base_url+time+'/limit'
		r = rq.get(url).json()
		print(time)
		print('Made: ' + str(r['CallsMade']))
		print('Left: ' + str(r['CallsLeft']))

def query_period(currency, duration, start=None):
	# start timestamp, duration in hours
	base_url = 'https://min-api.cryptocompare.com'
	url = base_url + '/data/histohour'
	params = {'fsym': currency, 'tsym': 'USD', 'limit': duration}
	if start is not None:
		params['toTs'] = start
	#print(params)
	r = rq.get(url, params=params).json()
	raw_data = r['Data']
	columns = ['time', 'open', 'close', 'low', 'high', 'volumefrom', 'volumeto']
	
	data = {}
	for col in columns:
		data[col] = reduce(lambda x, y: x+[y[col]], raw_data, [])
	
	df = pd.DataFrame(data, columns=columns)
	df['time'] = pd.to_datetime(df['time'], unit='s')
	df.set_index('time', inplace=True)
	
	return df

def query_all(currency):
	duration = 1920
	df = query_period(currency, duration)
	
	while(True):
		df.sort_index()
		if df.at[df.index[0], 'open'] == 0.0:
			return df[(df.T != 0).any()]
		
		time = df.index.values[0].astype(np.int64) / 1000000000
		newTime = time - duration
		df2 = query_period(currency, duration, newTime)
		#print(df2)
		#check_limit()
		df = df2.append(df).drop_duplicates()
	return df

def gen_currency(currency):
	data = query_all(currency)
	data.to_csv('price_data/' + currency + '.csv')

from cryptosAbreviationMap import crypto_map
from parse_crypto import get_top
top = get_top()
map = crypto_map()
for coin in top:
	ticker = map[coin]
	print(coin, ticker)
	try:
		gen_currency(ticker)
	except:
		print(coin + 'failed')


# gen_currency('BTC')
# crypto_api()