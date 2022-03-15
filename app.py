from player import Player
from command import CommandParser


def game():
    print("GAME START!!!!遊戲開始!!!")
    a = Player(name='Player A')
    b = Player(name='Player B')
    parser = CommandParser(a, b)
    round = 1
    while True:
        print(f'================= Round {round} =================')
        if round % 2 == 1:
            print(f'{a.name} > ', end='')
            cmd = input()
            if not parser.parse(cmd, 'A'):
                return
        else:
            print(f'{b.name} > ', end='')
            cmd = input()
            if not parser.parse(cmd, 'B'):
                return
        round += 1


if __name__ == '__main__':
    game()
