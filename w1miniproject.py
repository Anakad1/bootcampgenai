import random

class Game:
    def __init__(self):
        self.choices = ["pierre", "papier", "ciseaux"]
    
    def get_user_item(self):
        while True:
            user_choice = input("Choisissez pierre, papier ou ciseaux: ").lower()
            if user_choice in self.choices:
                return user_choice
            print("Choix invalide. Essayez encore.")
    
    def get_computer_item(self):
        return random.choice(self.choices)
    
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "match nul"
        elif (user_item == "pierre" and computer_item == "ciseaux") or \
             (user_item == "ciseaux" and computer_item == "papier") or \
             (user_item == "papier" and computer_item == "pierre"):
            return "victoire"
        else:
            return "défaite"
    
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"Vous avez sélectionné {user_item}. L'ordinateur a sélectionné {computer_item}. Résultat: {result}.")
        return result

def get_user_menu_choice():
    print("\nMenu:")
    print("1: Jouer une nouvelle partie")
    print("2: Afficher les scores")
    print("x: Quitter")
    
    choice = input("Votre choix: ")
    while choice not in ["1", "2", "x"]:
        print("Choix invalide. Veuillez réessayer.")
        choice = input("Votre choix: ")
    return choice

def print_results(results):
    print("\nRésumé des parties jouées:")
    print(f"Victoires: {results.get('victoire', 0)}")
    print(f"Défaites: {results.get('défaite', 0)}")
    print(f"Matchs nuls: {results.get('match nul', 0)}")
    print("Merci d'avoir joué !")

def main():
    results = {"victoire": 0, "défaite": 0, "match nul": 0}
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == "1":
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == "2":
            print_results(results)
        elif choice == "x":
            print_results(results)
            break

if __name__ == "__main__":
    main()
