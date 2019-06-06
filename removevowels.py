n=int(input())
s=input()
if n==len(s):
  s=s.translate({ord(i):None for i in 'aeiou'})
  print(s[::-1])
