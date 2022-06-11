import objects
import db
import locale
from datetime import datetime

# Chacks if player got blackjack
def checkBlackjack(value,count):
    if value == 21 and count == 2:
        return True
    else:
        return False

# Checks if there's a bust 
def checkBust(value):
    if value > 21:
        return True
    else:
        return False

# Prints the point total of the dealer and player
def printValues(playerValue, dealerValue):
    print("YOUR POINTS:\t" + str(playerValue))
    print("DEALER POINTS:\t" + str(dealerValue))

def main():

    # Sets the locale for all settings
    osCheck = locale.setlocale(locale.LC_ALL,'')
    if osCheck =="C":
        locale.setlocale(locale.LC_ALL, "en_US")
    
    startTime = datetime.now()
    #Prints header
    print("BLACKJACK!")
    print("Player starts with " + locale.currency(100))
    print("Blackjack payout is 3:2")
    print("Start time: ", startTime.strftime("%I:%M:%S %p\n\n"))
    db.setMoney(100)

    # Main game loop
    playAgain = "y"
    while playAgain.lower() == "y":
        db.checkMoney()
        db.printMoney()
        money = db.getMoney()
        bet = db.setBet()
        print("\n")
        winState = True

        deck = objects.Deck()
        deck.shuffle()
        # Deals initial hands and calculates values
        playerHand = objects.Hand()
        dealerHand = objects.Hand()
        for i in range(2):
           playerHand.addCard(deck.dealCard())
           dealerHand.addCard(deck.dealCard())

        #Prints initial hands
        print("DEALER'S SHOW CARD:")
        objects.dealerShowcard(dealerHand)
        print()

        print("YOUR HAND:")
        objects.printHand(playerHand)
        print()

        # The player's turn
        if checkBlackjack(playerHand.points(), playerHand.count()) == False:
            while True:
                if checkBust(playerHand.points()) == False:
                    hit = input("Hit or stand? (hit/stand):\t")
                    if hit.lower() == "hit":
                        playerHand.addCard(deck.dealCard())
                        print("YOUR HAND:")
                        objects.printHand(playerHand)
                        print()
                    elif hit.lower() == "stand":
                        print()
                        break
                    else:
                        print("You must either hit or stand. Please try again!\n")
                else:
                    winState = False
                    break
        
        # The dealer's turn
        if winState == True and checkBlackjack(dealerHand.points(), playerHand.count()) == False and checkBlackjack(playerHand.points(), playerHand.count()) :
            print("DEALER HAND:\n")
            objects.printHand(dealerHand)
            print()
            while dealerHand.points() < 17:
                dealerHand.addCard(deck.dealCard())
                print("DEALER HAND:\n")
                objects.printHand(dealerHand)
                print()

        # Logic for a win or loss
        if winState == True and checkBlackjack(playerHand.points(), playerHand.count()) == True:
            print("YOUR HAND:\n")
            objects.printHand(playerHand)
            print("You hit blackjack! Congratulations!")
            money = round((bet * 1.5), 2) + money
            db.setMoney(money)
        elif winState == False:
            print("Sorry, you busted!")
            money = money - bet
            db.setMoney(money)
        elif winState == True:
            if dealerHand.points() > 21:
                print("DEALER'S SHOW CARD:")
                objects.printHand(dealerHand)
                print()
                print("YOUR HAND:")
                objects.printHand(playerHand)
                print()
                print("Dealer busts you win!")
                money = bet + money
                db.setMoney(money)
            elif playerHand.points() > dealerHand.points():
                print("DEALER'S SHOW CARD:")
                objects.printHand(dealerHand)
                print()
                print("YOUR HAND:")
                objects.printHand(playerHand)
                print()
                print("You win!")
                money = bet + money
                db.setMoney(money)
            elif playerHand.points() == dealerHand.points():
                print("DEALER'S SHOW CARD:")
                objects.printHand(dealerHand)
                print()
                print("YOUR HAND:")
                objects.printHand(playerHand)
                print()
                print("It's a draw!")
            else:
                print("DEALER'S SHOW CARD:")
                objects.printHand(dealerHand)
                print()
                print("YOUR HAND:")
                objects.printHand(playerHand)
                print()
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
    stopTime = datetime.now()
    elapsedTime = stopTime - startTime
    print("Stop time: " + stopTime.strftime("%I:%M:%S %p"))
    print("Elapsed time: ", str(elapsedTime).split(".")[0])
    print("Thank you for playing! \nSee you next time!")


if __name__ == "__main__":
    main()