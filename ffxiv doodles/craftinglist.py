with open('itemlists') as f:
  read_data = f.read().split('\n')

import pprint 

oneex = "\"Serge Hat of Aiming\",1,craft,\"Lv. 66 WVR\" "
crafted = ",1,craft,\"Lv. 6"


def process(itemm):
  if crafted in itemm:
    print(itemm," was skipped")
    return "skip"
  elif crafted not in itemm:
    lis = itemm.split(",")
    #print(lis)
    name = lis[0][2:-2]
    #print(name)
    amount = int(lis[1])
    return name,amount

#print(process(oneex))

d = dict()
def findtotal(iteml):
  for item in iteml:
    #print(item)
    x = process(item)
    #print(x)
    if x != "skip": 
      if x[0] in d:
        d[x[0]] += x[1]
      elif x[0] not in d:
        d[x[0]] = x[1]
  c = dict()
  for key in d.keys():
    if d[key]>1:
      c[key] = d[key]  
  return c

m = findtotal(read_data)

for key in m.keys():
  print(key,m[key])
#print(findtotal(read_data))