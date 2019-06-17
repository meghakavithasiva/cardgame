import cards


class Pick:

    def __init__(self):
        self.cards = cards.Cards()

    def pick(self, index):
        return self.cards.cards[index]

    def __call__(self, *args):
        return self


