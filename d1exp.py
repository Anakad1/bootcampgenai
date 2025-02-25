import numpy as np

#exercice 1 
array_ex1 = np.arange(10)
print("Exercice 1:")
print(array_ex1)  



#Exercice 2 
#convertir une liste en tableau NumPy et changer son type de données en entier.
liste_ex2 = [3.14, 2.17, 0, 1, 2]
array_ex2 = np.array(liste_ex2, dtype=int)
print("\nExercice 2:")
print(array_ex2)  



#exercice 3 
#creer un tableau NumPy 3x3 avec des valeurs allant de 1 à 9.
array_ex3 = np.arange(1, 10).reshape(3, 3)
print("\nExercice 3:")
print(array_ex3)  



#exercice 4 
#creer un tableau NumPy 2D de forme (4, 5) rempli de nombres aléatoires (entre 0 et 1).
array_ex4 = np.random.rand(4, 5)
print("\nExercice 4:")
print(array_ex4)



#exercice 5 

array_ex5 = np.array([[21, 22, 23, 22, 22],
                      [20, 21, 22, 23, 24],
                      [21, 22, 23, 22, 22]])
second_row = array_ex5[1]
print("\nExercice 5:")
print(second_row)



#exercice 6 
#inverser l'ordre des éléments dans un tableau NumPy 1D (le premier élément devient le dernier).
array_ex6 = np.arange(10)[::-1]
print("\nExercice 6:")
print(array_ex6)



#exercice 7 
#crer une matrice d'identité 4x4 à l'aide de NumPy.
array_ex7 = np.eye(4)
print("\nExercice 7:")
print(array_ex7)



#exercice 8 
#trouver la somme et la moyenne d'un tableau 1D donné.
array_ex8 = np.arange(10)  # De 0 à 9
sum_ex8 = np.sum(array_ex8)
avg_ex8 = np.mean(array_ex8)
print("\nExercice 8:")
print("Sum:", sum_ex8, ", Average:", avg_ex8)



#exercice 9 
array_ex9 = np.arange(1, 21).reshape(4, 5)
print("\nExercice 9:")
print(array_ex9)



#exercice 10 : Sélection conditionnelle de valeurs
#extraire tous les nombres impairs d'un tableau NumPy donné.
array_ex10 = np.arange(10)
odd_numbers = array_ex10[array_ex10 % 2 == 1]
print("\nExercice 10:")
print(odd_numbers)

