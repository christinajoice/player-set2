#christinajoice
s=list(input())
l=[]
d={'X':'A','Y':'B','Z':'C','x':'a','y':'b','z':'c'}
for i in s:
  if i in d:
    l.append(d[i])
  else:
    l.append(chr(ord(i)+3))
print(''.join(l))
