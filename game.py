class Game:
    def __init__(self, home, away):
        # super().__init__(home, away)
        self._home = home
        self._away = away

    def opponents(self):
        game = self.__str__()
        print(game)

    def __str__(self):
        return f'{self._home} X {self._away}'


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
