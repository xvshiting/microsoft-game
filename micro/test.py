import get_hop as gp 
import json

# print json.dumps(gp.get_hop('2018949714','2105005017'))
# print json.dumps(gp.get_hop('2153635508','2126125555'))
print json.dumps(gp.get_hop('2251253715','2180737804'))
print json.dumps(gp.get_hop('2147152072','189831743'))
print json.dumps(gp.get_hop('2332023333','2310280492'))
print json.dumps(gp.get_hop('2332023333','57898110'))
print json.dumps(gp.get_hop('57898110', '2014261844'))
# print json.dumps(gp.get_hop('2126125555','2153635508'))

# print gp.get_hop('2100837269','621499171')
# print gp.get_hop('2030985472','2133644056')
# http://localhost/?id1=2147152072&id2=189831743
# http://localhost/?id1=2251253715&id2=2180737804
# http://localhost/?id1=2332023333&id2=2310280492
# http://localhost:8080/?id1=2332023333&id2=57898110
# http://localhost/?id1=57898110&id2=2014261844
