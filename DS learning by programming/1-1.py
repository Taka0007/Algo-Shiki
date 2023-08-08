N = int(input())
num = list(map(int,input().split()))
a=0
b=0
c=0
d=0
e=0

for i in range(N):
    if num[i]<=20:
        a+=1
    elif num[i]<=40:
        b+=1
    elif num[i]<=60:
        c+=1
    elif num[i]<=80:
        d+=1
    else:
        e+=1
print(a,b,c,d,e, sep="\n")