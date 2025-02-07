#exercise1 variables
name = "Alice"
age = 30 
ville = "New York" 
message_f_string = f"hello {name}!, You are {age} years old and live in {ville}."
print(message_f_string)
message_format = "hello {}!, Your are {} years old and live in {}.".format(name, age, ville)
print(message_format)

#exercise2
age = input("what is your age?")
age = int(age)
years_until_100 = 100 - age 
print(f"You will turn 100 in {years_until_100} years")


#exercise1 conditionals
name = input("What is your name?")
length_name = len(name)
if length_name < 5: 
    print('you have a short name : {name}')

#exercise2 
number = int(input("Choose a number between 1 and 100"))
if number % 3 == 0 and number % 5 == 0: 
    print("FizzBuzz")
elif number % 3 == 0: 
    print("Fizz")
elif number % 5 == 0: 
    print("Buzz")
else: 
    print(f"The num {number}, is neither a multiple of 3 nor of 5.")

#exercise
miles = float(input("Enter a number of miles to convert to kilometers."))
kilometers = miles * 1.60934
print(f"{miles} miles is equal to {kilometers} kilometers.")


name = "john doe"
if len(name) > 20: 
    print(f"Name '{name}' is more than 20 chars longs")
elif len(name) > 15: 
     print(f"Name '{name}' is more than 15 chars longs")
elif len(name) > 10: 
     print(f"Name '{name}' is more than 10 chars longs")
elif 8 <= len(name) <= 10: 
     print(f"Name '{name}' is 8, 9 or 10 chars longs")
else: 
     print(f"Name '{name}' is a short name")
     length_description = 'short'


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")


guests = int(input("Enter the number of people attending the wedding: "))
if guests <= 50:
    price = 4000
elif guests <= 100:
    price = 10000
elif guests <= 200:
    price = 15000
else:
    price = 20000
print(f"The cost for {guests} guests is ${price}.")