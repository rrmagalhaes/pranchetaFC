import requests
import time


def consult_club_id(club):
    url = "https://transfermarket.p.rapidapi.com/search"
    querystring = {"query": f"{club}"}
    headers = {
        "X-RapidAPI-Host": "transfermarket.p.rapidapi.com",
        "X-RapidAPI-Key": "ce9d336f10mshb876dd2ba324aacp1d848ajsn6a81834eaddb"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    time.sleep(2)
    data = response.json()
    id_club = verify_club(data)

    return id_club


def verify_club(data):
    verify = data['count']['clubs']
    if verify != 0:
        data_clubs = data['clubs']
        list_club = [t for t in data_clubs if t['league'] == 'BRA1']
        return list_club[0]['id']
    else:
        return 'Club not exists'


def consult_squad(id_club):
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