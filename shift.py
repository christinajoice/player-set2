n,k=map(int,input().split())
l=list(input().split())
sub=l[:-k-1:-1]
sub.reverse()
l=l[:len(l)-k]
for i in range(len(sub)):
  l.insert(i,sub[i])
print(' '.join(l))
