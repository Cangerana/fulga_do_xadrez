def is_coliding(player, state, steps=0):
    for piece, pos in state.items():
        y = 655 - (90 * steps)
        for posi in pos:
            y_distance = y - posi[1]

            if abs(y_distance) <= 300:
                x_distance = player - posi[0]

                if y_distance == 270 and piece == 'bispos' and abs(x_distance) == 252:
                        return True
                elif y_distance == 90:
                    if piece == 'cavalos' and abs(x_distance) == 168:
                        return True
                    elif piece == 'peoes' and (x_distance == 75 or x_distance == -89):
                        return True
                elif y_distance == 0 and piece == 'torres' and abs(x_distance) == 9:
                        return True
            else:
                continue
    return False
