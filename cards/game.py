import cards
import os.path
from pick import Pick

class Game:
    def __init__(self):
        self.user1 = ''
        self.user2 = ''

        self.login()
        self.pick = Pick()
        self.rounds = []
        self.result = None
        self.details = []

    def start_game(self):
        self.result = Result()
        r = 1
        while len(self.pick.cards.cards) > 0:
            p1 = input(self.user1 + ' pick card (press enter)')
            player1 = self.pick.pick()
            print(player1.colour + str(player1.value))
            p2 = input(self.user2 + ' pick card (press enter)')
            player2 = self.pick.pick()
            print(player2.colour + str(player2.value))
            winner = self.workout_round(player1, player2)
            if winner == 1:
                self.result.player1.append(player1)
                self.result.player1.append(player2)
                details = Details(r, player1, player2, self.user1)
            else:
                self.result.player2.append(player1)
                self.result.player2.append(player2)
                details = Details(r, player1, player2, self.user2)
            print('Round      ' + self.user1 + '     ' + self.user2 + '  winner')
            print(details.__str__())
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
            print(self.user1 + ' wins with {} cards.'.format(len(self.result.player1)))
            self.addToResults(self.user1, len(self.result.player1))
            print(self.result.pretty1())
        else:
            print(self.user2 + ' wins with {} cards.'.format(len(self.result.player2)))
            self.addToResults(self.user2, len(self.result.player2))
            print(self.result.pretty2())

        print('Round    ' + self.user1 + '    ' + self.user2 + '    Winner')
        for round in self.rounds:
            print(round.__str__())

        self.printLastFiveTopScores()

    def printLastFiveTopScores(self):
        results = []
        with open("results", 'r') as f:
            for line in f:
                splitted = line.split('|')
                player = str(splitted[0])
                quantity = int(splitted[1].rstrip())
                results.append(ResultToPrint(player, quantity))
        results.sort(key=lambda x: x.quantity, reverse = True)
        print('*********** Top 5 players')
        for i in range(len(results)):
            if i == 5 or i == len(results):
                return
            p = results[i]
            print(p.player + ', ' +  str(p.quantity))

    def addToResults(self, user, quantity):
        f = open('results', 'a')
        f.write(user + '|' + str(quantity) + '\n')
        f.close()

    def login(self):
        for i in range(2):
            name = input('Enter Player' + str(i+1) + ': ')
            pwd = input("Enter password:  ")
            pwd = pwd.rstrip()
            file_name='..'+ os.sep + 'user' + os.sep + 'user.txt'
            if os.path.isfile(file_name):
                with open(file_name, 'r') as f:
                    for line in f:
                        splitted = line.split('|')
                        username = splitted[0]
                        userpwd = splitted[1].rstrip()
                        if username == name:
                            if pwd != userpwd :
                                raise WrongPasswordException('wrong password')
                            else:
                                print('Good user')
                                if i == 0:
                                    self.user1 = name
                                else:
                                    self.user2 = name

        if not self.user1:
            raise WrongUserException('Wrong Player1, please add player first by running user.py')
        if not self.user2:
            raise WrongUserException('Wrong Player2, please add player first by running user.py')


class Result:
    def __init__(self):
        self.player1 = []
        self.player2 = []
        self.details = None
    def pretty1(self):
        s = ''
        for c in self.player1:
            s = s + str(c) + ','
        return s
    def pretty2(self):
        s = ''
        for c in self.player2:
            s = s + str(c) + ','
        return s

class Details:
    def __init__(self, round_number, player1, player2, winner):
        self.round_number = round_number
        self.player1 = player1
        self.player2 = player2
        self.winner = winner

    def __str__(self):
        return ' {}          {}         {}         {}'.format(self.round_number, self.player1.pretty(),
                                                              self.player2.pretty(), self.winner)

class ResultToPrint:
    def __init__(self, player, quantity):
        self.player = player
        self.quantity = quantity


class WrongPasswordException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class WrongUserException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

game = Game()
game.start_game()
game.print_result()
