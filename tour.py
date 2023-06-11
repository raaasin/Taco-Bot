import math

# Generate the initial bracket with placeholder values
def generate_bracket(teams):
    num_teams = len(teams)
    num_rounds = int(math.ceil(math.log2(num_teams)))

    # Calculate the size of the bracket
    bracket_size = 2 ** num_rounds

    # Generate the initial bracket with placeholder values
    bracket = [[None] * bracket_size for _ in range(num_rounds)]

    # Fill in the teams in the first round
    for i, team in enumerate(teams):
        bracket[0][i] = team

    return bracket

# Update the bracket with match results
def update_bracket(bracket, round_num, match_num, winner):
    bracket[round_num][match_num] = winner

# Print the bracket
def print_bracket(bracket):
    num_rounds = len(bracket)
    round_width = len(bracket[0])

    for round in range(num_rounds):
        spacing = round_width // (2 ** (round + 1))
        for i in range(round_width):
            if i % (2 * spacing) == 0:
                print(' ' * spacing, end='')

            if round == 0:
                print(bracket[round][i].center(spacing * 2), end='')
            else:
                match_result = bracket[round][i]
                if match_result is not None:
                    print(match_result.center(spacing * 2), end='')
                else:
                    print(' ' * (spacing * 2), end='')

        print()

# Example usage
teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E', 'Team F', 'Team G', 'Team H']
bracket = generate_bracket(teams)

# Initial bracket
print("Initial Bracket:")
print_bracket(bracket)
print()

# Update bracket with match results
for round_num in range(1, len(bracket)):
    print(f"Round {round_num} matches:")
    for match_num in range(len(bracket[round_num])):
        team1 = bracket[round_num-1][2*match_num]
        team2 = bracket[round_num-1][2*match_num+1]

        if team1 is None or team2 is None:
            break

        print(f"Match {match_num+1}: {team1} vs. {team2}")

        valid_input = False
        while not valid_input:
            winner = input("Enter the winner: ")
            if winner == team1 or winner == team2:
                valid_input = True
            else:
                print("Invalid input. Please enter the name of one of the teams in the match.")

        update_bracket(bracket, round_num, match_num, winner)

    print()

# Updated bracket
print("Updated Bracket:")
print_bracket(bracket)
