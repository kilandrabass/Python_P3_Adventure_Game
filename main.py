import time
import random
import sys

delay = 1.0  # For pauses for dramatic effect.

def introduction(): #intro backstory of the mansion
  print("Over 100 years ago, a wealthy family lived in a mansion in the middle of the woods.", end="")
  time.sleep(delay)
  print(" Legend has it that, one day the family went missing, and now their ghosts occupy the space. No one has determined what happened to the family, but there's a theory that they went into hiding.")

def generateRandomItems(num_items):
  items = ['key', 'potion', 'map', 'compass', 'torch', 'riddle scroll'] #generate random items for user to find
  random_items = [random.choice(items) for _ in range(num_items)]
  return random_items

#Explore Mansion and give the user choices
def exploreMansion(username, found_items): 
  print("As you step into a dimly lit hallway, you see a large metal door, while you also spy a creaking staircase to your right, leading up to the attic. To the left of the door is an entrance that leads to the dark, eerie basement.")
  time.sleep(delay)
  print()
  while True:
    choice1 = input("What do you want to inspect?[basement/staircase/secret door] ").strip()  #Choice 1
    print()
    # Decision structure . Evaluates choice for the three options presented.
    if choice1 == "basement":  # First option
      exploreBasement(username, found_items)
    elif choice1 == "staircase":
      exploreStaircase(username, found_items)
      break
    elif choice1 == "secret door":
      exploreSecretDoor(username, found_items)
      break
    else:
      print("Invalid input. Please try again.")

def exploreBasement(username, found_items): #Explore the basement
  thief = True
  print("You walk downstairs to the basement and the lights start flickering.")
  time.sleep(delay)
  if thief:  #Use boolean
    print("An unknown voice says: \n\"Hey, you're trespassing!\"")  
    print("A boobie trap goes off and you're suddenly trapped in the basement.")
    print("You lose {}, you're considered a thief and have been caught!".format(username))
    continue_exploring(username, found_items)  #Continuation loop
    sys.exit()
  
def exploreStaircase(username, found_items): #Explore the staircase
  print("You walk up the staircase with your heart pounding from fear.")
  print()
  time.sleep(delay)  # Another use of the dramatic pause feature
  print("Wind from an open window blows your lantern out and you end up lost in the mansion with no way out.")
  print()
  print("You lose, {}, you're considered a thief and have been caught!".format(username))
  continue_exploring(username, found_items)  #Continuation loop
  sys.exit()

def exploreSecretDoor(username, found_items): #Explore secrect door
  thief = False
  print("You open the secret door and find yourself in an old, dusty library.")
  time.sleep(delay)
  print("You grab a shiny book and it triggers a hidden passage to emerge leading to a small chamber.")
  time.sleep(delay)
  print("You walk in the chamber and see a tresure chest...")
  time.sleep(delay)
  puzzle_difficulty = random.randint(1, 10) #Simulate puzzle difficulty with a random number
  if puzzle_difficulty <= 5: #Higher probability of success for lower difficulty
      print("You manage to solve the puzzle on the treasure chest easily.")
      print("Congratulations, {}, you've found the hidden treasure!".format(username))
      print("You win!")
      found_items.append("hidden treasure")  #Add the found item to the list
  else:
      print("The puzzle on the treasure chest seems too complex to solve.")
      print("You couldn't unlock the treasure chest.")
      print("Better luck next time, {}!".format(username))

def exploreItems(found_items): #Print items found during the game
  print("You found the following items during your exploration:")
  for item in found_items:
      print("-", item)
      
def main():
  introduction()
  print()
  username = input("You've entered the Haunted Mansion. State your name: ")  # User’s name
  print("Welcome,", username, "to the Haunted Mansion, an estate that has been abandoned for 100 years! You must be brave to dare to enter.")
  print()
  # Player encounters a room where they may find random items
  print("You enter a mysterious room...")
  time.sleep(delay)
  print("You found some items: ")
  for item in generateRandomItems(3):
      print("- " + item)
  
  purpose = input("What has brought you here, " + username + "? ")  # User’s purpose

  #Decision structure 1. Evaluates purpose variable for two specific options. Also has a default response
  if purpose.lower() == "fun":
    print("Maybe you will solve the mystery!")
  elif purpose == "hidden treasure":
    print("I hear there is a treasure hidden somewhere in the mansion.")
  else:  #For any response other than “fun” or “hidden treasure”
    print("Well, I hope that you find what you're looking for.")
    print("It is time for you to enter the mansion!\n\n")

  found_items = []
  exploreMansion(username, found_items)
  exploreItems(found_items) #Prints items found

#Allow users to conitnue exploring the mansion or exit the game
def continue_exploring(username, found_items):
  while True:
    choice = input("Do you want to play again? [yes/no] ").lower()
    if choice.lower() not in ['yes', 'no']:
      print("Invalid input. Please enter 'yes' or 'no'.")
    elif choice.lower() == "yes":
        found_items.clear()  #Clear the found items list
        exploreMansion(username, found_items)  #Restart the game
        break
    else:
        print("Thanks for playing, {}. Goodbye!".format(username))
        sys.exit()

main()


