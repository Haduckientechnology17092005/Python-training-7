def r_max(arg):
    largest = None
    first_time = True
    for e in arg:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e
        if first_time or val > largest:
            largest = val
            first_time = False
    return largest
print("Max trong cau truc 1:", r_max([1, 2,[3,6,9,100], 3, 4, 5]))
print("Max trong cau truc 2: ", r_max(["Kien",["Hoang, Hao"], "Dung"]))
print("Max trong cau truc 3: ",r_max([[[1,17], 90],2,[1,100],8,6]))