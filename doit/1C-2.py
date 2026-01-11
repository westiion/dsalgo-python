# 세 정수를 입력받아 중앙값 구하기

def mid1(a,b,c):
    if a>=b:
        if b>=c:
            return b
        elif c>=a:
            return a
        else:
            return c
    # b>a
    elif a>=c:
        return a
    # b>a c>a
    elif b>=c:
        return c
    else:
        return b
    

def mid2(a,b,c):
    if a>=b:
        if b>=c:
            return b
        elif c>=a:
            return a
        else:
            return c
    # b>a
    elif a>c:
        return a
    # b>a c>=a
    elif b>c:
        return c
    else:
        return b
    

print(mid1(2,3,1),mid2(5,4,5))