s=input()
d={}
for i in s:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
max_key = max(d, key=lambda k: d[k])
print(max_key)
