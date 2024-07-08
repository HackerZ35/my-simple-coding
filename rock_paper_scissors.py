rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
pc_value = 0
rock_list = [rock, paper, scissors]

generate = random.choice(rock_list)
rock_index = len(rock_list)-3
paper_index = len(rock_list)-2
scissor_index = len(rock_list)-1


value = int(input("what do you choose? type 0 for rock, 1 for paper and 2 for scissors\n"))
if generate == rock_list[0]:
    pc_value = 0
elif generate == rock_list[1]:
    pc_value = 1
else:
    pc_value = 2







#ROCK shit
if value == 0 and pc_value == 0:
    print("you choose: ")
    print(rock)
    print("PC choose: ")
    print(rock)
    print("Its a draw")
elif value == 0 and pc_value == 1:
    print("you choose: ")
    print(rock)
    print("PC choose: ")
    print(paper)
    print("you lost")

elif value == 0 and pc_value == 2:
    print("you choose: ")
    print(rock)
    print("PC choose: ")
    print(scissors)
    print("You win!")


#paper shit
if value == 1 and pc_value == 0:
    print("you choose: ")
    print(paper)
    print("PC choose: ")
    print(rock)
    print("you win")
elif value == 1 and pc_value == 1:
    print("you choose: ")
    print(paper)
    print("PC choose: ")
    print(paper)
    print("its a draw")

elif value == 1 and pc_value == 2:
    print("you choose: ")
    print(paper)
    print("PC choose: ")
    print(scissors)
    print("you lost")




#scissor shit
if value == 2 and pc_value == 0:
    print("you choose: ")
    print(scissors)
    print("PC choose: ")
    print(rock)
    print("you lost")
elif value == 2 and pc_value == 1:
    print("you choose: ")
    print(scissors)
    print("PC choose: ")
    print(paper)
    print("you win")

elif value == 2 and pc_value == 2:
    print("you choose: ")
    print(scissors)
    print("PC choose: ")
    print(scissors)
    print("its a draw!")
exit()