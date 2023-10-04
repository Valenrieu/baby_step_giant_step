#permet de trouver les generateurs de Z/nZ
def isgenerator(n, g):
    nombres = set()

    for i in range(n):
        nombres.add(pow(g, i, n))

    if len(nombres)+1==n:
        return True
    
    return False

def findgenerator(n):
    for i in range(n):
        nombres = set()

        for j in range(n):
            nombres.add(pow(i, j, n))

        if len(nombres)+1==n:
            print(i)
