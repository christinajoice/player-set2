s=input()
d={}
for i in s:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
for i in d:
  if max(d[i].value())==true:
    print(d[i].keys())
