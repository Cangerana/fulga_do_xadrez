from node import Node


def mount_tree(player, state):
    checked_nodes = []
    max_deep = 1
    current_deep = 0

    stay = Node(action='STAY', vision_map=(player, state))
    flip = Node(action='FLIP', vision_map=(player, state))

    stay.score = evaluation(stay.vision_map, stay.action) 
    flip.score = evaluation(flip.vision_map, flip.action)

    checked_nodes.append(stay)
    checked_nodes.append(flip)
    return best_fit(checked_nodes).action


def is_coliding(piece, pos, player):
    if not pos:
        return False

    for posi in pos:
        posi[1] += 90
        if piece == 'torres':
            if 655 - posi[1] == 0:
                if abs(player - posi[0]) == 9:
                    return True
        if piece == 'bispos':
            if 655 - posi[1] == 270:
                if abs(player - posi[0]) == 252:
                    return True
        if piece == 'cavalos':
            if 655 - posi[1] == 90:
                if abs(player - posi[0]) == 168:
                    return True
        if piece == 'peoes':
            if 655 - posi[1] == 90:
                if player - posi[0] == 75 or player - posi[0] == -89:
                    return True
    return False


def evaluation(game_map, action):
    score = 0

    player = game_map[0]
    state = game_map[1]

    if action == 'FLIP':
        player = flip(player)
        score -= 5

    for piece, pos in state.items():
        score -= 20 if is_coliding(piece, pos, player) else 0

    return score


def flip(player):
    return 560 if player != 560 else 644


def best_fit(checked_nodes):
    best_node = checked_nodes[0]

    for node in checked_nodes:
        if node.score > best_node.score:
            best_node = node
    print(f'best node: {best_node}')
    return best_node
