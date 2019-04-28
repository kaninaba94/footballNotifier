import configparser

FILE = "config.ini"

config = configparser.ConfigParser()
config.read(FILE)
config.sections()

API_KEY = config['CONFIG']['API_KEY']
NUMBER = config['CONFIG']['NUMBER']
SENDER = config['CONFIG']['SENDER']
TEAMS = config['CONFIG']['TEAMS'].split(',')
team_list = []
for TEAM in TEAMS:
    team_list.append(TEAM.lower())
TEAMS = team_list

