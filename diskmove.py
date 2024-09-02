def DiskMove(n,c1,c2,c3):
    if n == 1:
        print("Move disk from",c1,"to",c2)
    else:
        DiskMove(n-1,c1,c3,c2)
        DiskMove(1,c1,c2,c3)
        DiskMove(n-1, c3,c2,c1)

print("Enter the number of disks")
n = int(input("Enter the number of disks: "))
print("The sequence of moves involved in the Tower of Hanoi are")
DiskMove(n,1,2,3)