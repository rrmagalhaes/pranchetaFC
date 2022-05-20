import clubs

def start_match(home, away):
    clubs.Clubs(home, away)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    home = input("Time da Casa: ").upper().strip()
    away = input("Time Visitante: ").upper().strip()
    start_match(home, away)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
