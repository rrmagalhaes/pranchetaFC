import time

from game import *


class Clubs:
    def __init__(self, home, away):
        self._home = Team(home)
        self._away = Team(away)
        self._teams = Game(self._home, self._away)

    @property
    def home(self):
        return self._home

    @property
    def away(self):
        return self._away

    @property
    def teams(self):
        return str(self._teams)

    @property
    def home_team(self):
        home_team = self.consult_home()
        self.lineup(self.home)
        self._home_team_players = Players(home_team)
        return self._home_team_players

    @property
    def away_team(self):
        away_team = self.consult_away()
        self.lineup(self.away)
        self._away_team_players = Players(away_team)
        return self._away_team_players

    # def __init__(self, nome, ano, duracao):
    #    super().__init__(nome, ano)

    def lineup(self, club):
        print(50 * '-')
        print(f'Jogadores do {club}')
        print(50 * '-')

    def consult_home(self):
        home = str(self.home).upper().strip()
        id_home = self.consult_club_id(home)
        self._home_team = self.consult_squad(id_home)
        return self._home_team

    def consult_away(self):
        away = str(self.away).upper().strip()
        id_away = self.consult_club_id(away)
        self._away_team = self.consult_squad(id_away)
        return self._away_team

        # with open('away.json', 'w') as outfile:
        #     json.dump(data['clubs'], outfile, indent=4)
        #     time.sleep(2)
        # print('away_created')

    def consult_club_id(self, club):
        url = "https://transfermarket.p.rapidapi.com/search"
        querystring = {"query": f"{club}"}
        headers = {
            "X-RapidAPI-Host": "transfermarket.p.rapidapi.com",
            "X-RapidAPI-Key": "ce9d336f10mshb876dd2ba324aacp1d848ajsn6a81834eaddb"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        time.sleep(2)
        data = response.json()
        id_club = self.verify_club(data)

        return id_club

    def verify_club(self, data):
        verify = data['count']['clubs']
        if verify != 0:
            data_clubs = data['clubs']
            list_club = [t for t in data_clubs if t['league'] == 'BRA1']
            return list_club[0]['id']
        else:
            return 'Club not exists'

    def consult_squad(self, id_club):
        url = f'https://transfermarket.p.rapidapi.com/clubs/get-squad?id={id_club}'
        payload = {}
        headers = {
            'X-RapidAPI-Host': 'transfermarket.p.rapidapi.com',
            'X-RapidAPI-Key': 'ce9d336f10mshb876dd2ba324aacp1d848ajsn6a81834eaddb'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()

        players = []
        for p in data['squad']:
            if p['isGoalkeeper']:
                position = 'Goalkepper'
                players.append({'shirt': p['shirtNumber'], 'name': p['name'], 'position': position})
            else:
                position = 'Line Player'
                players.append({'shirt': p['shirtNumber'], 'name': p['name'], 'position': position})

        return players


class Team:
    def __init__(self, team):
        self.team = team

    def cast(self, cast):
        for p in cast:
            print(f"Jogador: {p['name']} - Camisa: {p['shirt']}")

