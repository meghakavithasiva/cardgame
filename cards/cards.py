import random
import card


class Cards:

    def __init__(self):
        colours = ['B', 'R', 'Y']
        random.shuffle(colours)
        self.cards = []
        for c in colours:
            self.cards = self.cards + list(map(lambda x: card.Card(c, x+1), range(10)))
        random.shuffle(self.cards)

    def __str__(self) -> str:
        return ', '.join(map(str, self.cards))

