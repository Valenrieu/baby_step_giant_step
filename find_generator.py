def isgenerator(n, g):
    """Check if g is a generator of (Z/nZ, X)^X"""
    numbers = set()

    for i in range(n):
        numbers.add(pow(g, i, n))

    if len(numbers)+1==n:
        return True
    
    return False

def findgenerator(n):
    """Find all generators of (Z/nZ, X)^X"""
    for i in range(n):
        numbers = set()

        for j in range(n):
            numbers.add(pow(i, j, n))

        if len(numbers)+1==n:
            print(i)
