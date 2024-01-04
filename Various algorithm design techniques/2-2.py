# input
N,M = map(int,input().split())

# calculate
def f(X,N):
    result = N+1
    for i in range(5):
        result = result*X + 1
    return result

right = 100
left  = 0

while right - left > 10**(-3):
    mid = (right + left)/2
    if f(mid,N) <= M:
        left = mid
    else:
        right = mid

# output
print(right)