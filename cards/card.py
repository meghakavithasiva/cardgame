
class Card:
    def __init__(self, colour, value):
        self.colour = colour
        self.value = value

    def __str__(self) -> str:
        return '{}{}'.format(self.colour, self.value)

    def __call__(self, *args):
        return self

