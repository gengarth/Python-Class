# Functions that run the cards for the blackjack program
import random

class Session:
    def __init__(self, sessionID = 0, startTime = None, startMoney = 0, stopTime = None, stopMoney = 0):
        self.sessionID = sessionID
        self.startTime = startTime
        self.startMoney = startMoney
        self.stopTime = stopTime
        self.stopMoney = stopMoney

class Card:
    #Attributes for Card
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suit = ["H|", "C|", "S|", "D|"]
    points = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    
    def __str__(self):
        return self.rank, self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for rank in Card.rank:
            for suit in Card.suit:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def count(self):
        count = 0
        for card in self.deck:
            count += 1
        return count

    def dealCard(self):
       return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def addCard(self, newCard):
        self.cards.append(newCard)

    def points(self):
        points = 0
        for card in self.cards:
            points += card.points[card.rank]
        return points

    def showCardPoints(self):
        points = 0
        for card in self.cards:
            points += card.points[card.rank]
            return points

    def count(self):
        count = 0
        for card in self.cards:
            count += 1
        return count
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index == len(self.cards):
            raise StopIteration()
        card = self.cards[self.index]
        self.index += 1
        return card

    def __str__(self):
        return self.rank, self.suit

def dealerShowcard(cards):
    for card in cards:
        showCard = (card.rank, card.suit)
        break
    return showCard



# def buildDeck():
#     deck = {"2 of Hearts": 2, "2 of Clubs": 2, "2 of Spades": 2, "2 of Hearts" : 2,
#             "3 of Hearts": 3, "3 of Clubs": 3, "3 of Spades": 3, "3 of Hearts": 3,
#             "4 of Hearts": 4, "4 of Clubs": 4, "4 of Spades": 4, "4 of Hearts": 4,
#             "5 of Hearts": 5, "5 of Clubs": 5, "5 of Spades": 5, "5 of Hearts": 5,
#             "6 of Hearts": 6, "6 of Clubs": 6, "6 of Spades": 6, "6 of Hearts": 6,
#             "7 of Hearts": 7, "7 of Clubs": 7, "7 of Spades": 7, "7 of Hearts": 7,
#             "8 of Hearts": 8, "8 of Clubs": 8, "8 of Spades": 8, "8 of Hearts": 8,
#             "9 of Hearts": 9, "9 of Clubs": 9, "9 of Spades": 9, "9 of Hearts": 9,
#             "10 of Hearts": 10, "10 of Clubs": 10, "10 of Spades": 10, "10 of Hearts": 10,
#             "Jack of Hearts": 10, "Jack of Clubs": 10, "Jack of Spades": 10, "Jack of Hearts": 10,
#             "Queen of Hearts" : 10, "Queen of Clubs": 10, "Queen of Spades": 10, "Queen of Hearts": 10,
#             "King of Hearts": 10, "King of Clubs": 10, "King of Spades": 10, "King of Hearts": 10,
#             "Ace of Hearts": 11, "Ace of Clubs": 11, "Ace of Spades": 11, "Ace of Hearts": 11}
    
#     return deck

# def shuffleDeck(deck):
#     random.shuffle(deck)

#     return deck

# def dealHand(deck):
#     dealerHand = [random.choice(list(deck.keys())), random.choice(list(deck.keys()))]
#     while dealerHand[0] == dealerHand[1]:
#         dealerHand = [random.choice(list(deck.keys())), random.choice(list(deck.keys()))]
#     dealerValue = deck.pop(dealerHand[0]) + deck.pop(dealerHand[1])
#     playerHand = [random.choice(list(deck.keys())), random.choice(list(deck.keys()))]
#     while playerHand[0] == playerHand[1]:
#         [random.choice(list(deck.keys())), random.choice(list(deck,keys))]
#     playerValue = deck.pop(playerHand[0]) + deck.pop(playerHand[1])
    
#     return dealerValue, playerValue, dealerHand, playerHand

def printHand(cards):
    showCard= []
    for card in cards:
        showCard.append(card.rank)
        showCard.append(card.suit)
    return showCard


# def dealCard(deck, value, hand):
#     newCard = random.choice(list(deck.keys()))
#     hand.append(newCard)
#     value += deck.pop(hand[len(hand) - 1])
#     return value, hand

##>>> 
##==================== RESTART: C:\.........\Project_3\objects.py ====================
##Cards - Tester
##
##DECK
##Deck created.
##Deck shuffled.
##Deck count: 52
##
##HAND
##4 of Clubs
##King of Hearts
##8 of Hearts
##7 of Spades
##
##Hand points: 29
##Hand count: 4
##Deck count: 48
##>>> 


def main():
    print("Cards - Tester")
    print()

    # test Deck class
    print("DECK")
    deck = Deck()
    print("Deck created.")
    print()
    deck.shuffle()    
    print("Deck shuffled.")
    print()
    print("Deck count:", deck.count())
    print()

    # test Hand class
    print("HAND")
    hand = Hand()
    for i in range(4):
        hand.addCard(deck.dealCard())

    for card in hand:
        print(card.rank, card.suit)
    print()

    print("Hand points:", hand.points())
    print("Hand count:", hand.count())
    print("Deck count:", deck.count())

if __name__ == "__main__":
    main()
