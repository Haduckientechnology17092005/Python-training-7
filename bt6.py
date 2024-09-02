def bt1(n):
    if n == 1:
        return 1/2
    else:
        return 1/(2*n) + bt1(n-1)
    
n = int(input("Enter a number: "))
print(bt1(n))

def bt2(n):
    if n == 1:
        return 1
    else:
        return n**2 + bt2(n-1)

n = int(input("Enter a number: "))
print(bt2(n))

def bt3(n):
    if n == 1:
        return 3**(1/2)
    else:
        return ((3*n) + bt3(n-1))**(1/2)
    
n = int(input("Enter a number: "))
print(bt3(n))