#all the import
import random
import sys

#game_settings
nbTurn = 3

#####################################################Present the game################################################################
print("\nBienvenue dans mon petit jeux")
print("La règle est simple tu vas participerer à 6 niveau et ton but est GAGNER!")

#set user_name
user = input('Quel est ton nom, futur champion ?\n: ')
print(f"Très bien {user}, je te souhaite Bonne chance !")

#####################################################first_game######################################################################
print("\n1er Jeux\n")
print(f"Dans ce 1er jeux tu devras choisir 3 fois entre ces 10 verre d'eau,\nmais ATTENTION {user} un de ces verres contient un poison MORTEL,\net un de plus seras ajouter pour chaque tours")

#launch loop for first_game
for nblaunch in range(3):
   alea = random.randint(1,10)
   user_choice = int(input("Choisis l'un de ces 10 Verres et bonne chance\n: "))
   nbTurn -= 1
   
   if alea == user_choice:
      print('Ah non tu es mort\nGAME is OVER')
      print(f"dev = {alea}")
      sys.exit()

   elif user_choice < 1 or user_choice > 10:
      print(f'\nERROR: {user_choice} is not available in this script\n')
      user_choice = int(input(f'Choisis de nouveau un de ces 10 Verres et bonne chance {user}.\n: '))
      print(f"dev = {alea}")

   else:
      print(f"Bravo plus que {nbTurn} choix")
      print(f"dev = {alea}")

print(f"Bravo {user}, tu as finis le 1er Jeux")

#####################################################second_game#####################################################################

print("\n2eme Jeux\n")
print("2games_rules")
