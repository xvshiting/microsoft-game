#-*-coding:utf-8-*-
from urlTools import urlTools
import get_dict as gd
res=[]
reslist={}
pair_list={}
myurl=urlTools()
def get_sigle_id_attribute_list(d2):
	d2_ALL=[]
	type_d2_ALL=[]
	if d2.has_key('C'):
		d = d2['C']
		d2_ALL.append(d['CId'])
		type_d2_ALL.append(['C.CId',d['CId']])
	if d2.has_key('F'):
		for d in d2['F']:
			d2_ALL.append(d['FId'])
			type_d2_ALL.append(['F.FId',d['FId']])
	if d2.has_key('J'):
		d = d2['J']
		d2_ALL.append(d['JId'])
		type_d2_ALL.append(['J.JId',d['JId']])
	dd_2=d2['AA']
	for d in dd_2:
		d2_ALL.append(d['AuId'])
		type_d2_ALL.append(['AA.AuId',d['AuId']])


	return d2_ALL,type_d2_ALL
def RID_id2(d1_RID,id2):  #return RID
	print 'RID_id2'
	RID_3=[]
	if d1_RID!=[]:
		pId=d1_RID
		myurl.set_attributes(['Id'])
		while len(pId)>100:
			myurl.set_expr(myurl.combine_with_and(myurl.set_id(pId[0:100]),'RId='+id2))
		# print myurl.get_url()
			data=gd.get_dict(myurl.get_url())
			for d in data['entities']:
				RID_3.append(d['Id'])
			pId=pId[100:]
		if len(pId)>=1:
			myurl.set_expr(myurl.combine_with_and(myurl.set_id(pId),'RId='+id2))
			# print myurl.get_url()
			data=gd.get_dict(myurl.get_url())
			for d in data['entities']:
				RID_3.append(d['Id'])
		myurl.set_attributes()
	return RID_3
def get_attr_id_pair(auid_list,fid_list,jid_list,cid_list,data,id1,id2):
	for d in data['entities']:
		for d_AA in d['AA']:
			if d_AA['AuId'] in auid_list:
				print '*->AA.AuId(F.Fid/J.JId/C.CId)->Id->*'
				res.append([long(id1),d_AA['AuId'],d['Id'],long(id2)])

		if d.has_key('F'):
			for d2 in d['F']:
				if d2['FId'] in fid_list :
					print '*->AA.AuId(F.Fid/J.JId/C.CId)->Id->*'
					res.append([long(id1),d2['FId'],d['Id'],long(id2)])
					
		if d.has_key('J'):
			d2= d['J']
			if d2['JId'] in jid_list:
				print '*->AA.AuId(F.Fid/J.JId/C.CId)->Id->*'
				res.append([long(id1),d2['JId'],d['Id'],long(id2)])
				
		if d.has_key('C'):
			d2= d['C']
			if d2['CId'] in cid_list:
				print '*->AA.AuId(F.Fid/J.JId/C.CId)->Id->*'
				res.append([long(id1),d2['CId'],d['Id'],long(id2)])
def get_rid_attr_pair(auid_list,fid_list,jid_list,cid_list,data,id1,id2):
	for d in data['entities']:
		for d_AA in d['AA']:
			if d_AA['AuId'] in auid_list:
				print '*->Id->AA.AuId(F.Fid/J.JId/C.CId)->*'
				res.append([long(id1),d['Id'],d_AA['AuId'],long(id2)]) 
		if d.has_key('F'):
			for d2 in d['F']:
				if d2['FId'] in fid_list :
					print '*->Id->AA.AuId(F.Fid/J.JId/C.CId)->*'
					res.append([long(id1),d['Id'],d2['FId'],long(id2)])
		if d.has_key('J'):
			d2= d['J']
			if d2['JId'] in jid_list:
				print '*->Id->AA.AuId(F.Fid/J.JId/C.CId)->*'
				res.append([long(id1),d['Id'],d2['JId'],long(id2)])
		if d.has_key('C'):
			d2= d['C']
			if d2['CId'] in cid_list:
				print '*->Id->AA.AuId(F.Fid/J.JId/C.CId)->*'
				res.append([long(id1),d['Id'],d2['CId'],long(id2)])
def get_ID_RID_pair(data):
	lis=[]
	for d in data:
		for r in d['RId']:
			lis.append([d['Id'],r])
	return lis
def get_AfID_ID(data,AUID):
	AF_lis=[]
	ID_lis=[]
	for d in data:
		# print d
		if d.has_key('AA'):
			d_AA=d['AA']
			ID_lis.append(d['Id'])
			for d_AF in d_AA:
				if str(d_AF['AuId'])==str(AUID):
					if d_AF.has_key('AfId'):
						if d_AF['AfId'] not in AF_lis:
							AF_lis.append(d_AF['AfId'])
	return AF_lis,ID_lis	
def get_dict_AfId_Id(data,AUID_list):
	dic={}
	for d in data:
		if d.has_key('AA'):
			d_AA=d['AA']
			for d_AF in d_AA:
				if d_AF['AuId']in AUID_list:
					if d_AF.has_key('AfId'):
						try :
							d_lis=dic[d_AF['AuId']]
							d_lis=d_lis.append(d_AF['AfId'])
							dic[d_AF['AuId']]=d_lis
						except:
							dic[d_AF['AuId']]=[d_AF['AfId']]


	return dic

def id_id_get_one_hop(id1,id2,d1,d2):
	dd1= d1['RId']
	dd2=d2['Id']
	if dd2 in dd1:
		res.append([long(id1),long(id2)])
	id_id_get_two_hop(id1,id2,d1,d2,dd1)
def id_id_get_two_hop(id1,id2,d1,d2,RID_ID1):
	#Id->AA.AuId(F.Fid/J.JId/C.CId)->Id
	d1_list,no_1=get_sigle_id_attribute_list(d1)
	d2_list,no_2=get_sigle_id_attribute_list(d2)
	for d in set(d1_list).intersection(set(d2_list)):
		res.append([long(id1),d,long(id2)])
	#	Id->RId->RId
	d1_RID=RID_id2(RID_ID1,id2)
	for d in d1_RID:
		res.append([long(id1),d,long(id2)])
	id_id_get_THREE_HOP(id1,id2,d1,d2,no_1,no_2,RID_ID1)
def id_id_get_THREE_HOP(id1,id2,d1,d2,d1_list,d2_list,RID_ID1):
	#Id->AA.AuId(F.Fid/J.JId/C.CId)->Id->RId
	AUID_list=[]
	FID_list=[]
	JID_list=[]
	CID_list=[]
	myurl.set_attributes(['AA.AuId','F.FId','J.JId','C.CId','Id'])
	operator={'AA.AuId':AUID_list,'F.FId':FID_list,'J.JId':JID_list,'C.CId':CID_list}
	for d in d1_list:
		operator.get(d[0]).append(d[1])
	myurl.set_expr(myurl.combine_with_and(myurl.get_A_F_J_C(d1_list),'RId='+id2))
	data=gd.get_dict(myurl.get_url())
	get_attr_id_pair(AUID_list,FID_list,JID_list,CID_list,data,id1,id2)
	#Id->RId->AA.AuId(F.Fid/J.JId/C.CId)->Id
	AUID_list=[]
	FID_list=[]
	JID_list=[]
	CID_list=[]
	for d in d2_list:
		operator={'AA.AuId':AUID_list,'F.FId':FID_list,'J.JId':JID_list,'C.CId':CID_list}
		operator.get(d[0]).append(d[1])
	if RID_ID1!=[]:
		myurl.set_expr(myurl.combine_with_and(myurl.get_A_F_J_C(d2_list),myurl.set_id(RID_ID1)))
		data=gd.get_dict(myurl.get_url())
		get_rid_attr_pair(AUID_list,FID_list,JID_list,CID_list,data,id1,id2)
	#Id->RId->RId->RId
		myurl.set_expr('RId='+id2)
		myurl.set_attributes(['Id','RId'])
		data=gd.get_dict(myurl.get_url())
		RIDed_id2=[]
		if data['entities']!=[]:
			data=data['entities']
			for d in data:
				RIDed_id2.append(d['Id'])
			myurl.set_expr(myurl.set_id(RID_ID1))
			myurl.set_attributes(['RId','Id'])
			data=gd.get_dict(myurl.get_url())
			data_En=data['entities']
			rid_rid_list=[]
			for d in data_En:
				for dRID in d['RId']:
					rid_rid_list.append([d['Id'],dRID])
			for d in rid_rid_list:
				if d[1] in RIDed_id2:
					res.append([long(id1),d[0],d[1],long(id2)])
def AUID_ID_ONE_HOP(id1,id2,d1,d2):
	lis=[]
	for d in d1:
		lis.append(d['Id'])
	if d2['Id'] in lis:
		res.append([long(id1),long(id2)])
	AUID_ID_TWO_HOP(id1,id2,d1,d2,lis)
def AUID_ID_TWO_HOP(id1,id2,d1,d2,lis):
	#AUID->ID->RID
	if lis!=[]:
		temp_lis=lis[:]
		while len(temp_lis)>100:
			myurl.set_expr(myurl.combine_with_and(myurl.set_id(temp_lis[0:100]),"RId="+str(id2)))
			myurl.set_attributes(['Id'])
			data=gd.get_dict(myurl.get_url())
			data=data['entities']
			for d in data:
				res.append=[id1,d['Id'],id2]	
			temp_lis=temp_lis[100:]
		if len(temp_lis)>=1:
			myurl.set_expr(myurl.combine_with_and(myurl.set_id(temp_lis),"RId="+str(id2)))
			myurl.set_attributes(['Id'])
			data=gd.get_dict(myurl.get_url())
			data=data['entities']
			for d in data:
				res.append=[id1,d['Id'],id2]
	AUID_ID_THREE_HOP(id1,id2,d1,d2,lis)
def AUID_ID_THREE_HOP(id1,id2,d1,d2,lis):
	#AA.AuId->AA.AfId->AA.AuId->Id
	dd_2=d2['AA']
	d1_AfId=[]
	d1_RID=[]
	RID_3=[]
	dic_d1ID_RId=[]
	d1_ID_ALL=[]
	d2_ALL=[]
	consist=[]
	for dd_1 in d1:
		for rid in dd_1['RId']:
			if rid!="":
				d1_RID.append(rid)
				dic_d1ID_RId.append([dd_1['Id'],rid])
		for d in dd_1['AA']:
			if str(d['AuId'])==str(id1):
				if d.has_key('AfId'):
					d1_AfId.append(d['AfId'])
			d1_ID_ALL.append([dd_1['Id'],d['AuId']])
		if dd_1.has_key('C'):
			d = dd_1['C']
			if d!=[]:
				d1_ID_ALL.append([dd_1['Id'],d['CId']])
		if dd_1.has_key('F'):
			for d in dd_1['F']:
				if d.has_key('FId'):
					d1_ID_ALL.append([dd_1['Id'],d['FId']])
		if dd_1.has_key('J'):
			d= dd_1['J']
			if d!="":
				d1_ID_ALL.append([dd_1['Id'],d['JId']])
	consist=[]
	for d in dd_2:
		if d.has_key('AfId'):
			if d['AfId'] in d1_AfId:
				print 'AA.AuId->AA.AfId->AA.AuId->Id'
				res.append(long(id1),d1_AfId,d['AuId'],long(id2))

	#AA.AuId->Id->RId->RId(AA.AuId->1.c))
	RID_3=RID_id2(d1_RID,id2)
	if RID_3!=[]:
		for d in dic_d1ID_RId:
			if d[1] in RID_3:
				print 'AA.AuId->Id->RId->RId'
				res.append([long(id1),d[0],d[1],long(id2)])
	#AA.AuId->Id->AA.AuId(F.Fid/J.JId/C.CId)->Id
    
	d2_ALL,no=get_sigle_id_attribute_list(d2)#********#
	print d2_ALL
	for d in  d1_ID_ALL:
		if d[1] in d2_ALL:
			print 'AA.AuId->Id->AA.AuId(F.Fid/J.JId/C.CId)->Id'
			res.append([long(id1),d[0],d[1],long(id2)])
def AUID_AUID_two_HOP(id1,id2,d1,d2):
	#AA.AuId->AA.AfId->AA.AuId
	AFID_ID1=[]
	AFID_ID2=[]
	paperID_ID1=[]
	paperID_ID2=[]
	# print d1
	AFID_ID1,paperID_ID1=get_AfID_ID(d1,id1)
	AFID_ID2,paperID_ID2=get_AfID_ID(d2,id2)
	for d in set(AFID_ID1).intersection(set(AFID_ID2)):
		print 'AA.AuId->AA.AfId->AA.AuId'
		res.append([long(id1),d,long(id2)])
	for d in set(paperID_ID1).intersection(set(paperID_ID2)):
		print 'AA.AuId->AA.AfId->AA.AuId'
		res.append([long(id1),d,long(id2)])
	AUID_AUID_THREE_HOP(id1,id2,d1,d2,paperID_ID1,paperID_ID2)
def AUID_AUID_THREE_HOP(id1,id2,d1,d2,paperID_ID1,paperID_ID2):
	#AA.AuId->Id->RId-> AA.AuId
	pId=paperID_ID1
	while len(pId)>100:
		myurl.set_expr(myurl.set_id(pId[0:100]))
		myurl.set_attributes(['RId','Id'])
		data=gd.get_dict(myurl.get_url())
		ID_RID_lis=get_ID_RID_pair(data['entities'])
		for paperId in ID_RID_lis:
			if paperId[1] in paperID_ID2:
				res.append([long(id1),paperId[0],paperId[1],long(id2)])
		pId=pId[100:]
	myurl.set_expr(myurl.set_id(pId))
	myurl.set_attributes(['RId','Id'])
	data=gd.get_dict(myurl.get_url())
	ID_RID_lis=get_ID_RID_pair(data['entities'])
	for paperId in ID_RID_lis:
		if paperId[1] in paperID_ID2:
			print 'AA.AuId->Id->RId-> AA.AuId'
			res.append([long(id1),paperId[0],paperId[1],long(id2)])
def ID_AUID_ONE_HOP(id1,id2,d1,d2):
	#Id-> AA.AuId
	ID1_AUID=[]
	if d1 !=[]:
		for d in d1['AA']:
			ID1_AUID.append(d['AuId'])
		if id2 in ID1_AUID:
			print 'Id-> AA.AuId'
			res.append([long(id1),long(id2)])
def ID_AUID_TWO_HOP(id1,id2,d1,d2):
	myurl.set_attributes(['Id'])
	#Id->RId->AA.AuId
	d1_RId=d1['RId']
	while len(d1_RId)>100:
		myurl.set_expr(myurl.combine_with_and(myurl.set_id(d1_RId[0:100]),"Composite(AA.AuId="+id2+")"))
		data=gd.get_dict(myurl.get_url())
		data=data['entities']
		for d in data:
			print 'Id->RId->AA.AuId'
			res.append([long(id1),d['id'],long(id2)])
		d1_RId=d1_RId[100:]
	if len(d1_RId)>1:
		myurl.set_expr(myurl.combine_with_and(myurl.set_id(d1_RId),"Composite(AA.AuId="+id2+")"))
		data=gd.get_dict(myurl.get_url())
		data=data['entities']
		for d in data:
			print 'Id->RId->AA.AuId'
			res.append([long(id1),d['id'],long(id2)])
def ID_AUID_THREE_HOP(id1,id2,d1,d2):
	myurl.set_attributes()
	#Id->AA.AuId(F.Fid/J.JId/C.CId)->Id->AA.AuId
	print  'three hop'
	id1_attr,d1_list=get_sigle_id_attribute_list(d1)
	ID2_ID=[]
	AUID_list=[]
	FID_list=[]
	JID_list=[]
	CID_list=[]
	for d in d2:
		ID2_ID.append(d['Id'])
	if ID2_ID==[]:
		pass
	elif d1_list==[]:
		pass
	else:
		operator={'AA.AuId':AUID_list,'F.FId':FID_list,'J.JId':JID_list,'C.CId':CID_list}	
		for d in d1_list:
			operator.get(d[0]).append(d[1])
		ID2_ID_2=ID2_ID
		myurl.set_attributes(['AA.AuId','F.FId','J.JId','C.CId','Id'])
		while len(ID2_ID_2)>90:
			myurl.set_expr(myurl.combine_with_and(myurl.get_A_F_J_C(d1_list),myurl.set_id(ID2_ID_2[0:90])))
			data=gd.get_dict(myurl.get_url())
			get_attr_id_pair(AUID_list,FID_list,JID_list,CID_list,data,id1,id2)
			ID2_ID_2=ID2_ID_2[90:]
		if len(ID2_ID_2)>1:
			myurl.set_expr(myurl.combine_with_and(myurl.get_A_F_J_C(d1_list),myurl.set_id(ID2_ID_2)))
			data=gd.get_dict(myurl.get_url())
			get_attr_id_pair(AUID_list,FID_list,JID_list,CID_list,data,id1,id2)
	myurl.set_attributes()
	#Id->RId->RId->AA.AuId
	ID1_RID=d1['RId']
	RID_RID_LIST=[]
	if ID1_RID!=[]:
		if ID2_ID!=[]:
			while len(ID1_RID)>100:
				myurl.set_expr(myurl.set_id(ID1_RID[0:100]))
				myurl.set_attributes(['RId','Id'])
				data=gd.get_dict(myurl.get_url())
				data=data['entities']
				RID_RID_LIST=get_ID_RID_pair(data)
				for d in RID_RID_LIST:
					if d[1] in ID2_ID:
						print 'Id->RId->RId->AA.AuId'
						res.append([long(id1),d[0],d[1],long(id2)])
				ID1_RID=ID1_RID[100:]
			if len(ID1_RID)>1:
				myurl.set_expr(myurl.set_id(ID1_RID))
				myurl.set_attributes(['RId','Id'])
				data=gd.get_dict(myurl.get_url())
				data=data['entities']
				RID_RID_LIST=get_ID_RID_pair(data)
				for d in RID_RID_LIST:
					if d[1] in ID2_ID:
						print 'Id->RId->RId->AA.AuId'
						res.append([long(id1),d[0],d[1],long(id2)])
	#Id-> AA.AuId -> AA.AfId ->AA.AuId
	AFID_ID2,paperID_ID2=get_AfID_ID(d2,id2)
	myurl.set_attributes(['AA.AuId,AA.AfId','Id'])
	myurl.set_expr('Composite('+myurl.get_Or_AUID(AUID_list)+')')
	data=gd.get_dict(myurl.get_url())
	dd2=data['entities']
	AFID_ID1=get_dict_AfId_Id(dd2,AUID_list)
	for l in AUID_list:
		try:
			for d in set(AFID_ID1[l]).intersection(set(AFID_ID2)):
				res.append([long(id1),l,d,long(id2)])
		except:
			pass
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
	print id1,id2
	res[:]=[]
	hop_type=0
	if reslist.has_key(str(id1)+"+"+str(id2)):
		print 'hahah'
		return reslist[str(id1)+"+"+str(id2)]
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
		if len(data['entities'])>=1:
			d1=data['entities'][0]
		else:
			d1=[]
		hop_type=hop_type+1
	if d2==[]:
		myurl.set_attributes()
		myurl.set_expr('Id='+id2)
		data=gd.get_dict(myurl.get_url())
		if len(data['entities'])>=1:
			d2=data['entities'][0]
		else:
			d2=[]
		hop_type=hop_type+2
	operator={0:AuId_AuId_get_hop,1:id_AuId_get_hop,2:AuId_Id_get_hop,3:id_id_get_hop}
	operator.get(hop_type)(id1,id2,d1,d2) 
	s='路径条数'
	print '路径条数为：'+str(len(res))
	reslist[str(id1)+"+"+str(id2)]=res[:]
	return res
		



