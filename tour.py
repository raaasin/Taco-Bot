import pandas as pd
import math

def extract_team_names_from_csv(csv_file):
    colnames = ['teamname', 'player1', 'player2', 'player3', 'sub']
    df = pd.read_csv(csv_file, names=colnames, header=None)
    team_names = df['teamname'].tolist()
    return team_names

def gentourney():
    pass

def generate_double_elimination_bracket(team_names,tourney):
    team_names = extract_team_names_from_csv('teams.csv')
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

def regtourney():
    pass