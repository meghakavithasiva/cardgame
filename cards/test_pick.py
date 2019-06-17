from unittest import TestCase
import pick


class TestPick(TestCase):
    def test_init(self):
        self.pick = pick.Pick()
        self.assertNotEqual(self.pick.pick(10).__str__(), 'Y10')
        for i in range(15):
            self.player1 = self.pick.pick(i*2)
            self.player2 = self.pick.pick((i*2)+1)
            print('Round {}, Player1: {}, Player2: {}'.format(i+1, self.player1.__str__(), self.player2.__str__()))


