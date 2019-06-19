import random
import card


class Cards:

    def __init__(self):
        cards = list(map(lambda x: card.Card('B', x+1), range(10)))
        for i in list(map(lambda x: card.Card('R', x+1), range(10))):
            cards.append(i)
        for i in list(map(lambda x: card.Card('Y', x + 1), range(10))):
            cards.append(i)
        self.cards = cards
        random.shuffle(self.cards)

    def __str__(self) -> str:
        return ', '.join(map(str, self.cards))


