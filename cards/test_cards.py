from unittest import TestCase
import cards


class TestCards(TestCase):
    def test_init(self):
        self.cards1 = cards.Cards()
        self.assertEqual('G1', self.cards1.cards[0].__str__())
        self.assertEqual('R1', self.cards1.cards[10].__str__())
        self.assertEqual('Y1', self.cards1.cards[20].__str__())

    def test_shuffle(self):
        self.cards1 = cards.Cards()
        cards2 = self.cards1.cards.copy()
        print(cards2[0])
        self.cards1.shuffle_cards()
        self.assertEqual(len(cards2), len(self.cards1.cards))

