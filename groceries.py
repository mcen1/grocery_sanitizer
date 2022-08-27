#!/bin/env python3

import json
maxcount=3 
f = open('mastergroceries.json')
file1 = open('list.txt', 'r')

grocerylist = file1.readlines()
storedata = json.load(f)
tobuy={}
for item in grocerylist:
  found=False
  item=item.lower().replace('\n','')
  for product in storedata:
    #for zapo in storedata[product]:
        #print(f"'{item}' vs '{zapo}'")
    if str(item.lower()) in storedata[product]:
      if product not in tobuy:
        tobuy[product]=[]
      tobuy[product].append(item.lower())
      found=True
  if not found:
    if "unknown" not in tobuy:
      tobuy["unknown"]=[]
    tobuy["unknown"].append(item.lower())
for item in tobuy:
    print(f"{item}\n")
    count = 0
    tosay=""
    for thing in tobuy[item]: 
      count=count+1
      tosay=tosay+(f"[ ]{thing} ")
      if count>maxcount:
          count=0
          tosay=f"{tosay}\n"
    print(tosay)
    print(f"\n")
     
