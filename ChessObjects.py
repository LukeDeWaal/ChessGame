import numpy as np


class GamePiece(object):

    def __init__(self):

        self.__position = None  # Position of Piece
        self.__name = None      # Name of Piece
        self.__symbol = None    # Symbol representing Piece
        self.__colour = None    # Colour of the team
        self.__id = -1          # Piece ID
        self.__status = False   # True for Alive, False for Dead

        self.__kils = []

    def __str__(self):
        return f"{self.get_name()}, position {self.get_position()}"

    def __eq__(self, other):
        if self.get_ID() == other.get_ID():
            if self.get_colour() == other.get_colour():
                return True
            else:
                return False
        else:
            return False

    def get_ID(self) -> int:
        return self.__id

    def set_ID(self, ID: int):
        self.__id = ID

    def get_position(self) -> np.array:
        return self.__position

    def set_position(self, position: np.array):
        self.__position = position

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_symbol(self) -> str:
        return self.__symbol

    def set_symbol(self, symbol: str):
        self.__symbol = symbol

    def get_colour(self) -> str:
        return self.__colour

    def set_colour(self, colour: str):
        self.__colour = colour

    def get_possible_moves(self, enemy_team):
        pass

    def get_inrange_enemies(self, enemy_team) -> list:
        pass

    def get_enemy_threats(self, enemy_team) -> list:
        pass


class Pawn(GamePiece):

    def __init__(self):

        GamePiece.__init__(self)

        self.set_name(name='Pawn')
        self.set_symbol(symbol='p')


class Rook(GamePiece):

    def __init__(self):

        GamePiece.__init__(self)

        self.set_name(name='Rook')
        self.set_symbol(symbol='R')


class Knight(GamePiece):

    def __init__(self):

        GamePiece.__init__(self)

        self.set_name(name='Knight')
        self.set_symbol(symbol='H')


class Bishop(GamePiece):

    def __init__(self):

        GamePiece.__init__(self)

        self.set_name(name='Bishop')
        self.set_symbol(symbol='B')


class Queen(GamePiece):

    def __init__(self):

        GamePiece.__init__(self)

        self.set_name(name='Queen')
        self.set_symbol(symbol='Q')


class King(GamePiece):

    def __init__(self):

        GamePiece.__init__(self)

        self.set_name(name='King')
        self.set_symbol(symbol='K')
