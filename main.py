print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

question_1 = input("You're at a cross road. Where do you want to go ? Type \"left\" or \"right\" ?\n")

if question_1 == "right":
  print("Oops !! you fall into a hole. Game over")

elif question_1 == "left" :
  question_2 = input("You reach the river bank. What will you do? Type \"swim\" or \"wait\" ?\n")

  if question_2 == "swim":
    print("Oh Nooo !! You attcaked by trout. Game Over.")
  
  elif question_2 == "wait" :
    question_3 = input("Finally you arrived at your destination by boat that ypu've wait. One challenge remains. Choose 1 of these 3 doors. Type \"Red\", \"Blue\", or \"Yellow\" ?\n")

    if question_3 == "Yellow" :
      print("You Win!")
    elif question_3 == "Blue":
      print("Oh No!! You eateb by beasts. Game Over.")
    elif question_3 == "Red":
      print("Oh No! Ypu burn by fire. Game Over.")
    else:
      print("Game Over.")