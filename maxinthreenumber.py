def maxinthreenumber(n1, n2, n3):
    def maxoftwo(n1, n2):
        return n1 if n1 > n2 else n2
    def maxofthree(n1, n2, n3):
        return maxoftwo(n1, maxoftwo(n2, n3))
    return maxofthree(n1, n2, n3)

a,b,c = int(input("Enter the first number: ")), int(input("Enter the second number: ")), int(input("Enter the third number: "))
print(maxinthreenumber(a, b, c))