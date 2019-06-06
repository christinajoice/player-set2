n=int(input())
li=input().split()
for i in range(len(li)):
  for j in range(len(li)):
    if li[i]==li[j]:
      li.pop(i)
      li.pop(j)
      break
print(li)
