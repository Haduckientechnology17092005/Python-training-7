def iterativefactorial(n):
    result = 1
    for i in range (2, n+1):
        result *= i
    return result

n = int(input("Enter a number: "))
for i in range(n+1):
    print(i, iterativefactorial(i))