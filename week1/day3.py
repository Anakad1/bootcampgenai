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