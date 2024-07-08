print('''
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
                                                               
           88           88                                 88  
           ""           88                                 88  
                        88                                 88  
 ,adPPYba, 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
a8P_____88 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
8PP""""""" 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
"8b,   ,aa 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
 `"Ybbd8"' 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇
direction = str(input("Where to go? left or right?\n"))
direction1 = direction.upper()
if direction1 == "RIGHT":
          print("Fall into a hole game over")
          
elif direction1 == "LEFT":
          next = str(input("swim or wait?\n"))
          next1 = next.upper()
          if next1 == "SWIM":
                    print("attacked by trout game over")
          elif next1 == "WAIT":
                    door = str(input("which door red blue or yellow\n"))
                    door1 = door.upper()
                    if door1 == "RED":
                              print("burned and over game")
                    elif door1 == "BLUE":
                              print("eaten by beast and over")
                    elif door1 == "YELLOW":
                              print("You win!")
                    else:
                              print("game over")

else:
          print("bad keywords brother!")