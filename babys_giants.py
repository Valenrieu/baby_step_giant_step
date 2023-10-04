from math import sqrt, gcd, ceil
import datetime as dt

def inv_mod(a, b):
    """Returns modular inverse of a mod b.
    returns None if a is not invertible i.e. pgcd(a,b)!=1"""
   
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

def babys_giants(n, alpha, beta):
    """Implementation of baby step giant step algorithm"""
    tableh = dict()
    m = ceil(sqrt(n))+1
    
    for j in range(m):
        baby = pow(alpha, j, n)
        tableh[baby] = j
    
    inv = inv_mod(alpha**m, n)

    if inv is None:
        alpha = str(alpha)
        n = str(n)
        raise ValueError(f"{alpha} is not invertible modulus {n}")

    y = beta

    for i in range(m):
        if y in tableh:
            return i*m+tableh[y]

        else:
            y = (y*inv)%n

def bsgs(n, a, b=1):
    start = dt.datetime.now()
    x = babys_giants(n, a, b)
    print("x =", x)
    end = dt.datetime.now()
    time = end-start
    print("Commputation time :", time)

    if not x is None:
        print("Checking x value...")
        verif = pow(a, x, n)

        if verif==b:
            print("Correct value of x")

        else:
            print("Incorrect value of x")

    else:
        print("No value found for x...")
