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
        return action

    elif model == 'bfs':
        sleep(3)
        s = datetime.now()
        player = [state['player'], 0]
        paths = breadth_first_search(
            player, goal=-90*103, game_state=state['state']
        )
        score = final_score(paths)
        print(score)
        print(datetime.now() -  s)
        return paths

    elif model == 'dfs':
        sleep(1)
        s = datetime.now()
        player = [state['player'], 0]
        paths = depthFirstSearch(
            player, goal=-90*33, game_state=state['state']
        )
        score = final_score(paths)
        print(datetime.now() -  s)
        print(score)
        
        # sleep(1)
        return paths

    elif model == 'GA':
        sleep(1)
        s = datetime.now()
        paths = ga(state=state)
        paths = list(
            map(lambda action: 'FLIP' if action == 1 else 'STAY', paths))
        print(datetime.now() -  s)

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


def final_score(actions):
    score = 0
    for action in actions:
        if action == 'FLIP':
            score -= 5
        score += 10
    return score


def best_fit(paths, state):
    return max(paths, key=lambda x: evaluation(x[1], state))
