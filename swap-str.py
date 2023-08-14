d=input()
k=[]
for i in range(len(d)):
  k.append(d[i])
a=0
b=1
for i in range(len(k)):
    if a<len(k)-1:
          c=k[a]
          k[a]=k[b]
          k[b]=c
          a=b+1
          b=a+1
    else:
        break
for i in range(len(k)):
    print(k[i],end='')
