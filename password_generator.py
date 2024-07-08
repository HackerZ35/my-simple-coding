#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#ONLY FOR LETTERS!
letter1 = []
for x in range(1,(nr_letters+1)):
  y = random.choices(letters)
  letter1.append(y)

str(letter1)


symbols1 = []
#ONLY for symbols
for z in range(1,nr_symbols+1):
  i = random.choices(symbols)
  symbols1.append(i)

str(symbols1)


#only for numbers
numbers1 = []
for j in range(1,nr_numbers+1):
  k = random.choices(numbers)
  numbers1.append(k)

str(numbers1)



#addition of the lists
password = letter1 + symbols1 + numbers1

#since its a nested list we need to make it flat
flat_list =[]
for sub_list in password:
  for item in sub_list:
    flat_list.append(item)

shuffle  =  input("want to shuffle or not? Y/N\n")
str_shuffle = shuffle.upper()
if str_shuffle == "Y":
  random.shuffle(flat_list)
  
  my_pass1 = ''.join(flat_list)
  print(my_pass1)
  

elif str_shuffle == "N":
  my_pass2 = "".join(flat_list)
  print(my_pass2)

else:
  print("Invalid")

quit()