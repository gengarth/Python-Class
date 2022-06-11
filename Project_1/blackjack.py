## Main blackjack program
## Charles Denney

import cards
import db

def checkBlackjack(value):
    """Takes card value as argument checks if 
    the identified value is blacjack"""
    if value == 21:
        return True
    else:
        return False

def checkBust(value):
    """Takes card value as argument checks
    if the identified value has busted"""
    if value > 21:
        return True
    else:
        return False

def printValues(playerValue, dealerValue):
    """Takes both card values as arguments and displays them"""
    print("YOUR POINTS:\t" + str(playerValue))
    print("DEALER POINTS:\t" + str(dealerValue))

def main():
    print("BLACKJACK!")
    print("Player starts with 100 chips")
    print("Blackjack payout is 3:2")
    print("Dealer must play to 17")
    print("Aces are a hard 11\n")
    db.setMoney(100) # Sets inital chips to 100

    ## Main play loop
    playAgain = "y"
    while playAgain.lower() == "y":
        db.checkMoney()
        db.printMoney()
        money = db.getMoney()
        bet = db.setBet()
        print()
        winState = True # Used to check various winstates

        ## Builds and shuffles the deck
        deck = cards.buildDeck()
        cards.shuffleDeck(deck)

        ## Deals initial hands and gets game values
        dealerValue, playerValue, dealerHand, playerHand, cardCount = cards.dealHand(deck)

        print("DEALER'S SHOW CARD:\n" + str(dealerHand[0] + "\n"))
        print("YOUR HAND:")
        cards.printHand(playerHand)
        print()

        hasBlackjack = checkBlackjack(playerValue)
        ## Loop for the player's turn
        if hasBlackjack == False:
            while True:
                if checkBust(playerValue) == False:
                    hit = input("Hit or stand? (hit/stand):\t")
                    if hit.lower() == "hit":
                        playerValue, playerHand, cardCount = cards.dealCard(deck, playerValue, playerHand, cardCount)
                        print("YOUR HAND:")
                        cards.printHand(playerHand)
                        print()
                    elif hit.lower() == "stand":
                        print()
                        break
                    else:
                        print("You must either hit or stand. Please try again!\n")
                else:
                    winState = False
                    break
              
        ## Loop for the dealer's turn
        if winState == True and hasBlackjack == False:
            print("DEALER HAND:\n")
            cards.printHand(dealerHand)
            print()
            while dealerValue < 17:
                dealerValue, dealerHand, cardCount = cards.dealCard(deck, dealerValue, dealerHand, cardCount)
                print("DEALER HAND:\n")
                cards.printHand(dealerHand)
                print()
        
        ## Various win conditions
        if winState == True and hasBlackjack == True:
            print("You hit blackjack! Congratulations!")
            money = round((bet * 1.5), 2) + money
            db.setMoney(money)
        elif winState == False:
            print("Sorry, you busted!")
            money = money - bet
            db.setMoney(money)
        elif winState == True:
            if dealerValue > 21:
                printValues(playerValue, dealerValue)
                print()
                print("Dealer busts you win!")
                money = bet + money
                db.setMoney(money)
            elif playerValue > dealerValue:
                printValues(playerValue, dealerValue)
                print("You win!")
                money = bet + money
                db.setMoney(money)
            elif playerValue == dealerValue:
                printValues(playerValue, dealerValue)
                print("It's a draw!")
            else:
                printValues(playerValue,dealerValue)
                print("Sorry, you lost!")
                money = money - bet
                db.setMoney(money)

        print()
        db.printMoney()
        
        playAgain = input("Play again? (y/n) :\t")
        while playAgain.lower() != "y" and playAgain.lower() != "n":
            playAgain = input("You must enter either 'y' to continue " +
            "or 'n' to quit. Try again! (y/n):\t")
        print()
    print("Thanks for playing! See you next time!")


if __name__ == "__main__":
    main()