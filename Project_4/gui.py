import objects as ob
import db
import locale as lc
import tkinter as tk
from tkinter import ttk
from datetime import datetime


class BlackjackFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        result = lc.setlocale(lc.LC_ALL, '')
        if result == 'C':
            lc.setlocale(lc.LC_ALL, 'en_US')        
        global newSession

        startTime = datetime.now()

        db.connect()
        db.create_session()
        lastSession = db.get_last_session()
        newSession = ob.Session(lastSession.sessionID + 1, startTime, lastSession.stopMoney, None, lastSession.stopMoney)
        # Define string variables for text entry fields
        self.moneyLabel = tk.StringVar()
        self.betEntry = tk.DoubleVar()
        self.dealerCardsLabel = tk.StringVar()
        self.dealerPointsLabel = tk.StringVar()
        self.playerCardsLabel = tk.StringVar()
        self.playerPointsLabel = tk.StringVar()
        self.resultLabel = tk.StringVar()

        self.moneyLabel.set(lc.currency(lastSession.stopMoney))
        self.initComponents()

    def initComponents(self):
        self.pack()

        ttk.Label(self, text = "Money:").grid(column = 0, row = 0, sticky = tk.E)
        ttk.Entry(self, width = 25, textvariable = self.moneyLabel, state = "readonly").grid(column = 1, row = 0, sticky = tk.W)

        ttk.Label(self, text = "Bet:").grid(column = 0, row = 1, sticky = tk.E)
        ttk.Entry(self, width=25, textvariable = self.betEntry).grid(column = 1, row = 1, sticky = tk.W)

        ttk.Label(self, text = "DEALER").grid(column = 0, row = 2, sticky = tk.E )

        ttk.Label(self, text = "Cards:").grid(column = 0, row = 3, sticky = tk.E)
        ttk.Entry(self, width = 50, textvariable = self.dealerCardsLabel, state = "readonly").grid(column = 1, row = 3, sticky = tk.W)

        ttk.Label(self, text = "Points:").grid(column = 0, row = 4, sticky = tk.E)
        ttk.Entry(self, width = 25, textvariable = self.dealerPointsLabel, state = "readonly").grid(column = 1, row = 4, sticky = tk.W)

        ttk.Label(self, text = "YOU").grid(column = 0, row = 5, sticky = tk.E )

        ttk.Label(self, text = "Cards:").grid(column = 0, row = 6, sticky = tk.E)
        ttk.Entry(self, width = 50, textvariable = self.playerCardsLabel, state = "readonly").grid(column = 1, row = 6, sticky = tk.W)

        ttk.Label(self, text = "Points:").grid(column = 0, row = 7, sticky = tk.E)
        ttk.Entry(self, width = 25, textvariable = self.playerPointsLabel, state = "readonly").grid(column = 1, row = 7, sticky = tk.W)

        ttk.Label(self, text = "RESULT:").grid(column = 0, row = 9, sticky = tk.E)
        ttk.Entry(self, width = 50, textvariable = self.resultLabel, state = "readonly").grid(column = 1, row = 9, sticky = tk.W)

        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons(self):
        buttonFrameOne = ttk.Frame(self)

        buttonFrameOne.grid(column = 1, row = 8, columnspan = 2, sticky = tk.W)

        ttk.Button(buttonFrameOne, text = "Hit", command = self.hit).grid(column= 0, row= 0)
        ttk.Button(buttonFrameOne, text = "Stand", command = self.stand).grid(column = 1, row= 0)

        buttonFrameTwo = ttk.Frame(self)

        buttonFrameTwo.grid(column = 1, row = 10, columnspan = 2, sticky = tk.W)

        ttk.Button(buttonFrameTwo, text = "Play", command = self.play).grid(column= 0, row= 0)
        ttk.Button(buttonFrameTwo, text = "Exit", command =self.exit).grid(column = 1, row= 0)

    def play(self):
        global winState
        global deck
        global playerHand
        global dealerHand
        global bet
        global money
        global newSession

        bet = self.betEntry.get()
        money = newSession.stopMoney
        if bet > 0 and bet <= money:
            self.resultLabel.set("")
            winState = "normal"

            deck = ob.Deck()
            deck.shuffle()
            
            playerHand = ob.Hand()
            dealerHand = ob.Hand()
            for i in range(2):
                playerHand.addCard(deck.dealCard())
                dealerHand.addCard(deck.dealCard())
            
            self.dealerCardsLabel.set(ob.dealerShowcard(dealerHand))
            self.dealerPointsLabel.set(dealerHand.showCardPoints())
            self.playerCardsLabel.set(ob.printHand(playerHand))
            self.playerPointsLabel.set(playerHand.points())

            if playerHand.points() == 21:
                winState = "blackjack"
                self.resultLabel.set("Blackjack! You Won!")
                money = round(money + (1.5 * bet), 2)
                newSession.stopMoney = money
                self.moneyLabel.set(lc.currency(money))

        else:
            self.resultLabel.set("You must place a valid bet to play")
    
    def hit(self):
        global winState
        global money
        global bet

        if playerHand.points() < 22:
            playerHand.addCard(deck.dealCard())
            self.playerCardsLabel.set(ob.printHand(playerHand))
            self.playerPointsLabel.set(playerHand.points())
        
        if playerHand.points() > 21 and winState == "normal":
                winState = "playerLost"
                self.resultLabel.set("Sorry, you busted!")
                money = round(money - bet, 2)
                newSession.stopMoney = money
                self.moneyLabel.set(lc.currency(money))

    def stand(self):
        global winState
        global money
        global bet

        if winState == "normal":
            while winState == "normal":
                self.dealerCardsLabel.set(ob.printHand(dealerHand))
                self.dealerPointsLabel.set(dealerHand.points())
                if dealerHand.points() > 21 or dealerHand.points() >= 17:
                    winState = "done"
                    break
                dealerHand.addCard(deck.dealCard())
                self.dealerCardsLabel.set(ob.printHand(dealerHand))
                self.dealerPointsLabel.set(dealerHand.points())
                if dealerHand.points() > 21 or dealerHand.points() >= 17:
                    winState = "done"
            if dealerHand.points() > playerHand.points() and dealerHand.points() <= 21:
                winState = "playerLost"
                self.resultLabel.set("Sorry, you lost!")
                money = round(money - bet, 2)
                newSession.stopMoney = money
                self.moneyLabel.set(lc.currency(money))
            if dealerHand.points() < playerHand.points() or dealerHand.points() > 21:
                winState = "playerWins"
                self.resultLabel.set("Hooray! You won!")
                money = round(money + bet, 2)
                newSession.stopMoney = money
                self.moneyLabel.set(lc.currency(money))
            if dealerHand.points() == playerHand.points():
                winState = "push"
                self.resultLabel.set("It's a tie!")
        
    def exit(self):
        result = lc.setlocale(lc.LC_ALL, '')
        if result == 'C':
            lc.setlocale(lc.LC_ALL, 'en_US')
        endTime = datetime.now()
        newSession.stopTime = endTime
        db.connect()
        db.add_session(newSession)
        db.close()
        root.destroy()




if __name__ == "__main__":
    root = tk.Tk()
    root.title("Blackjack")
    BlackjackFrame(root)
    root.mainloop()