def generatebinarysquences(n, sequence=[]):
    if len(sequence) == n:
        print(sequence)
        return
    else:
        generatebinarysquences(n, sequence + [0])
        generatebinarysquences(n, sequence + [1])

generatebinarysquences(3)