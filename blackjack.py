import random

# Standard Blackjack deck (Ace as 11, face cards as 10)
deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]
player_cards=[]
computer_cards=[]

# Draw a card and add it to the hand
def draw_card(cards):
    card=random.choice(deck)
    cards.append(card)

# Sum cards, convert Ace (11) to 1 if over 21
def sum_of_cards(cards):
    total=sum(cards)
    while total>21 and 11 in cards:
        cards[cards.index(11)]=1
        total=sum(cards)
    return total

# Deal initial 2 cards
for card_draw in range(2):
    draw_card(player_cards)
    draw_card(computer_cards)

print("Your cards:",player_cards)
print("Computer's first card:",computer_cards[0])

# Player's turn
while True:
    total_player=sum_of_cards(player_cards)
    total_computer=sum_of_cards(computer_cards)

    if total_player>21:
        print(f"Your cards: {player_cards} Computer cards: {computer_cards}")
        print(f"Your total: {total_player}. You Lose! Computer wins.")
        break

    ans=input("Do you want to draw another card? (yes or no): ").lower()
    if ans=='no':
        print(f"Your final cards: {player_cards}, Total: {total_player}")
        break
    elif ans=='yes':
        draw_card(player_cards)
        print("Your cards:",player_cards)
        print("Computer's first card:",computer_cards[0])
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Computer's turn (only if player didn't bust)
if sum_of_cards(player_cards)<=21:
    while sum_of_cards(computer_cards)<17:
        draw_card(computer_cards)

    total_player=sum_of_cards(player_cards)
    total_computer=sum_of_cards(computer_cards)

    print(f"Your final cards: {player_cards}, Total: {total_player}")
    print(f"Computer's final cards: {computer_cards}, Total: {total_computer}")

    if total_computer>21 or total_player>total_computer:
        print("You win!")
    elif total_player<total_computer:
        print("Computer wins!")
    else:
        print("It's a tie!")
