import random


class Card:
    # possible values for rank and suit
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suits = [1, 2, 3, 4]

    # Initialize card with valid rank and suit
    def __init__(self, suit: int, rank: int):
        if suit not in self.suits:
            raise ValueError("%d is not a valid suit." % suit)
        if rank not in self.nums:
            raise ValueError("%d is not a valid title." % rank)

        self.suit = suit
        self.rank = rank

    # Change the __str__ method so it prints out in "rank of suit" format
    def __str__(self):
        if self.suit == 1:
            suit = "Clubs"
        elif self.suit == 2:
            suit = "Diamonds"
        elif self.suit == 3:
            suit = "Hearts"
        elif self.suit == 4:
            suit = "Spades"

        if self.rank == 1:
            rank = "Ace"
        elif 1 < self.rank < 11:
            rank = str(self.rank)
        elif self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"

        return rank + " of " + suit


class Deck():
    # create a standard deck of 52 cards
    def __init__(self):
        cards = []
        self.cards = cards
        for s in range(1, 5):
            for r in range(1, 14):
                self.cards.append(Card(s, r))

    # Change __str__ method so that the deck prints out each card with each suit on a different line
    # This is currently not working and is what I am focusing on to fix
    def __str__(self):
        names = ""
        count = 0
        for s in range(1, 5):
            for r in range(1, 14):
                if Card(s, r) in self.cards:
                    names += str(self.cards[count]) + ", "
                    count += 1
                # a temp else statement to help me while I figure out what is going wrong
                else:
                    print("%s is not in self.cards" % Card(s, r))
            names += "\n"
        return names

    # Shuffle method to randomly change the order of the cards, currently being used to test the __str__ method
    def shuffle(self):
        for card in self.cards:
            self.cards.remove(card)


deck1 = Deck()
# deck1.shuffle()
print(deck1)
