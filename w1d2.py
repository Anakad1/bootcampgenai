#DAILY CHALLENGE 

word = input("Entrez un mot : ").strip()


letter_indices = {}

#parrcourir chaque lettre avec son index
for index, letter in enumerate(word):
   
    if letter in letter_indices:
        letter_indices[letter].append(index)  
    else:
        letter_indices[letter] = [index]  

#afficher le dictionnaire final
print("Résultat :", letter_indices)
