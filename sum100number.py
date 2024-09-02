def sum100number(n, sum):
    if n<1:
        return sum
    else:
        return sum100number(n-1, sum+n)
    
n = int(input())
print(sum100number(n, 0))