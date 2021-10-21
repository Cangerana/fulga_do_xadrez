from utils.colision import is_coliding
from utils.moves import flip


def breadth_first_search(player, goal, game_state):
    tree = []
    tree.insert(0, ((player), []))

    visited = []
   
    while tree:
        player, path = tree.pop()

        if player[1] <= goal-90:
            break

        actions = get_actions(player, game_state)

        for action in actions:
            if action:
                position = action_to_position(player, action)
                if position not in visited:
                    visited.append(position)
                    tree.insert(0, (position, path + [action]))

    print(path)
    return path


def action_to_position(player, action):
    x = flip[player[0]] if action == 'FLIP' else player[0]
    return [x, player[1] - 90]


def get_actions(player, state):
    steps = int(abs(player[1]/90))
    mapa = ['STAY','FLIP']
    
    if is_coliding(player[0], state, steps=steps):
        mapa[0] = None
    if is_coliding(flip[player[0]], state, steps=steps):
        mapa[1] = None

    return mapa


if __name__ == '__main__':
    player = [644, 0]
    paths = breadth_first_search(player, goal=-180)
    for path in paths:
        print(path)
