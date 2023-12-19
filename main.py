import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letter_amount = int(input("How many letters would you like in your password? "))
symbol_amount = int(input("How many symbols would you like? "))
number_amount = int(input("How many numbers would you like? "))

password = ""

for  char in range(1, letter_amount + 1):
  password += random.choice(letters)
  #It goes through the loops the amount of times specified giving a random letter each iteration

for x in range(1, symbol_amount + 1):
  password += random.choice(symbols)
  #you can use any variable because it stands for one item of the list in the range
  #Remember for fruit in fruits. It was one fruit or one iteration in teh list of fruits

for char in range(1, number_amount + 1):
  password += random.choice(numbers)

print(password)
#It is important for this print statement to be out of the loop entirely
