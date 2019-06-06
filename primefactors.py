#christinajoice
import sympy
n=int(input())
s=[]
for i in range(2,n+1):
  if n%i==0 and sympy.isprime(i):
    s.append(str(i))
print(' '.join(s))
