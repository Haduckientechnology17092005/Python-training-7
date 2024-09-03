import itertools

def partitions(s):
    if len(s) == 1:
        yield [s]
        return
    first = s[0]
    for smaller in partitions(s[1:]):
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[first] + subset] + smaller[n+1:]
        yield [[first]] + smaller
        
s = [1, 2, 3]
partition_list = list(partitions(s))
for partition in partition_list:
    print([set(p) for p in partition])
