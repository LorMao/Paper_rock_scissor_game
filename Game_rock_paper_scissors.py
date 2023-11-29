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
my_choice = input("What do you choose? Type '0' for rock, type '1' for paper, type '2' for scissors\n")

if my_choice == "0":
  print("you picked:" + rock)
elif my_choice == "1":
  print("you picked:" + paper)
else:
  print("you picked:" + scissors)



import random

computer_list = [rock, paper, scissors]
computer_pick = random.choice(computer_list)
print(f"computer choice: {computer_pick}")



if my_choice == "0" and computer_pick == scissors:
  print("You win!")
elif my_choice == "1" and computer_pick == rock:
  print("You win!")
elif my_choice == "2" and computer_pick == paper:
  print("You win!")
elif my_choice == "0" and computer_pick == paper:
  print("You lose!")
elif my_choice == "1" and computer_pick == scissors:
  print("You lose!")
elif my_choice == "2" and computer_pick == rock:
  print("You lose!")
else:
  print("It's a tie!")
