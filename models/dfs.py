from models.model_ultils import *


def depthFirstSearch(player, goal, game_state):
    tree = []
    tree.append(((player), []))

    visited = []

    while tree:
        player, path = tree.pop()
        if player[1] <= goal-90:
            break

        actions = get_actions(player, game_state)
        for action in actions:
            position = action_to_position(player, action)
            if position not in visited:
                visited.append(position)
                tree.append((position, path + [action]))

    return path


def options(player_x, game_state):
    actions = ['atira', 'esquerada', 'direita', 'atira']

    for enime in enimes:
        if 'atirar':
            if is_coliding(player_x, game_state, atira=True):
                actions[0] = None
        if 'esquerada':
            if is_coliding(player_x-amt_move, game_state):
                actions[1] = None
        if 'direita':
            if is_coliding(player_x+amt_move, game_state):
                actions[2] = None
        if 'atira':
            if is_coliding(player_x, game_state):
                actions[3] = None

    return actions
