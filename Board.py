import numpy as np
from Team import  WhiteTeam, BlackTeam


positions = {}
positions['Pawn']   = [[np.array([j, i]) for i in range(8)] for j in (1, 6)]
positions['Rook']   = [[np.array([j, i]) for i in (0, 7)] for j in (0, 7)]
positions['Knight'] = [[np.array([j, i]) for i in (1, 6)] for j in (0, 7)]
positions['Bishop'] = [[np.array([j, i]) for i in (2, 5)] for j in (0, 7)]
positions['Queen']  = [[np.array([j, i]) for i in (3, )] for j in (0, 7)]
positions['King']   = [[np.array([j, i]) for i in (4, )] for j in (0, 7)]


class Board(object):

    def __init__(self, team_1, team_2):

        self.__coordinates = np.zeros((8, 8))
        self.__teams = {'T1': team_1, 'T2': team_2}

        self.__assemble_board()

    def __assemble_board(self):

        for idx_1, team in enumerate(self.get_teams().values()):
            for kind in positions.keys():
                for idx_2, item in enumerate(team.get_all_of_a_type(kind)):
                    position = positions[kind][idx_1][idx_2]
                    item.set_position(position)
                    self.__coordinates[position[0], position[1]] = item.get_ID()

    def move_piece(self, team, ID, move):
        pass

    def print_coordinates(self):
        print(self.__coordinates)

    def get_coordinates(self):
        return self.__coordinates

    def get_teams(self):
        return self.__teams


if __name__ == "__main__":

    team1 = BlackTeam()
    team2 = WhiteTeam()

    board = Board(team1, team2)
    board.print_coordinates()