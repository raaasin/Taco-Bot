import pandas as pd
import math
import os

def is_bracket_generated(tournament_name):
    if tournament_name[-19:] == "_brac_generated.csv":
        return True
    else:
        return False

def does_tournament_exist():
    existing_tournaments = [file for file in os.listdir() if file.startswith('to_')]
    if existing_tournaments:
        return "".join(existing_tournaments)
    else:
        return False
    
def tourneybrac():
    try:
        if is_bracket_generated(does_tournament_exist()):
            return True
        else:
            return False
    except:
        return False
def tourneyexists():
    if does_tournament_exist(): 
        return True
    else:
        return False

def extract_team_names_from_csv(csv_file):
    colnames = ['teamname', 'player1', 'player2', 'player3', 'sub']
    df = pd.read_csv(csv_file, names=colnames, header=None)
    team_names = df['teamname'].tolist()
    return team_names

def gentourney(tourname):
    tournament_csv = f"to_{tourname}.csv"

    # Check if any existing tournament CSV files begin with 'to_'
    existing_tournaments = [file for file in os.listdir() if file.startswith('to_')]
    if existing_tournaments:
        print(existing_tournaments)
        return "Another tournament is already in progress. Please end the current tournament using the '/tourney end' command."

    # Create an empty CSV file for the tournament
    with open(tournament_csv, "w") as file:
        file.write("teamname,player1,player2,player3,sub\n")

    return f"Tournament '{tourname}' created successfully."

def generate_double_elimination_bracket(team_names):
    #check if tourney exists to generate
    existing_tournaments = [file for file in os.listdir() if file.startswith('to_')]
    if len(existing_tournaments)<1:
        return "There is no existing tournament, Please use /tourney generate to create a tournament"
    else:
        tourn="".join(existing_tournaments)
    team_names = extract_team_names_from_csv(tourn)
    num_teams = len(team_names)
    num_rounds = int(math.ceil(math.log2(num_teams)))
    num_matches = int(math.pow(2, num_rounds - 1))

    winners_bracket = []
    losers_bracket = []
    for i in range(num_matches):
        match_id = i + 1
        team1 = team_names[i * 2]
        team2 = team_names[i * 2 + 1]
        winners_bracket.append({'match_id': match_id, 'team1': team1, 'team2': team2, 'winner': None})

    bracket = {'winners_bracket': winners_bracket, 'losers_bracket': losers_bracket}
    #disable registration and de registering now
    return bracket


def update_match_result(bracket, match_id, winner):
    for match in bracket['winners_bracket']:
        if match['match_id'] == match_id:
            match['winner'] = winner
            break
    
    for match in bracket['losers_bracket']:
        if match['match_id'] == match_id:
            match['winner'] = winner
            break

    # Progress teams in the winners' bracket
    winners_bracket = bracket['winners_bracket']
    updated_winners_bracket = []
    for match in winners_bracket:
        if match['team1'] == winner:
            updated_winners_bracket.append({'match_id': match['match_id'] // 2, 'team1': winner, 'team2': None, 'winner': None})
        elif match['team2'] == winner:
            updated_winners_bracket.append({'match_id': match['match_id'] // 2, 'team1': None, 'team2': winner, 'winner': None})
        else:
            updated_winners_bracket.append(match)
    bracket['winners_bracket'] = updated_winners_bracket

    # Progress teams in the losers' bracket
    losers_bracket = bracket['losers_bracket']
    updated_losers_bracket = []
    for match in losers_bracket:
        if match['team1'] == winner:
            updated_losers_bracket.append({'match_id': match['match_id'] // 2, 'team1': winner, 'team2': None, 'winner': None})
        elif match['team2'] == winner:
            updated_losers_bracket.append({'match_id': match['match_id'] // 2, 'team1': None, 'team2': winner, 'winner': None})
        else:
            updated_losers_bracket.append(match)
    bracket['losers_bracket'] = updated_losers_bracket

def regtourney(player1,player2,player3,sub=None):
    #register for tourney, 
    #check if tourney exists
    #check if all players are registered users 
    #check if already registered 
    #check if brakcet generated already (no more registrations)
    pass
def unregtourney():
    #unregfor tourney
    #check if tourney exists
    #check if bracket generated already (no unreg now)
    pass



#Test
#print(tourneybrac())
#print(tourneyexists())