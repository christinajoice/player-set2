l,r=map(int,input().split())
if l>r:
  great=l
else:
  great=r
while(True):
  if great%l==0 and great%r==0:
    lcm=great
    break
  great=great+1
print(lcm)
