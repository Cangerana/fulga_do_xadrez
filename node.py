class Node:
    def __init__(self, score=None, action='', vision_map=()):
        self.vision_map = vision_map
        self.score = score
        self.action = action
        self.stay = None
        self.flip = None


    def __str__(self):
        return f'Action: {self.action} |>|>| Score: {self.score}' 