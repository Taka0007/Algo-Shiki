import statistics
N = int(input())
A = list(map(int,input().split()))
mode_A = statistics.multimode(A)
mode_A.sort()
for S in mode_A:
    print(S)