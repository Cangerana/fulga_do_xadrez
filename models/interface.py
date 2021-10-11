from models.heuristica import decision


def get_action(state, model='heuristica'):
    if model == 'heuristica':
        action = decision(state)
    elif model == 'busca_em_largura':
        pass
    elif model == 'busca_em_largura':
        pass
    elif model == 'genetico_1':
        pass
    elif model == 'genetico_2':
        pass
    else:
        action = None
    return action