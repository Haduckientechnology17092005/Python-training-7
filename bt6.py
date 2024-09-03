import math
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

def bt4(n):
    if n == 2:
        return pow(2,1/2)
    else:
        return pow(n,1/n) + bt4(n-1)

n = int(input("Enter a number: "))
print(bt4(n))

def bt5(n):
    if n == 1:
        return 1
    else:
        return pow(n+bt5(n-1),1/(n+1))
    
n = int(input("Enter a number: "))
print(bt5(n))

def bt6(n):
    if n == 1:
        return 1
    else:
        return pow(n+bt6(n-1),1/2)
    
n = int(input("Enter a number: "))
print(bt6(n))

def giaithua(n):
    if n == 0:
        return 1
    else:
        return n*giaithua(n-1)
def bt7(n):
    if n == 1:
        return 1
    else:
        return pow(giaithua(n) + bt7(n-1),1/(n+1))
    
n = int(input("Enter a number: "))
print(bt7(n))

def bt8(x,n):
    if n==1:
        return x
    else:
        return (pow(x,n)/giaithua(n) + bt8(x,n-1))

x = int(input("Enter a number: "))
n = int(input("Enter a number: "))
print(bt8(x,n))