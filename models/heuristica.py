from utils.colision import is_coliding 

def decision(state):
    actions = [
        'STAY',
        'FLIP'
    ]
    return best_fit(actions, state)


def evaluation(player, state, action):
    def flip(player):
        return 560 if player != 560 else 644

    score = 0
    if action == 'FLIP':
        player = flip(player)
        score -= 5
    
    score -= 20 if is_coliding(player, state) else 0
    return score


def best_fit(actions, state):
    return max(actions, key=lambda x: evaluation(**state, action=x))
