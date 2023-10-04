babys_giants.py file implements baby step giant step algorithm. There is also a function called
inv_mod to compute modular inverse of two integers.

Ex:
```python
>>> inv_mod(3, 11) # modular inverse of 3 mod 11
4
```

babys_giants function solves a^x = b mod n equations. Usage : babys_giants(n, a, b)

Ex, solve $5^x \equiv 17 [23]$:
```python
>>> babys_giants(23, 5, 17)
17
```

bsgs function solves the equation, then it checks the value and print time of computation.
The usage is the same as babys_giant.

Ex:
```python
>>> bsgs(21, 3, 17)
Temps d'execution : 0:00:00.000092
Verification de la valeur de x...
Valeur de x correcte
```

find_generator.py file allows us to check if a given integer is a generator of a cyclic group
or to find all generators of a group.

Ex, check if 7 is a generator of $(\mathbb{Z}/21\mathbb{Z}^*, \times)$:
```python
>>> isgenerator(21, 7)
False
```

Ex, find all generators of $(\mathbb{Z}/21\mathbb{Z}^*, \times)$:
```python
>>> findgenerator(7)
3
5
```

These two functions shouldn't be used, especially for a big modulus and the last one shoudldn't be used at all.
