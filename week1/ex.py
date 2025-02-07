#introduction a Python
#exercise xp 

#exercise 1 : 
#imprimer en ue seule ligne 
print("Hello world\nHello world\nHello world\nHello world")

#exercise 2 : 
calcul = (99^3)*8
print(calcul)

#exercise 3 : 
name = input("what is your name?")
if name == "anaelle":
    print("twins")
else: 
    print("go out")

#exercise 4 : 
hight = int(input("what is your hight in centimeters"))
if hight > 145: 
    print("You are tall enough to ride the rollercoaster!")
else:
    print("Sorry, you need to grow a little more to ride.")


#exercise 5 : 
my_fav_numbers = {8, 11, 14, 17, 26}
#add two numbers 
my_fav_numbers.add(29)
my_fav_numbers.add(32)
#remove the last number 
my_fav_numbers.pop()
#create a set friend favorit number 
friend_fav_numbers = {15, 19, 4}
#our fav num
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("my favorite numbers:", my_fav_numbers)
print("firend's favorite numbers:", friend_fav_numbers)
print("our favorite numbers:", our_fav_numbers)

#exercise 6 : 
original_tuple = (1, 2, 3)
new_elements = (4, 5)
# Create a new tuple by concatenating
new_tuple = original_tuple + new_elements
print(new_tuple)

#exercise 7 : 
# Initial list
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list
basket.remove("Banana")
# Remove "Blueberries" from the list
basket.remove("Blueberries")
# Add "Kiwi" at the end of the list
basket.append("Kiwi")
# Add "Apple" at the beginning of the list
basket.insert(0, "Apple")
# Count how many "Apples" are in the basket
apple_count = basket.count("Apples")
print("Number of Apples in the basket:", apple_count)
# Empty the basket
basket.clear()
# Print the final basket
print("Basket after clearing:", basket)


#exercise 8 : 
#list of sandwich orders
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", 
                   "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", 
                   "Pastrami sandwich"]
#Remove all occurrences of "Pastrami sandwich" using a while loop
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
#create an empty list called finished_sandwiches
finished_sandwiches = []
#Process each sandwich order and add it to finished_sandwiches
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)  # Remove the first sandwich from the list
    finished_sandwiches.append(sandwich)  # Add it to finished_sandwiches
    # Print the message for each sandwich prepared
    print(f"I made your {sandwich}")
#optional: print the final list of finished sandwiches
print("All sandwiches have been made:", finished_sandwiches)


#DAILYCHALLENGE 1
#ask the user for a number and length
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))
#create a list of multiples of the number until the length is reached
multiples = [number * i for i in range(1, length + 1)]
#print the result
print(multiples)


#DAILYCHALLENGE 2 
#ask the user for a string
user_word = input("Enter a word: ")
#create a new string by removing consecutive duplicate letters
result = ""
#loop through the string and add each character to the result only if it's not the same as the last added character
for i in range(len(user_word)):
    if i == 0 or user_word[i] != user_word[i - 1]:
        result += user_word[i]
#Print the result
print("New word:", result)