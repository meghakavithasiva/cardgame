import cards
from pick import Pick


class Game:
    def __init__(self):
        self.pick = Pick()
        self.rounds = []
        self.result = None
        self.details = []

    def start_game(self):
        self.result = Result()
        r = 1
        while len(self.pick.cards.cards) > 0:
            player1 = self.pick.pick()
            player2 = self.pick.pick()
            winner = self.workout_round(player1, player2)
            if winner == 1:
                self.result.player1.append(player1)
                self.result.player1.append(player2)
            else:
                self.result.player2.append(player1)
                self.result.player2.append(player2)
            details = Details(r, player1, player2, winner)
            r += 1
            # print(details.__str__())
            self.rounds.append(details)
            # next_pick = input('Continue y/n: ')
            # if next_pick == 'n':
            #     break
        self.result.details = self.rounds

    @staticmethod
    def workout_round(player1, player2):
        if player1.colour == player2.colour:
            if player1.value > player2.value:
                return 1
            else:
                return 2
        else:
            if player1.colour == 'R' and player2.colour == 'B':
                return 1
            if player1.colour == 'B' and player2.colour == 'R':
                return 2
            if player1.colour == 'Y' and player2.colour == 'R':
                return 1
            if player1.colour == 'R' and player2.colour == 'Y':
                return 2
            if player1.colour == 'B' and player2.colour == 'Y':
                return 1
            if player1.colour == 'Y' and player2.colour == 'B':
                return 2

    def print_result(self):
        if len(self.result.player1) > len(self.result.player2):
            print('Player 1 wins with {} cards.'.format(len(self.result.player1)))
        else:
            print('Player 2 wins with {} cards.'.format(len(self.result.player2)))

        print('Round    Player1    Player2    Winner')
        for round in self.rounds:
            print(round.__str__())


class Result:
    def __init__(self):
        self.player1 = []
        self.player2 = []
        self.details = None


class Details:
    def __init__(self, round_number, player1, player2, winner):
        self.round_number = round_number
        self.player1 = player1
        self.player2 = player2
        self.winner = winner

    def __str__(self):
        return ' {}          {}         {}         {}'.format(self.round_number, self.player1.pretty(),
                                                              self.player2.pretty(), self.winner)


game = Game()
game.start_game()
game.print_result()
