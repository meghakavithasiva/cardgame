import cards


class Pick:

    def __init__(self):
        self.cards = cards.Cards()

    def pick(self):
        return self.cards.cards.pop()

    def __call__(self, *args):
        return self


