# Functions that access the money for blackjack program
import sys
import locale

def getMoney():
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
    try:
        osCheck = locale.setlocale(locale.LC_ALL,'')
        if osCheck =="C":
            locale.setlocale(locale.LC_ALL, "en_US")

        with open("money.txt") as file:
            money = file.read()
            print("Money:\t" + locale.currency(float(money), grouping = True))   
    except FileNotFoundError:
        print("Could not find money.txt")
    except OSError:
        print("File found - error reading file")
    except Exception:
        print("Unknown error occured")

def setBet():
    osCheck = locale.setlocale(locale.LC_ALL,'')
    if osCheck =="C":
        locale.setlocale(locale.LC_ALL, "en_US")

    while True:
        try:
            bet = float(input("Bet amount:\t"))
            if bet < 5 or bet > 1000:
                print("Minimum bet is" + locale.currency(5) + ". Maximum bet is " + 
                locale.currency(1000) + ". " + "Please try again!")
            elif bet > getMoney():
                print("Bet can't be bigger than current money " +
                "which is " + str(getMoney()))
            else:
                return bet
        except ValueError:
            print("Must enter a number")


def checkMoney():
    osCheck = locale.setlocale(locale.LC_ALL,'')
    if osCheck =="C":
        locale.setlocale(locale.LC_ALL, "en_US")
    if getMoney() < 5:
        while True:
            addChips = input("Can't cover minimum bet, enter 'y' " +
            "to add " + locale.currency(100)  + " or 'n' to quit! (y/n)\t")
            if addChips.lower() == "y":
                setMoney(getMoney() + 100)
                break
            elif addChips.lower() == "n":
                print("Thanks for playing, see you next time!")
                sys.exit()
            else:
                print("Must enter either 'y' or 'n'. Please try again! (y/n)\t")


def main():
    # Function tests
    # money = getMoney()
    # print(money)

    # setMoney(50)
    # printMoney()

    # setMoney()
    # printMoney()

    # money = getMoney()
    # print(money)

    #bet = setBet()
    #print(bet)

    #checkMoney()

    printMoney()

if __name__ == "__main__":
    main()