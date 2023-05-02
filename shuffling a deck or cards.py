import random
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
cards = []
for suit in suits:
    for rank in ranks:
        cards.append(f"{rank} of {suit}")
random.shuffle(cards)
for i in range(8):
    print("Card", i + 1, ":", cards[i])
