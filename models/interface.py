from models.heuristica import decision
from models.bfs import breadth_first_search
from models.dfs import depthFirstSearch
from models.ga import ga
from utils.moves import flip
from utils.colision import is_coliding

from time import sleep
from datetime import datetime


def get_action(state, model='heuristica'):
    if model == 'heuristica':
        action = decision(state)

    elif model == 'bfs':
        player = [state['player'], 0]
        paths = breadth_first_search(
            player, goal=-90*20, game_state=state['state'])

        return paths

    elif model == 'dfs':
        player = [state['player'], 0]
        paths = depthFirstSearch(
            player, goal=-90*20, game_state=state['state'])

        return paths

    elif model == 'GA':
        paths = ga(state=state)
        paths = list(map(lambda action: 'FLIP' if action == 1 else 'STAY', paths))

        return paths

    elif model == 'genetico_2':
        pass

    else:
        action = None
    return action


def evaluation(actions, state):
    player = state['player']
    state = state['state']

    score = 0
    steps = 1

    for action in actions:
        if action == 'FLIP':
            score -= 5
            player = flip[player]

        if is_coliding(player, state, steps=steps):
            return score - 200

        steps += 1

    return score


def best_fit(paths, state):
    return max(paths, key=lambda x: evaluation(x[1], state))
