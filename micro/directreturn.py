
def get_time():
	stimes=stimes+1
	print stimes
	return stimes
def set_res(jso):
	ress.append(jso)
def get_json():
	print 'direct'
	return ress[stimes-6]
stimes=[]
ress=[]