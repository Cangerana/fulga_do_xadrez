from models.heuristica import decision
from models.bfs import breadth_first_search
from utils.moves import flip
from utils.colision import is_coliding

from time import sleep

def get_action(state, model='heuristica'):
    if model == 'heuristica':
        action = decision(state)

    elif model == 'bfs':
        player = [state['player'], 0]
        paths = breadth_first_search(player, goal=-1000)

        return best_fit(paths, state)

    elif model == 'busca_em_largura':
        pass

    elif model == 'genetico_1':
        pass

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

    print(actions)
    for action in actions:
        if action == 'FLIP':
            player = flip(player)
            score -= 5
        col = is_coliding(player, state.copy(), steps=steps)
        if col:
            score -= 200
        steps += 1
    print(score)
    return score


def best_fit(paths, state):
    return max(paths, key=lambda x: evaluation(x[1], state))

