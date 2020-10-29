n=int(input())
list=[]
for a in range(n):
  k=int(input())
  count=0
  if k==0:
    count=count+1
  while(k>0):
    count=count+1
    k=k//10
  list.append(count)
for b in range(n):
  print(list[b])