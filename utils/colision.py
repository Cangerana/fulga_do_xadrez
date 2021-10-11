def is_coliding(player, state):
    for piece, pos in state.items():
        if not pos: continue

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
