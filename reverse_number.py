def reverse_number(n, result=0):
    if n == 0:
        return result
    else:
        last = n%10
        result = result*10 + last
        return reverse_number(n//10, result)
    
n = int(input("Enter a number: "))
print("Reverse number:", reverse_number(n))