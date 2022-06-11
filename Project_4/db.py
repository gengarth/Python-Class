# Functions that access the money for blackjack program
import sys
import locale
import sqlite3
from contextlib import closing

from objects import Session

conn = None

def connect():
    global conn
    conn = sqlite3.connect("session_db.sqlite") 

def close():
    if conn:   
        conn.close()

def create_session(): 
    c = conn.cursor()
    sql = ('''CREATE TABLE IF NOT EXISTS Session 
            (sessionID INTEGER PRIMARY KEY, startTime TEXT, startMoney REAL, stopTime TEXT, stopMoney REAL);''')
    with closing(conn.cursor()) as c:
        c.execute(sql)
        conn.commit()

    lastSession = get_last_session()

    if lastSession == None:
        sql = ('''INSERT INTO Session (sessionID, startTime, startMoney, stopTime, stopMoney)
                VALUES (0, 'x', 199, 'y', 199); ''')
        with closing(conn.cursor()) as c:
            c.execute(sql)
            conn.commit()



def get_last_session():
    query = '''SELECT * FROM Session ORDER BY sessionID DESC;'''
    c = conn.cursor()

    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()
        lastSessionFields = c.fetchone()
        if lastSessionFields != None:
            lastSession = Session(lastSessionFields[0], lastSessionFields[1], lastSessionFields[2], lastSessionFields[3], lastSessionFields[4])
            return lastSession

def add_session(Session):
    query = '''INSERT INTO Session (sessionID, startTime, startMoney, stopTime, stopMoney) 
                    VALUES (?, ?, ?, ?, ?)'''
    c = conn.cursor()
    
    with closing(conn.cursor()) as c:
        c.execute(query, (Session.sessionID, Session.startTime, Session.startMoney, Session.stopTime, Session.stopMoney))
        conn.commit()
    
# def getMoney():
#     try:
#         with open("money.txt") as file:
#             money = file.read()
#             return round(float(money), 2)
#     except FileNotFoundError:
#         print("Could not find money.txt")
#     except OSError:
#         print("File found - error reading file")
#     except Exception:
#         print("Unknown error occured")

# def setMoney(money):
#     try:
#         with open("money.txt", "w") as file:
#             moneyRounder = round(money, 2)
#             file.write(str(moneyRounder))
#     except FileNotFoundError:
#         print("Could not find money.txt")
#     except OSError:
#         print("File found - error wrtiting file")
#     except Exception:
#         print("Unknown error occured")

# def printMoney():
#     try:
#         osCheck = locale.setlocale(locale.LC_ALL,'')
#         if osCheck =="C":
#             locale.setlocale(locale.LC_ALL, "en_US")

#         with open("money.txt") as file:
#             money = file.read()
#             print("Money:\t" + locale.currency(float(money), grouping = True))   
#     except FileNotFoundError:
#         print("Could not find money.txt")
#     except OSError:
#         print("File found - error reading file")
#     except Exception:
#         print("Unknown error occured")

# def setBet(bet):
#     osCheck = locale.setlocale(locale.LC_ALL,'')
#     if osCheck =="C":
#         locale.setlocale(locale.LC_ALL, "en_US")

#     while True:
#         try:
#             if bet < 5 or bet > 1000:
#                 print("Minimum bet is" + locale.currency(5) + ". Maximum bet is " + 
#                 locale.currency(1000) + ". " + "Please try again!")
#             elif bet > getMoney():
#                 print("Bet can't be bigger than current money " +
#                 "which is " + str(getMoney()))
#             else:
#                 return bet
#         except ValueError:
#             print("Must enter a number")


# def checkMoney():
#     osCheck = locale.setlocale(locale.LC_ALL,'')
#     if osCheck =="C":
#         locale.setlocale(locale.LC_ALL, "en_US")
#     if getMoney() < 5:
#         while True:
#             addChips = input("Can't cover minimum bet, enter 'y' " +
#             "to add " + locale.currency(100)  + " or 'n' to quit! (y/n)\t")
#             if addChips.lower() == "y":
#                 setMoney(getMoney() + 100)
#                 break
#             elif addChips.lower() == "n":
#                 print("Thanks for playing, see you next time!")
#                 sys.exit()
#             else:
#                 print("Must enter either 'y' or 'n'. Please try again! (y/n)\t")


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

    #printMoney()

    connect()
    create_session()
    session = get_last_session()
    print("Money:", session.stopMoney)
    
    # count = 20
    # while count < 30:
    #     newSession = Session(2 + count, 4 +count, 5 + count , 3 + count , 1 + count)
    #     add_session(newSession)
    #     count+=1
    close()

if __name__ == "__main__":
    main()