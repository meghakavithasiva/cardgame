from unittest import TestCase
import cards


class TestCards(TestCase):
    def test_init(self):
        self.cards1 = cards.Cards()
        self.assertEqual(len(self.cards1.cards), 30)


