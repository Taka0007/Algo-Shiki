N,M = map(int,input().split())
ans = 0

for x in range(1,N+1):
    for y in range(1,N+1):
        if M - (x+y) >= 1:
            ans += (M - (x+y))
print(ans)