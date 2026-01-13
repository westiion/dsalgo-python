# 1부터 n까지 정수 합 구하기(양수만 받기)
while True:
    n=int(input("n 입력: "))
    if n<=0:
        break
    total=0
    for i in range(1,n+1):
        total+=i
print(total)

# 가우스 덧셈 
while True:
    n=int(input("n 입력: "))
    if n<=0:
        break
    total=n*(n+1)/2

print(total)
