"""
Digital Ready Summer 2024
Card Game Project

Write your card game here!
"""
from card import Card
from rank import Rank
from suit import Suit

import random 

def main():
    print("WELCOME TO GO FISH!!!")

    # Create a deck.
    deck = Card.new_deck()

    # Creating Player and Computer hand
    playerHand   = []
    computerHand = []

    # Dealing seven cards to the Computer and the Player
    n = 7
    while n != 0:
        # Deal card to player and comp

        # card1 = random.choice(deck)
        # card2 = random.choice(deck)

        card1 = deck.pop()
        card2 = deck.pop()

        playerHand.append(card1)
        computerHand.append(card2)

        # Remove dealt cards from deck 
        # deck.remove(card1)
        # deck.remove(card2)
        
        # Updating loop counter
        n-=1
    
    # print(playerHand)
    # print(deck)

    # Show the player the cards they were given.
    print("You were dealt the following cards: ", playerHand)
    
    # Game is over when there are no more cards in the deck/fishing pool 
    while len(deck) >= 0:

        # Ask for player input (i.e. what card do you want to ask the computer for?)
        choice = input("What rank do you want to ask for? Give me a number between 1 and 13: ")
        choice = int(choice)
        print(choice)

        # Computer either gives the card the player ask (i.e. add card to player deck) for or tells 
        print(computerHand)
        new_player_cards = []
        for card in computerHand:
            if card.rank == choice:
                new_player_cards.append(card)
                computerHand.remove(card)

        print(new_player_cards)

        # Player turn 
        if len(new_player_cards) == 0:
            # Choose random card from the original deck
            # Add chosen card to player hand
            # Remove chosen card from the original deck
            card3 = random.choice(deck)
            playerHand.append(card3)
            deck.remove(card3)
            print("Go Fish! You were given the following card from the deck: " + str(card3))
            print("Player Hand: " + str(playerHand))
        else:
            # Add matching rank cards to player hand
            # Remove matching rank cards from computer hand 
            for card in new_player_cards:
                playerHand.append(card)
            print("The following cards were added to your hand: " + str(new_player_cards))
            print("Player Hand: " + str(playerHand))
            # computerHand.remove(new_player_cards)
        
        # print(computerHand)
        # print(playerHand)

        # Computer Turn 
        # Generate a random rank the computer will ask the player for 
        comp_choice = random.randint(1, 13)
        print("The Computer requested the following rank from the Player: " + str(comp_choice))

        # Determine what cards the player will need to give the computer (or if the comp has to go fish)
        computer_cards = []
        for card in playerHand:
            if card.rank == comp_choice:
                computer_cards.append(card)
                playerHand.remove(card)

        # Computer turn 
        if len(computer_cards) == 0:
            # Choose random card from the original deck
            # Add chosen card to player hand
            # Remove chosen card from the original deck
            card4 = random.choice(deck)
            computerHand.append(card4)
            deck.remove(card4)
            print("Computer had to go fish!")
        else:
            # Add matching rank cards to player hand
            # Remove matching rank cards from computer hand 
            for card in computer_cards:
                computerHand.append(card)
            print("The following cards were added to computer hand " + str(computer_cards))
            # computerHand.remove(new_player_cards)
        
        # print(computerHand)
        # print(playerHand)

        player_hand_ranks = []
        for card in playerHand:
            player_hand_ranks.append(card.rank)
        # print(player_hand_ranks)

        computer_hand_ranks = []
        for card in computer_hand_ranks:
            computer_hand_ranks.append(card.rank)
        # print(computer_hand_ranks)

        player_books = 0
        computer_books = 0
        for i in range(1,13):
            if player_hand_ranks.count(i) == 4:
                player_books += 1
            elif computer_hand_ranks.count(i) == 4:
                computer_books += 1 
        # print(computer_books)
        # print(player_books)
        

    # Computer takes its turn.
        # Display the results of the Computers turn (i.e. either takes a card from the player or goes fish)
    # This process contines until there are no more cards in the original deck.
    # When the game is over, we need to count the number of books the computer and player have each.
    # Whoever has the most books wins the game. 
        # Display game results at the end of the game (i.e. number of books each and who won)


if __name__ == "__main__":
    main()