import string
#アルファベット一覧
alfa = [chr(i) for i in range(97, 97+26)]

#入力
S = input()
ans = 1

for i in range(len(S)):
    ans *= (alfa.index(S[i]))+1

print(ans)