# from utils.moves import flip


def breadth_first_search(player, goal):
    tree = []
    tree.insert(0, ((player), []))

    visited = []

    actions = ['FLIP', 'STAY']

    while tree:
        state, path = tree.pop()

        if state[1] <= goal-90:
            break

        for action in actions:
            position = action_to_position(state.copy(), action)
            if position not in visited:
                visited.append(position)
            tree.insert(0, (position, path + [action]))

    return tree


def action_to_position(state, action):
    if action == 'FLIP':
        state[0] = flip(state)

    state[1] -= 90
    return state

def flip(player):
    return 560 if player != 560 else 644



if __name__ == '__main__':
    player = [644, 0]
    paths = breadth_first_search(player, goal=-700)
    print(paths)
