from player import Player


class CommandParser():
    def __init__(self, playerA: Player, playerB: Player) -> None:
        self.players = {'A': playerA, 'B': playerB}

    def parse(self, command: str, sender_id: str) -> bool:
        sender = self.players[sender_id]
        if command.lower() == 'attack':
            opponent_id = 'A' if sender_id == 'B' else 'B'
            opponent = self.players[opponent_id]
            sender.attack(opponent)
        elif command.lower() == 'quit':
            return False
        return True
