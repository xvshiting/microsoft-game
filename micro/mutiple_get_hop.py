from urlTools import urlTools
import get_dict as gd
res=[]
reslist=[]
myurl=urlTools()
def id_id_get_hop(id1,id2,d1,d2):
	print 'id_id'
	id_id_get_one_hop(id1,id2,d1,d2)
def id_AuId_get_hop(id1,id2,d1,d2):
	print 'id_AUID'
	ID_AUID_ONE_HOP(id1,id2,d1,d2)
	ID_AUID_TWO_HOP(id1,id2,d1,d2)
	ID_AUID_THREE_HOP(id1,id2,d1,d2)
def AuId_Id_get_hop(id1,id2,d1,d2):
	print 'AUID_ID'
	AUID_ID_ONE_HOP(id1,id2,d1,d2)
def AuId_AuId_get_hop(id1,id2,d1,d2):
	print 'AUID_AUID'
	AUID_AUID_two_HOP(id1,id2,d1,d2)
def get_hop(id1,id2):
	res[:]=[]
	hop_type=0
	d1={}
	d2={}
	i_d=[id1,id2]
	i_d_1={'AA.AuId':[id2]}
	myurl.set_attributes()
	myurl.set_expr('Composite(AA.AuId='+id1+')')
	data=gd.get_dict(myurl.get_url())
	d1=data['entities']
	myurl.set_expr('Composite(AA.AuId='+id2+')')
	data=gd.get_dict(myurl.get_url())
	d2=data['entities']
	if d1==[]:
		myurl.set_expr('Id='+id1)
		data=gd.get_dict(myurl.get_url())
		d1=data['entities'][0]
		hop_type=hop_type+1
	if d2==[]:
		myurl.set_expr('Id='+id2)
		data=gd.get_dict(myurl.get_url())
		d2=data['entities'][0]
		hop_type=hop_type+2
	operator={0:AuId_AuId_get_hop,1:id_AuId_get_hop,2:AuId_Id_get_hop,3:id_id_get_hop}
	operator.get(hop_type)(id1,id2,d1,d2) 
	return res