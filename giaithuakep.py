def solution(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * solution(n - 2)

def sumgiaithua(n):
    if n == 0:
        return 1
    else:
        return sum(solution(i) * (-1) ** (i-1) for i in range(1, n+1))

n = int(input("Enter a number: "))
print("Solution (double factorial):", solution(n))
print("Sumgiaithua:", sumgiaithua(n))
