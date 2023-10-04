Le fichier projetbsgs.py implement l'algorithme de baby step giant step, on peut trouver 
l'inverse modulaire de deu entiers avec la fonction inv_mod

Ex : 
inv_mod(3, 11) #inverse modulaire de 3 mod 11

babys_giants resoud une equation du type a^x = b mod n, on l'utilise comme ca : babys_giants(n, a, b)

Ex : babys_giants(21, 3, 17)

bsgs resoud l'equation, teste la valeur de x et affiche le temps d'execution, elle s'utilise pareillement

Ex : bsgs(21, 3, 17)

Le fichier find_generator.py permet de verifier si un generateur en est bien un ou de trouver les
generateurs

Ex:
isgenerator(21, 7) #verifie si 7 est un generateur de (Z/21Z*, x)

Ex:
findgenerator(21) #trouve tous les generateurs de (Z/21Z*, x)

Ces deux fonctions sont à déconseiller pour des gros nombres, surtout la derniere fonction