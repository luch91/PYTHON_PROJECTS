"""
Black Jack Game. Rules of the game.
Deal both user and computer a starting hand of 2 random card values.

Detect when computer or user has a blackjack. (Ace + 10 value card).

If computer gets blackjack, then the user loses (even if the user also has a blackjack). If the user gets a blackjack, then they win (unless the computer also has a blackjack).

Calculate the user's and computer's scores based on their card values.

If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.

Reveal computer's first card to the user.

Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.

Ask the user if they want to get another card.

Once the user is done and no longer wants to draw any more cards, let the computer play. The computer should keep drawing cards unless their score goes over 16.

Compare user and computer scores and see if it's a win, loss, or draw.

Print out the player's and computer's final hand and their scores at the end of the game.

After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.
Note:
The deck is unlimted in size
There are no jokers
The Jack/Queen/King all count as 10
The Ace can count as 11 or 1
The cards in the list have equal probablility of being drawn
Cards are not removed from the deck as they are drawn.
"""
import random
# the list of cards

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Deal the user and the computer 2 cards each using deal_card()

user_cards = []
computer_cards = []
is_game_over = False


for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

#Create a function called calculate_score() that tales a list
# of cards as input and returns the score
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""

    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
    # and return 0 instead of the actual score. 0 will represent a blackjack in our game.   


    if sum(cards) == 21 and len(cards) == 2 :
        return 0
    
    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Create a function called compare() and pass in the user_score and computer_score. 
# If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses.
#  If the user has a blackjack (0), then the user wins. If the user_score is over 21, 
# then the user loses. If the computer_score is over 21, then the computer loses.
#  If none of the above, then the player with the highest score wins.


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤 "
    
    if user_score == computer_score:
        return "Draw 🙃 "
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score ==  21:
        return "Win with a Blackjack 😎"
    elif user_score > 21 :
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else: 
        return "You lose 😤"

# The score will need to be rechecked with every new card drawn 
# and the checks in Hint 9 need to be repeated until the game ends.

while not is_game_over:
    #    # Call calculate_score(). If the computer or the user has a blackjack (0) 
    # or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card : {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score >21:
        is_game_over = True

    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

    # once the user is done, it's time to let the computer play. 
    # The computer should keep drawing cards as long it has a score less than 17

    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}. final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


#while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    #play_game()




    



    

 

