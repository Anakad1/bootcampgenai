word = "ppoeemm"

word_second =  word[0] #"p"

for index, letter in enumerate(word) :
    print(f"{index} - {letter}") 
    last_letter = word_second[-1]
    if index <= len(word)-2 and word[index+1] != last_letter:
        word_second += word[index+1]

print(word_second)




# colors = ["red", "pink", "green"]

# list(enumerate(colors)) #converti l'object cree par la fonction enumerate en liste
# [
#     (0, 'red'), 
#     (1, 'pink'), 
#     (2, 'green')
# ]

# colors = ["red", "pink", "green"]

# for color in colors :
#     print(color)

# for index, color in enumerate(colors) :
#     print(f"{index} - {color}") 


# 1er boucle
#  index : 0
#  color : "red"

# 2e boucle
#  element = (1, "pink")


# 1er boucle
#  element = (0, "red")

# 2e boucle
#  element = (1, "pink")




# user = ("John", "Smith")
# # print(user)

# variableA, variableB = tuple
# variableA = tuple[0]
# variableB = tuple[1]

# first_name, last_name = user #("John", "Smith")
# print(first_name)
# print(last_name)

# # liste 
# colorA, colorB = ["red", "pink"]
# print(colorA)
# print(colorB)
# print(f"{colorA} - {colorB}")
# print(colorA, colorB)

# # chaine de caractere
# letterA, letterB = "He"
# print(letterA)
# print(letterB)

#destructuration
# city, country = "Paris","France"
# print(city)
# print(country)


# Write a program that asks a string to the user, 
# and display a new string with any duplicate consecutive letters removed.

word = "ppoeemm"

word_second =  word[0] #on commence avec la premiere lettre

# ajout
# on boucle pour parcourir la variable word
for letter in word :
    last_letter = word_second[-1] #"o"
    if letter != last_letter :
        word_second += letter
        # word_second = word_second + letter

print(word_second)


# 1er boucle
#     word_second = "p"
#     letter = "p"
#     last_letter = "p" --> je ne rentre pas dans le if

# 2e boucle
#     word_second = "p"
#     letter = "p"
#     last_letter = "p" --> je ne rentre pas dans le if

# 3e boucle
#     word_second = "p"
#     letter = "o"
#     last_letter = "p" 
#     --> je ne rentre pas dans le if et je rajoute la lettre
#     word_second = "po"



##
#user = {
#    "first_name" : "john",
#   "age" : 30, 
##   "is_married" : False, 
#   "animals" : ["cat", "dog"], 
#}

#Exercice 1 
#create a dictionary

user = {
    "first_name" : 'John',
    "last_name" : 'Doe',
    "favorite_hobby" : 'Python',
    "sports_hobby" : 'gym', 
    "age" : 82,
}
print(user)

#print the total duration of the playlist 
playlist = {
    'title': "Hello World",
    'author': "Planet",
    'songs': [
        {
            'song_title': "Song One",
            'artist': ['Artist 1', 'Artist 2'],
            'duration': 4.31,
        },
        {
            'song_title': "Song Two",
            'artist': ['Artist 1'],
            'duration': 2.53,
        },
        {
            'song_title': "Song Three",
            'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
            'duration': 3.43,
        }
    ]
}

#print the total duration 
total_duration = sum(song['duration']for song in playlist['songs'])
print(f"la total duree de la playlist : {total_duration} minutes ")


#list initiale
words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
uppercase_words = [word for word in words if word.isupper()]
print(uppercase_words)



#function
#objectif : verifier que le nb est sup a 18 
#si sup 18 : majeur 
#personne mineur

def check_age(age_user) :  
    if age_user >= 18 : 
        print("personne majeure")
    else: 
        print("personne mineure")

check_age(22)
check_age(16)
check_age(18)

reponse_user = int(input("what is your age?"))
check_age(reponse_user)

#je cree une fonction qui recupere en entree le num de ma table et la liste des prix des plats et renvoie la somme a payer 
#phrase indication

def pay_restau(num_table, list_price, first_name) :
    total = sum(list_price)
    print(f"la table {num_table} doit payer {total} euros")

pay_restau(1, [34, 76, 29], "john")
pay_restau(2, [37, 79, 69], "john")
pay_restau(3, [44, 96, 39], "john")



#annotation = indication 
#def check_user(name : str, age = int) : 
    #print(f"hello {name} - {age}")

# colors = ["red", "pink", "green"]

# first_color =  colors[0]
# last_color = colors[-1]
# counter = 0
# color = colors[counter+1] #color[1] #pink

# dictionnaires

# user = {
#     key : value,
#     key : value,
#     key : value,
# }

# dictionnaire

# liste
# ["a", "b", "c"]

# # tuple
# (0, "red")

# dictionnaire
# user = {
#     "first_name" : "John", 
#     "age" : 30,
#     "is_married" : False,
#     "animals" : ["cat", "dog"]
# }

# print(user["first_name"])
# print(user)
# print(user.items())

# dict_items([
#     ('first_name', 'John'), 
#     ('age', 30),
#     ('is_married', False), 
#     ('animals', ['cat', 'dog'])
#     ])

# for element in user.items() :
#     print(element)

# for clef, valeur in user.items() :
#     print(f"son {clef} est {valeur}")




users = [
    {
        "first_name" : "John", 
        "age" : 30,
         "is_married" : False,
    },
    {
        "first_name" : "Lea", 
        "age" : 35,
        "is_married" : True,
    }
]

# recuperer l'age de la 2e personne
# age_second_person = users[1]["age"]
# print(age_second_person)


# (0, ["cat", "dog"])


# JEU QUIZ
# 30 questions
#     - Instruction
#     - Option 
#     - Reponse


quiz = [
    {
        "instruction": "Quelle est la capitale de la France",
        "options": ["Paris", "Toulouse", "Bordeaux", "Lyon"],
        "reponse" : "Paris",
    },
    {
        "instruction": "Quelle est la superficie de la France",
        "options": [23.4, 45,9, 100, 300],
        "reponse" : 300,
    }
]

# avec les elements de la liste
for question in quiz :
    question_instruction = question["instruction"]
    question_response = question["reponse"]
    print(f" la question est {question_instruction} - la reponse est {question_response}")

#avec des index
for i in range(len(quiz)) :
    # print(i)
    question = quiz[i]
    question_instruction = question["instruction"]
    question_response = question["reponse"]
    print(f" la question est {question_instruction} - la reponse est {question_response}")

    