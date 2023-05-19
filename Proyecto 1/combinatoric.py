import itertools


def total_team_value(players):
    best_value = 0
    win_team = []
    for team in itertools.permutations(range(len(players)), len(players[0])):
        team_value = 0
        for i, j in enumerate(team):
            team_value += players[j][i]

        if team_value > best_value:
            best_value = team_value
            win_team = team
    final_team = []
    for i, j in enumerate(win_team):
        final_team.append((j, i))
    return best_value, final_team
