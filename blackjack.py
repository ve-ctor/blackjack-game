# blackjack game using oop
from os import system, name
import random

def CreateReturnObj(status, obj):
    return {"ok": status, "returnObj": obj}

class Game:
    # Class which controls the flow of the game
    def __init__(self):
        self.AI = Player("Alana")
        self.Player = None
        self.Deck = Deck()

    def ClearOutput(self):
        # If you literally can't understand this function from the name I have nothing to say to you
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def MakeReaderFriendlyMenu(self, dictIn):
        # Transforms a dictionary into a menu with form [k] v
        output = ""

        sortedDict = sorted(dictIn.items())
        for k,v in sortedDict:
            output = output + "[" + str(k) + "] " + str(v) + ((sortedDict[-1][0] == str(k)) and " " or "\n") # Remove \n from end of string for cleanliness
        
        return output

class Player:
    # Player class to store the player's name, score, and track what's in their hand
    def __init__(self, pName, score=0, hand=[]):
        self.PlayerName = pName
        self.Score = score
        self.Hand = hand

class PlayingCard:
    # No explanation needed
    def __init__(self, suit, rank, value):
        self.Suit = suit
        self.Rank = rank
        self.Value = value
    
    def GetName(self):
        return (self.Rank + " of " + self.Suit)

class Deck:
    # Deck class
    # Able to shuffle the deck of cards and deal and remove cards from the deck to the players
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