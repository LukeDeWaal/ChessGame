import numpy as np


class PawnMoves(object):

    def __init__(self, start):

        self.coordinate = start

    def get_coordinate(self):
        return self.coordinate

    def normal_pawn_move(self, v_direction: 1 or -1):

        self.coordinate += np.array([v_direction, 0])

    def double_pawn_move(self, v_direction: 1 or -1):

        self.coordinate += np.array([2*v_direction, 0])

    def pawn_diagonal(self, v_direction: 1 or -1, d_direction: 1 or -1):

        self.coordinate += np.array(v_direction, d_direction)
