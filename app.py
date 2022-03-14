from player import Player
from command import CommandParser


def game():
    a = Player('A')
    b = Player('B')
    parser = CommandParser(a, b)
    round = 1
    while True:
        print(f'================= Round {round} =================')
        if round % 2 == 1:
            print('Player A > ', end='')
            cmd = input()
            if not parser.parse(cmd, 'A'):
                return
        else:
            print('Player B > ', end='')
            cmd = input()
            if not parser.parse(cmd, 'B'):
                return
        round += 1


if __name__ == '__main__':
    game()
