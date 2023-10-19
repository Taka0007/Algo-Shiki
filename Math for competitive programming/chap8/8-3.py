A,K = map(int,input().split())

if A==0:
    ans = -1
elif A%(K+1)==0:
    ans = (A//(K+1))*K
else:
    ans = -1

print(ans)