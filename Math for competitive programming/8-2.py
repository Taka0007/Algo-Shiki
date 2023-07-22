A = int(input())

if A==0:
    ans = -1
elif A%3==0:
    ans = (A//3)*2
else:
    ans = -1

print(ans)