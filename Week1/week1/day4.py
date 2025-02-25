#day4 
#exercice 1 
#classe mère cat
class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

#sous classes de cat
class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#nouvelle sous classe siamese
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#classe pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

#création des instances de chats
bengal_cat = Bengal("Leo", 3)
chartreux_cat = Chartreux("Milo", 5)
siamese_cat = Siamese("Luna", 2)

#liste de tous les chats
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

#instance de Sara avec ses chats
sara_pets = Pets(all_cats)

#emmener tous les chats en promenade
sara_pets.walk()


#exercice 2 
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} aboie"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} a gagné le combat contre {other_dog.name} !"
        else:
            return f"{other_dog.name} a gagné le combat contre {self.name} !"

#création de 3 chiens
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 25)
dog3 = Dog("Rocky", 4, 18)

#faire courir les chiens
print(dog1.bark())
print(dog2.run_speed())
print(dog3.fight(dog1))


#exercice 3 
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *other_dogs):
        dog_names = ", ".join([dog.name for dog in other_dogs])
        print(f"{self.name}, {dog_names} jouent ensemble !")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} fait un tonneau.",
                f"{self.name} se tient sur ses pattes arrières.",
                f"{self.name} te serre la main.",
                f"{self.name} fait le mort."
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} n'est pas encore dressé !")

#tester la classe PetDog
pet_dog = PetDog("Rex", 5, 20)
pet_dog.train()
pet_dog.do_a_trick()

pet_dog2 = PetDog("Buddy", 3, 25)
pet_dog.play(pet_dog2)


#exercice 4 
class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Félicitations ! La famille {self.last_name} accueille {kwargs['name']}.")

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                return member["age"] >= 18
        return False

    def family_presentation(self):
        print(f"Famille {self.last_name}:")
        for member in self.members:
            print(f"- {member['name']}, {member['age']} ans, {member['gender']}")

#je cree la famille
family_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]
my_family = Family("Dupont", family_members)

#je teste les méthodes
my_family.family_presentation()
print(my_family.is_18("Michael"))  # True
my_family.born(name="Emma", age=0, gender="Female", is_child=True)
my_family.family_presentation()


#DAILY CHALLENGE
class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items else []  #liste des éléments
        self.pageSize = int(pageSize)  #NB d'element  par page
        self.totalPages = max(1, (len(self.items) + self.pageSize - 1) // self.pageSize)  # Nombre total de pages
        self.currentPage = 1 

        