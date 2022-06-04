import time

from iterationAPI import *

from game import *


class Clubs:
    def __init__(self, home, away):
        self._home = home
        self.instance_home = Team(self._home)
        time.sleep(1)
        self._away = away
        self.instance_away = Team(self._away)
        time.sleep(1)
        self._teams = Game(self._home, self._away)
        print('Carregamento completo')

    @property
    def home(self):
        return str(self._home).upper().strip()

    @property
    def away(self):
        return str(self._away).upper().strip()

    @property
    def teams(self):
        return str(self._teams).upper().strip()

    # def home_team(self):
    #     print('Carregando time da casa')
    #     self._players = self.home_team_data()
    #     time.sleep(5)
    #     return self._players

    def home_team_data(self):
        self.home_data = self.instance_home.consult_team()
        self.players = self.instance_home.cast(self.home_data)
        return self.players_home

    def away_team_data(self):
        print('Carregando time da visitante')
        self.away_data = self.instance_away.consult_team()
        self.players = self.instance_away.cast(self.away_data)
        return self.players_away

    # def __init__(self, nome, ano, duracao):
    #    super().__init__(nome, ano)

        # with open('away.json', 'w') as outfile:
        #     json.dump(data['clubs'], outfile, indent=4)
        #     time.sleep(2)
        # print('away_created')


class Team:
    def __init__(self, team):
        self.team = team

    def consult_team(self):
        team_consult = str(self.team)
        id_team = consult_club_id(team_consult)
        self._team = consult_squad(id_team)
        return self._team

    def lineup(self, team):
        print(50 * '-')
        print(f'Jogadores do {team}')
        print(50 * '-')

    def cast(self, cast):
        self.lineup(self.team)
        for p in cast:
            print(f"Jogador: {p['name']} - Camisa: {p['shirt']}")

