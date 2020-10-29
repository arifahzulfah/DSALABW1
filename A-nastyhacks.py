n=int(input())
list=[]
for _ in range(n):
  r,e,c=map(int,input().split())
  if r>e-c:
    list.append("do not advertise")
  elif r<e-c:
    list.append("advertise")
  else:
    list.append("does not matter")
for a in range(n):
  print(list[a])