# Incorporate the random library
import random
​
# Outcome statments
win = "You won!"
loss = "You lost try again!"
tied = "You tied the computer"
​
# Print Title
print("Let's Play Rock Paper Scissors!")
​
# Specify the three options
options = ["r", "p", "s"]
​
# Computer Selection
computer_choice = random.choice(options)
​
# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")
​
# Run Conditionals
# Tied
if(computer_choice==user_choice):
    print(f"You played {user_choice} and the computer played {computer_choice}")
    print(tied)
​
# Win R beats S, P beats R, S beats P
elif(user_choice=="r" and computer_choice == "s") or (user_choice=='p'and computer_choice=='r') or (user_choice=='s' and computer_choice=='p'):
    print(f"You played {user_choice} and the computer played {computer_choice}")
    print(win)
​
else:
    print(f"You played {user_choice} and the computer played {computer_choice}")
    print(loss)