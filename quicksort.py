def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print("Enter the list: ")
arr = []
for i in range(int(input("Enter the number of elements: "))):
    arr.append(int(input("Enter the element: ")))
print("Sorted list: ")
print(quicksort(arr))