n = int(input("Enter a number: "))
def giaithua(n):
    if n == 0:
        return 1
    else:
        return n*giaithua(n-1)
    
print(giaithua(n))