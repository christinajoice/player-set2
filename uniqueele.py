n=int(input())
li=list(map(int,input().split()))
d={}
for i in li:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
for i in d:
  if d[i]==1:
    print(i)
