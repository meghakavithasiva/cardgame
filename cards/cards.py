import random
import card


class Cards:

    def __init__(self):
        colours = ['B', 'R', 'Y']
        random.shuffle(colours)
        self.cards = []
        for c in colours:
            for i in range(10):
                self.cards.append(card.Card(c, i+1))

        random.shuffle(self.cards)

    def __str__(self) -> str:
        return ', '.join(map(str, self.cards))

