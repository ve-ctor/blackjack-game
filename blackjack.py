# blackjack game using oop
from os import system, name
import random

def CreateReturnObj(status, obj):
    return {"ok": status, "returnObj": obj}

class Game:
    def __init__(self):
        self.AI = Player("Alana")
        self.Player = None
        self.Deck = Deck()

    def ClearOutput(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def MakeReaderFriendlyMenu(self, dictIn):
        output = ""

        sortedDict = sorted(dictIn.items())
        for k,v in sortedDict:
            output = output + "[" + str(k) + "] " + str(v) + ((sortedDict[-1][0] == str(k)) and " " or "\n") # Remove \n from end of string for cleanliness
        
        return output

class Player:
    def __init__(self, pName, score=0):
        self.PlayerName = pName
        self.Score = score

class PlayingCard:
    def __init__(self, suit, rank, value):
        self.Suit = suit
        self.Rank = rank
        self.Value = value
    
    def GetName(self):
        return (self.Rank + " of " + self.Suit)

class Deck:
    def __init__(self):
        deck = []

        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        values = [1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10, 10, 10, 10]

        for s in suits:
            for r in range(0,len(ranks)):
                deck.append(PlayingCard(s, ranks[r], values[r]))

        self.Deck = deck

    def Shuffle(self):
        random.shuffle(self.Deck)
        return self.Deck

# testing code

for c in Game().Deck.Shuffle():
    print(c.GetName())