base = 2

def square(n):
    return base ** n
    
if __name__== '__main__': # 파이썬에서 직접 실행하면 dir 에 __name__ 이 __main__ 이 된다.
    print(base)           # 매우 많이쓰는 코드이다.
    print(square(10))