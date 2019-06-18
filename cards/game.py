import cards
import pick


class Game:
    def __init__(self):
        self.pick = pick.Pick()
        self.rounds = []

    def start_game(self):
        for i in range(15):
            player1 = self.pick.pick(i*2)
            player2 = self.pick.pick((i*2)+1)
            self.rounds.append(Details(str(i+1), player1, player2))

    def print_result(self):
        print('Round    Player1    Player2    Winner')
        for round in self.rounds:
            print(round.__str__())


class Details:
    def __init__(self, round_number, player1, player2):
        self.round_number = round_number
        self.player1 = player1
        self.player2 = player2
        self.winner = 'Player 1'

    def __str__(self):
        return ' {}          {}         {}         {}'.format(self.round_number, self.player1.pretty(), self.player2.pretty(), self.winner)


game = Game()
game.start_game()
game.print_result()




