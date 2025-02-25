#day 3 
#exercice 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Milo", 2)
cat2 = Cat("Luna", 5)
cat3 = Cat("Simba", 7)

def find_oldest_cat(cats):
    return max(cats, key=lambda cat: cat.age)

oldest_cat = find_oldest_cat([cat1, cat2, cat3])
print(f"Le chat le plus âgé est {oldest_cat.name}, et a {oldest_cat.age} ans.")


#exercice 2 
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} fait ouaf !")

    def jump(self):
        print(f"{self.name} saute {self.height * 2} cm de haut !")
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

#chien de David
print(f"Nom du chien de David : {davids_dog.name}")
print(f"Taille du chien de David : {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

#chien de Sarah
print(f"\nNom du chien de Sarah : {sarahs_dog.name}")
print(f"Taille du chien de Sarah : {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"\nLe plus grand chien est {davids_dog.name}.")
else:
    print(f"\nLe plus grand chien est {sarahs_dog.name}.")


#exercice 3 
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

#création d'un objet Song avec les paroles
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

#affichage des paroles
stairway.sing_me_a_song()



#DAILY CHALLENGE 
class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, count=1):
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        result = f"{self.name}'s farm\n\n"
        
        for animal, count in self.animals.items():
            result += f"{animal} : {count}\n"

        result += "\n    E-I-E-I-0!\n"
        return result

#Création de la ferme
macdonald = Farm("McDonald")

#AjoutER des animaux
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

#Aficher des informations de la ferme
print(macdonald.get_info())