from utils.colision import is_coliding
from utils.moves import flip
from random import shuffle

def action_to_position(player, action):
    x = flip[player[0]] if action == 'FLIP' else player[0]
    return [x, player[1] - 90]


def get_actions(player, state):
    steps = int(abs(player[1]/90))
    mapa = ['STAY', 'FLIP']
    # shuffle(mapa)

    if is_coliding(player[0], state, steps=steps):
        mapa[0] = None
    if is_coliding(flip[player[0]], state, steps=steps):
        mapa[1] = None

    return mapa
