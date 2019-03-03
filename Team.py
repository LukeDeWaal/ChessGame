import numpy as np

from ChessObjects import *


class Team(object):

    @staticmethod
    def __assign_ID(piece, ID):
        piece.set_ID(ID)

    def __init__(self):

        self.__alive_pieces = [King(), Queen(), Bishop(), Bishop(), Knight(), Knight(), Rook(), Rook()] + [Pawn() for _ in range(8)]
        self.__dead_pieces = []
        self.__possible_moves = {}
        self.__possible_attacks = {}
        self.__possible_threats = {}
        self.__colour = None
        self.__piece_ids = []

        self.assign_IDs(range(0, 16))

    def move_piece(self, ID, move):
        pass

    def get_all_of_a_type(self, which):
        return [piece for piece in self.get_all_pieces() if piece.get_name() == which]

    def get_all_pieces(self):
        return self.get_live_pieces() + self.get_dead_pieces()

    def get_live_pieces(self) -> list:
        return self.__alive_pieces

    def get_dead_pieces(self) -> list:
        return self.__dead_pieces

    def kill_piece(self, piece_id):

        for idx, piece_i in enumerate(self.get_live_pieces()):
            if piece_i == piece_id:
                self.get_dead_pieces().append(self.get_live_pieces().pop(idx))
                break
            else:
                continue

    def raise_piece_from_dead(self, piece_id):
        pass

    def add_live_piece(self, piece):
        self.get_live_pieces().append(piece)

    def get_colour(self) -> str:
        return self.__colour

    def set_colour(self, colour):
        self.__colour = colour

        for piece in self.get_all_pieces():
            piece.set_colour(self.__colour)

    def get_IDs(self) -> list:
        return self.__piece_ids

    def assign_IDs(self, IDs):
        for piece, ID in zip(self.get_live_pieces(), IDs):
            self.__piece_ids.append(ID)
            self.__assign_ID(piece, ID)

    def __calculate_possible_moves(self, enemy_team):

        for piece in self.get_live_pieces():
            self.__possible_moves[piece.get_ID()] = piece.get_possible_moves(enemy_team=enemy_team)

    def __calculate_enemy_threats(self, enemy_team):

        for piece in self.get_live_pieces():
            self.__possible_threats[piece.get_ID()] = piece.get_enemy_threats(enemy_team=enemy_team)

    def __calculate_possible_attacks(self, enemy_team):

        for piece in self.get_live_pieces():
            self.__possible_attacks[piece.get_ID()] = piece.get_inrange_enemies(enemy_team=enemy_team)

    def get_possible_moves(self, enemy_team):
        self.__calculate_possible_moves(enemy_team=enemy_team)
        return self.__possible_moves

    def get_possible_attacks(self, enemy_team):
        self.__calculate_possible_attacks(enemy_team=enemy_team)
        return self.__possible_attacks

    def get_possible_threats(self, enemy_team):
        self.__calculate_enemy_threats(enemy_team=enemy_team)
        return self.__possible_threats


class WhiteTeam(Team):

    def __init__(self):

        Team.__init__(self)

        self.set_colour('White')


class BlackTeam(Team):

    def __init__(self):

        Team.__init__(self)

        self.set_colour('Black')
