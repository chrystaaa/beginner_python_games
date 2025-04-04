import random

# ASCII representations 
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Score counters
player_score=0
computer_score=0

print("Welcome to Rock, Paper, Scissors!")
print("Type rock, paper, or scissors to make your move.\n")

# Game loop
while True:
    # Get player's input
    player_choice=input("Your move: ").strip().lower()

    # Validate input
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please try again.")
        continue

    # Computer randomly picks a move
    computer_choice=random.choice(["rock", "paper", "scissors"])

    # Show player's choice
    print("\nYou chose:")
    if player_choice=="rock":
        print(rock)
    elif player_choice=="paper":
        print(paper)
    else:
        print(scissors)

    # Show computer's choice
    print("Computer chose:")
    if computer_choice=="rock":
        print(rock)
    elif computer_choice=="paper":
        print(paper)
    else:
        print(scissors)

    # Determine result
    if player_choice==computer_choice:
        print("It's a tie!")
    elif (player_choice=="rock" and computer_choice=="scissors") or \
         (player_choice=="paper" and computer_choice=="rock") or \
         (player_choice=="scissors" and computer_choice=="paper"):
        print("You win this round!")
        player_score+=1
    else:
        print("Computer wins this round.")
        computer_score+=1

    # Show current score
    print(f"\nScore: You {player_score} | Computer {computer_score}\n")

    # Ask to continue or quit
    again=input("Play again? (y/n): ").strip().lower()
    if again!='y':
        print("\nFinal Score:")
        print(f"You: {player_score} | Computer: {computer_score}")
        print("Thanks for playing!")
        break
