class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.atk = 10
        self.hp = 100
        self.mp = 100

    def attack(self, opponent: 'Player') -> None:
        print(f'{self.name}: Take this!')
        opponent.__under_attack(self)
        pass

    def __under_attack(self, attacker: 'Player') -> None:
        print(f'{self.name}: Ouch!')
        pass
