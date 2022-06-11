## Functions that access the money for blackjack program
## Full module must be imported for most functions to work

import sys

def getMoney():
    """Reads money.txt and returns value found there as float"""
    try:
        with open("money.txt") as file:
            money = file.read()
            return round(float(money), 2)
    except FileNotFoundError:
        print("Could not find money.txt")
    except OSError:
        print("File found - error reading file")
    except Exception:
        print("Unknown error occured")

def setMoney(money):
    """Takes numeric data as argument and writes it
    it money.txt"""
    try:
        with open("money.txt", "w") as file:
            moneyRounder = round(money, 2)
            file.write(str(moneyRounder))
    except FileNotFoundError:
        print("Could not find money.txt")
    except OSError:
        print("File found - error wrtiting file")
    except Exception:
        print("Unknown error occured")

def printMoney():
    """Reads money.txt and prints value found there"""
    try:
        with open("money.txt") as file:
            money = file.read()
            print("Money:\t" + str(money))   
    except FileNotFoundError:
        print("Could not find money.txt")
    except OSError:
        print("File found - error reading file")
    except Exception:
        print("Unknown error occured")

def setBet():
    """Get's player's bet amount, checks that it is within parameters,
    returns numberic value"""
    while True:
        try:
            bet = float(input("Bet amount:\t"))
            if bet < 5 or bet > 1000:
                print("Minimum bet is 5. Maximum bet is 1,000. " + 
                "Please try again!")
            elif bet > getMoney():
                print("Bet can't be bigger than current money " +
                "which is " + str(getMoney()))
            else:
                return bet
        except ValueError:
            print("Must enter a number")


def checkMoney():
    """Uses getMoney() to check if player has enough money to 
    cover the minimum bet, if not it uses setMoney() to add 100
    more chips"""
    if getMoney() < 5:
        while True:
            addChips = input("Can't cover minimum bet, enter 'y' " +
            "to add 100 more chips or 'n' to quit! (y/n)\t")
            if addChips.lower() == "y":
                setMoney(getMoney() + 100)
                break
            elif addChips.lower() == "n":
                print("Thanks for playing! !ee you next time!")
                sys.exit()
            else:
                print("Must enter either 'y' or 'n'. Please try again! (y/n)\t")


def main():
    """Various test code"""
    # Function tests
    # money = getMoney()
    # print(money)

    # setMoney(50)
    # printMoney()

    # setMoney()
    # printMoney()

    # money = getMoney()
    # print(money)

    bet = setBet()
    print(bet)

    #checkMoney()


if __name__ == "__main__":
    main()