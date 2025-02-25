#day 2 
#exercice xp 
#exercice 2 

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


total_cost = 0  # Variable pour stocker le coût total
costs = {}  # Dictionnaire pour stocker le coût individuel

for name, age in family.items():
    
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15

 #ajouter au coût total
    total_cost += cost
    #stocker le coût individuel
    costs[name] = cost


print("Coût par membre de la famille :")
for name, cost in costs.items():
    print(f"{name}: ${cost}")

print(f"Coût total pour la famille : ${total_cost}")


#exercice 4 

def describe_city(city, country="France"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")  
describe_city("Paris")  
describe_city("Tokyo", "Japan")  


#exercice 4 
#iste des questions et réponses
data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]
#fonction pour poser les questions et vérifier les réponses
def star_wars_quiz():
    correct_count = 0
    incorrect_count = 0
    incorrect_answers = []  

    print("Welcome to the Star Wars Quiz!\n")


    for item in data:
        user_answer = input(f"{item['question']} (Appuie sur Entrée pour ignorer) ").strip() or "default"


        if user_answer.lower() == item['answer'].lower():
            print("Correct!\n")
            correct_count += 1
        else:
            print(f"Incorrect! The correct answer is: {item['answer']}\n")
            incorrect_count += 1
            # aouter à la liste des réponses incorrectes
            incorrect_answers.append({
                "question": item['question'],
                "your_answer": user_answer,
                "correct_answer": item['answer']
            })
    
    #resultats
    display_results(correct_count, incorrect_count, incorrect_answers)
    #fonction pour afficher les résultats
def display_results(correct_count, incorrect_count, incorrect_answers):
    print("Quiz Results")
    print(f"Correct answers: {correct_count}")
    print(f"Incorrect answers: {incorrect_count}\n")

    if incorrect_answers:
        print("Here are the questions you got wrong:\n")
        for error in incorrect_answers:
            print(f"Question: {error['question']}")
            print(f"Your answer: {error['your_answer']}")
            print(f"Correct answer: {error['correct_answer']}\n")
    
    
    if incorrect_count > 3:
        print("You got more than 3 incorrect answers. Please try again!")
        replay = input("Do you want to replay? (yes/no) ").strip().lower()
        if replay == "yes":
            print("\nRestarting the quiz...\n")
            star_wars_quiz()
        else:
            print("Thanks for playing!")

star_wars_quiz()


#exercice 5 
import random

def compare_numbers(user_number):
    if 1 <= user_number <= 100:
        random_number = random.randint(1, 100)
        if user_number == random_number:
            print(f" Succès ! Vous avez deviné le bon nombre : {random_number}")
        else:
            print(f" Échec ! Votre nombre : {user_number}, Nombre généré : {random_number}")
    else:
        print("Veuillez entrer un nombre entre 1 et 100.")

user_input = int(input("Entrez un nombre entre 1 et 100 : "))
compare_numbers(user_input)



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
