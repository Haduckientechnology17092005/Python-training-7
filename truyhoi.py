def truyhoi(n):
    if n == 0:
        return 1
    else:
        return sum((n-i)**2*truyhoi(i) for i in range(n))
n = int(input("Enter a number: "))
print(truyhoi(n))