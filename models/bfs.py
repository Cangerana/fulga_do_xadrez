from models.model_ultils import *


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


if __name__ == '__main__':
    player = [644, 0]
    paths = breadth_first_search(player, goal=-180)
    for path in paths:
        print(path)
