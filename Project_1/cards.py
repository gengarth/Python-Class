## Functions that run the cards for the blackjack program
## Full module must be imported to run most functions

import random

def buildDeck():
    """Builds deck for other functions to use, returns the deck list of lists"""
    deck = [["2 of Hearts", 2], ["2 of Clubs", 2], ["2 of Spades", 2], ["2 of Hearts", 2],
            ["3 of Hearts", 3], ["3 of Clubs", 3], ["3 of Spades", 3], ["3 of Hearts", 3],
            ["4 of Hearts", 4], ["4 of Clubs", 4], ["4 of Spades", 4], ["4 of Hearts", 4],
            ["5 of Hearts", 5], ["5 of Clubs", 5], ["5 of Spades", 5], ["5 of Hearts", 5],
            ["6 of Hearts", 6], ["6 of Clubs", 6], ["6 of Spades", 6], ["6 of Hearts", 6],
            ["7 of Hearts", 7], ["7 of Clubs", 7], ["7 of Spades", 7], ["7 of Hearts", 7],
            ["8 of Hearts", 8], ["8 of Clubs", 8], ["8 of Spades", 8], ["8 of Hearts", 8],
            ["9 of Hearts", 9], ["9 of Clubs", 9], ["9 of Spades", 9], ["9 of Hearts", 9],
            ["10 of Hearts", 10], ["10 of Clubs", 10], ["10 of Spades", 10], ["10 of Hearts", 10],
            ["Jack of Hearts", 10], ["Jack of Clubs", 10], ["Jack of Spades", 10], ["Jack of Hearts", 10],
            ["Queen of Hearts", 10], ["Queen of Clubs", 10], ["Queen of Spades", 10], ["Queen of Hearts", 10],
            ["King of Hearts", 10], ["King of Clubs", 10], ["King of Spades", 10], ["King of Hearts", 10],
            ["Ace of Hearts", 11], ["Ace of Clubs", 11], ["Ace of Spades", 11], ["Ace of Hearts", 11]]
    
    return deck

def shuffleDeck(deck):
    """Takes deck as argument, shuffles the deck, returns 
    shuffled deck"""
    random.shuffle(deck)

    return deck

def dealHand(deck):
    """Takes the shuffled deck list as argument, instantiates game values, 
    deals the intial hand, returns game values"""
    dealerValue = 0
    playerValue = 0
    dealerHand = []
    playerHand = []
    cardCount = 0
    
    while cardCount < 4:
        dealerHand.append(deck[cardCount][0])
        dealerValue += deck[cardCount][1]
        cardCount += 1
        playerHand.append(deck[cardCount][0])
        playerValue += deck[cardCount][1]
        cardCount += 1
    
    return dealerValue, playerValue, dealerHand, playerHand, cardCount


def printHand(hand):
    """Takes hand list as argument, prints the hand"""
    for card in hand:
        print(card)

def dealCard(deck, value, hand, cardCount):
    """ Takes game values as arguments, deals a card to appropriate hand,
    returns game values"""
    hand.append(deck[cardCount][0])
    value += deck[cardCount][1]
    cardCount += 1
    return value, hand, cardCount

def main():
    """ Various test code"""
    # deck = buildDeck()
    # print(deck[1])

    deck = buildDeck()
    print(shuffleDeck(deck))

    # print(deck[0][1])

    dealHand(deck)

if __name__ == "__main__":
    main()
