#-*-coding:utf-8-*-
import json
from urlTools import urlTools 
import requests
s = requests.Session()
saved_data={}
def get_dict(url):
	offset=0
	if saved_data.has_key(url):
		return saved_data[url]
	data=s.get(url).json()
	if data !=[]:
		new_data=data
		while len(new_data['entities'])>=10000:
			print 'another 10000 entities'
			url=url.replace("offset="+str(offset),"offset="+str(offset+10000))
			new_data=s.get(url).json()
			offset=offset+10000
			data['entities'].append(new_data['entities'])
			if offset>=110000:
				break
	saved_data[url]=data
	return data

if __name__ == '__main__':
	ss='https://oxfordhk.azure-api.net/academic/v1.0/evaluate?subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6&count=10000&attributes=Id,AA.AuId,AA.AfId,RId,F.FId,J.JId,C.CId&expr=Composite(AA.AfId=56590836)'
	print len(get_dict(ss))
