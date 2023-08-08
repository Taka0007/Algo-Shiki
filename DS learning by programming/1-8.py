import numpy as np
N = int(input())
A = list(map(int,input().split()))
mean_A = np.mean(A)
B = [num - mean_A for num in A]
print(*B, sep=' ')