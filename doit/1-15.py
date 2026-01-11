n=int(input("n개수: "))
w=int(input("w개수:"))

for _ in range(n//w):
    print('*'*w)

print('*'*(n%w))