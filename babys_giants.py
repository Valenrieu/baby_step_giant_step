from math import sqrt, gcd, ceil
import datetime as dt

# Calcul de l'inverse modulaire utilisant l'algorithme d'euclide etendu

def inv_mod(a, b):
    """retourne l'inverse de a modulo b
    retourne None s'il n'est pas inversible i.e. pgcd(a,b)!=1"""
   
    r, u, v, rr, uu, vv = a, 1, 0, b, 0, 1

    if gcd(a, b)==1:
        while rr!=0:
            q = r//rr
            r, u, v, rr, uu, vv = rr, uu, vv, r-q*rr, u-q*uu, v-q*vv

        if u<0:
            u += b
        
        return u

    else:
        return None

# Algorithme de baby step giant step

def babys_giants(n, alpha, beta):
    tableh = dict()
    m = ceil(sqrt(n))+1
    
    for j in range(m):
        baby = pow(alpha, j, n)
        tableh[baby] = j
    
    inv = inv_mod(alpha**m, n)

    if inv is None:
        alpha = str(alpha)
        n = str(n)
        raise ValueError(f"{alpha} n'est pas inversible modulo {n}")

    y = beta

    for i in range(m):
        if y in tableh:
            return i*m+tableh[y]

        else:
            y = (y*inv)%n

# Essaie de resoudre en utilisant l'algorithme du haut, affiche le temps
# avec les micro secondes et verifie la valeur trouvee

def bsgs(n, a, b=1):
    debut = dt.datetime.now()
    x = babys_giants(n, a, b)
    print("x =", x)
    fin = dt.datetime.now()
    temps = fin-debut
    print("Temps d'execution :", temps)

    if not x is None:
        print("Verification de la valeur de x...")
        verif = pow(a, x, n)

        if verif==b:
            print("Valeur de x correcte")

        else:
            print("Valeur de x incorrecte")

    else:
        print("Pas de valeur trouvee...")
