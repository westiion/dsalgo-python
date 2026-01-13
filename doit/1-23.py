# 왼쪽/오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

# 왼쪽
n=int(input("짧은 변의 길이를 입력하세요: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()

#오른쪽 
for i in range(n,0,-1):
    print(' '*(i-1)+'*'*(n-i+1))
    