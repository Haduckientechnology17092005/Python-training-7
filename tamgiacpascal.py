def pascal_triangle_right(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    for row in triangle:
        print(' '.join(map(str, row)))

n = int(input("Enter the number of rows: "))
pascal_triangle_right(n)
def pascal_triangle_equilateral(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    max_width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        row_str = ' '.join(map(str, row))
        print(row_str.center(max_width))

n = int(input("Enter the number of rows: "))
pascal_triangle_equilateral(n)
