def Ackermann(m,n):
    if m == 0:
        return n + 1
    elif n == 0 and m > 0:
        return Ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return Ackermann(m - 1, Ackermann(m, n - 1))
    
n = int(input("Enter a number n: "))
m = int(input("Enter a number m: "))
print(Ackermann(m,n))