def prime(b):
  if(b==0 or b==1):
    return False
  for h in range(2,b//2+1):
    if(b%h==0):
       return False
  return True
n= int(input())
for i in range(n):
  c=[]
  a=[]
  s=int(input())
  for j in range(s-5,s+5):
    if(prime(j)==True):
       c.append(j)
       a.append(abs(j-s))
  x=min(a)
  k=a.index(x)
  print(c[k])
  