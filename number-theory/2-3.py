# エラトステネスの篩
# Nまでの素数を列挙する
def prime_sieve(N):
    
    # Nまでの数列を作成。Trueならその数字は素数。
    num = [True]*(N+1)
    
    # 0,1は素数でないので1にしておく
    num[0] = False
    num[1] = False
    # 1～Nまでの範囲を走査。
    # 1-indexで考えます。 (ex:1はnum[1],77はnum[77])
    for i in range(2,N+1):
        if num[i]:
            # iが素数である場合、iの倍数のフラグを全て1に変更する
            for j in range(2*i, N+1, i):
                num[j] = False
    return num

N   = int(input())
num = prime_sieve(N+2)

ans = sum(num[:N+1])
print(ans)