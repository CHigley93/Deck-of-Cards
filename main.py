import random


class Card:
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suits = [1, 2, 3, 4]

    def __init__(self, suit: int, rank: int):
        if suit not in self.suits:
            raise ValueError("%d is not a valid suit." % suit)
        if rank not in self.nums:
            raise ValueError("%d is not a valid title." % rank)

        self.suit = suit
        self.rank = rank

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

    def __init__(self):
        cards = []
        self.cards = cards
        for s in range(1, 5):
            for r in range(1, 14):
                self.cards.append(Card(s, r))

    def __str__(self):
        names = ""
        count = 0
        for s in range(1, 5):
            for r in range(1, 14):
                if Card(s, r) in self.cards:
                    names += str(self.cards[count]) + ", "
                    count += 1
                    # print("stuff")
                    print(names)
                else:
                    print("%s is not in self.cards" % Card(s, r))
            names += "\n"
        return names

    def shuffle(self):
        for card in self.cards:
            self.cards.remove(card)


deck1 = Deck()
# deck1.shuffle()
print(deck1)
