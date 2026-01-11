# +와 -를 번갈아 출력하기

n=int(input("출력 개수"))
for i in range(n//2):
    print('+-',end="")

if n%2:
    print('+')