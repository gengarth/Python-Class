# Functions that run the cards for the blackjack program
import random

def buildDeck():
    deck = {"2 of Hearts": 2, "2 of Clubs": 2, "2 of Spades": 2, "2 of Hearts" : 2,
            "3 of Hearts": 3, "3 of Clubs": 3, "3 of Spades": 3, "3 of Hearts": 3,
            "4 of Hearts": 4, "4 of Clubs": 4, "4 of Spades": 4, "4 of Hearts": 4,
            "5 of Hearts": 5, "5 of Clubs": 5, "5 of Spades": 5, "5 of Hearts": 5,
            "6 of Hearts": 6, "6 of Clubs": 6, "6 of Spades": 6, "6 of Hearts": 6,
            "7 of Hearts": 7, "7 of Clubs": 7, "7 of Spades": 7, "7 of Hearts": 7,
            "8 of Hearts": 8, "8 of Clubs": 8, "8 of Spades": 8, "8 of Hearts": 8,
            "9 of Hearts": 9, "9 of Clubs": 9, "9 of Spades": 9, "9 of Hearts": 9,
            "10 of Hearts": 10, "10 of Clubs": 10, "10 of Spades": 10, "10 of Hearts": 10,
            "Jack of Hearts": 10, "Jack of Clubs": 10, "Jack of Spades": 10, "Jack of Hearts": 10,
            "Queen of Hearts" : 10, "Queen of Clubs": 10, "Queen of Spades": 10, "Queen of Hearts": 10,
            "King of Hearts": 10, "King of Clubs": 10, "King of Spades": 10, "King of Hearts": 10,
            "Ace of Hearts": 11, "Ace of Clubs": 11, "Ace of Spades": 11, "Ace of Hearts": 11}
    
    return deck

def shuffleDeck(deck):
    random.shuffle(deck)

    return deck

def dealHand(deck):
    dealerHand = [random.choice(list(deck.keys())), random.choice(list(deck.keys()))]
    while dealerHand[0] == dealerHand[1]:
        dealerHand = [random.choice(list(deck.keys())), random.choice(list(deck.keys()))]
    dealerValue = deck.pop(dealerHand[0]) + deck.pop(dealerHand[1])
    playerHand = [random.choice(list(deck.keys())), random.choice(list(deck.keys()))]
    while playerHand[0] == playerHand[1]:
        [random.choice(list(deck.keys())), random.choice(list(deck,keys))]
    playerValue = deck.pop(playerHand[0]) + deck.pop(playerHand[1])
    
    # while cardCount < 4:
    #     dealerHand.append(deck[cardCount][0])
    #     dealerValue += deck[cardCount][1]
    #     cardCount += 1
    #     playerHand.append(deck[cardCount][0])
    #     playerValue += deck[cardCount][1]
    #     cardCount += 1
    
    return dealerValue, playerValue, dealerHand, playerHand
    # print("DEALER'S SHOW CARD:\n" + str(dealerHand[0] + "\n"))
    # print("YOUR HAND:")
    # printHand(playerHand)

    # blackjackChecker(playerValue)
    
    #print(dealerValue)

def printHand(hand):
    for card in hand:
        print(card)

def dealCard(deck, value, hand):
    newCard = random.choice(list(deck.keys()))
    hand.append(newCard)
    value += deck.pop(hand[len(hand) - 1])
    return value, hand

def main():
    # deck = buildDeck()
    # print(deck[1])

    deck = buildDeck()
    print(shuffleDeck(deck))

    # print(deck[0][1])

    dealHand(deck)

if __name__ == "__main__":
    main()
