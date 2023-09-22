Q = int(input())
num_list = [3,1,4,1,5,9,2,6,5,3]

for i in range(Q):
    query = list(map(int,input().split()))

    if query[0]==0:
        print(num_list[query[1]])
    else:
        num_list[query[1]] = query[2]