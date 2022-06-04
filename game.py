class Game:
    def __init__(self, home, away):
        # super().__init__(home, away)
        self._home_game = home
        self._away_game = away

    def opponents(self):
        game = self.__str__()
        print(game)

    def __str__(self):
        return f'{self._home_game} X {self._away_game}'


class Players:
    def __init__(self, cast):
        for p in cast:
            print(f"Jogador: {p['name']} - Camisa: {p['shirt']}")



class Staff:
    def __init__(self, name, office):
        self._name = name
        self._office = office


class Events:
    pass
