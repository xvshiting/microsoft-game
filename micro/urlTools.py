url_head="http://oxfordhk.azure-api.net/academic/v1.0/evaluate?subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6"
expr="&expr="
Id="Id="
And="&"
COUNT="&count="
OFFSET="&offset"
attributes="&attributes=Id,AA.AuId,AA.AfId,C.CId,RId,F.FId,J.JId"
attr=['Id','AA.AuId','AA.AfId','C.CId','RId','F.FId','J.JId']
class urlTools:
	expr="2140251882"
	attribute="Id,AA.AuId,AA.AfId,C.CId,RId,F.FId,J.JId"
	offset="0"
	count="10000"
	
	def __set_expr_e__(self,type='Or',**other_id):
		ss="123456789"
		for t in other_id:
			dg=other_id[t]
			for d in dg:
				ss=ss+t+"="+str(d)+","
		self.expr=type+"("+ss[:-1]+")"
		return self.expr

	def type_and(self,**other_id):
		return self.__set_expr_e__("And",**other_id)

	def type_or(self,**other_id):
		return self.__set_expr_e__(**other_id)

	def combine_with_and(self,a,b):
		return "And("+a+","+b+")"


	def combine_with_Or(self,a,b):
		return "Or("+a+","+b+")"

	def combine_with_composite(self,a):
		return "Composite("+a+")"

	def set_id(self,new_id):  
		if new_id!=[]: 
			d={'Id':new_id}
			ss='Id='+str(new_id[0])
			if len(new_id)>1:
				new_id=new_id[1:]
				for i_d in new_id:
					ss='Or('+ss+','+"Id="+str(i_d)+')'
			self.expr=ss
			return ss
		

		#print self.expr

	def set_attributes(self,attributes=attr):
		ss=""
		for a in attributes:
			ss=ss+a+","
		self.attribute=ss[:-1]

	def set_offset(self,offset=0):
		self.offset=offset

	def set_count(self,count=10000):
		self.count=count

	def set_composites(self,**other_id):
		ss=""
		for t in other_id:
			dg=other_id[t]
			for d in dg:
				ss=ss+self.combine_with_composite(t+"="+"'"+d+"'")+","
				
		return ss[:-1]

	def set_expr(self,a):
		self.expr=a



	def get_url(self):   
		return url_head+"&expr="+self.expr+"&count="+self.count+"&offset="+self.offset+"&attributes="+self.attribute

	def get_A_F_J_C(self,lis):
		ss=""
		l_1=lis[0]
		ss="Composite("+str(l_1[0])+"="+str(l_1[1])+")"
		if len(lis)>1:
			lis=lis[1:]
			for l in lis:
				ss=self.combine_with_Or(ss,"Composite("+str(l[0])+"="+str(l[1])+")")

		return ss
	def get_OR_RId(self,new_id):
		ss='RId='+str(new_id[0])
		if len(new_id)>1:
			new_id=new_id[1:]
			for i_d in new_id:
				ss='Or('+ss+','+"RId="+str(i_d)+')'
		return ss

	
	
	
if __name__ == '__main__':
	uu=urlTools();
	d={"Id":['111','222'],"AuId":['111','222']}
	#uu.set_expr_e(**d)
	# print uu.type_or(**d)
	#Composite(And(AA.AuN='mike smith',AA.AfN='harvard university'))
	dd={"AA.AuN":['mike smith','djsdj','dsds'],'AA.AfN':['harvard university']}
	# print uu.combine_with_composite(uu.type_and(**dd))
	# print uu.set_composites(**dd)
	d=['123','123','123']
	uu.set_id(d)
	print uu.expr
	# print uu.attribute
	# print uu.get_url()
