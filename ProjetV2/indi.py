import random
import sys
import threading

sys.setrecursionlimit(99999999)
threading.stack_size(200000000)



class Runner(object):

    def __init__(self, x1, y1, x2, y2, walls, end):
        self._pos_x_1 = x1
        self._pos_y_1 = y1
        self._pos_x_2 = x2
        self._pos_y_2 = y2
        self._is_alive = True
        self._walls = walls
        self._nbr_move = 0
        self._genes = []
        self._end = end
        self._fitness = 0

    def get_is_alive(self):
        return self._is_alive

    def _check_is_alive(self):
        walls = self._walls
        # on enlève 10 en x car le point spawn aux coords 10 10
        x1 = int(self._pos_x_1) - 10
        y1 = int(self._pos_y_1) - 10
        x2 = int(self._pos_x_2) + 10
        y2 = int(self._pos_y_2) + 10
        #print("Nouvelles coords (check_is_alive) : " + str(x1) + ":" + str(y1) + " " + str(x2) + ":" + str(y2))
        if (str(x1) + ":" + str(y1) + " " + str(x2) + ":" + str(y2)) in walls:
            #print("L'individu est mort...")
            self._is_alive = False
        else:
            return

    def set_alive(self):
        self._is_alive = True

    def new_pos(self, new_pos_var, direction):
        self._genes.append(direction)
        self._nbr_move = len(self._genes)
        self._set_pos_x1(int(new_pos_var[0]))
        self._set_pos_y1(int(new_pos_var[1]))
        self._set_pos_x2(int(new_pos_var[2]))
        self._set_pos_y2(int(new_pos_var[3]))
        self._check_is_alive()
        self.get_is_alive()
        #print("Nouvelles coords : " + str(int(new_pos[0])) + ":" + str(int(new_pos[1])) + " " + str(int(new_pos[2])) + ":" + str(int(new_pos[3])))
        #print(self._check_is_alive())
        #print("Vivant ? " + str(self.get_is_alive()))
        #print("_______________")

    def new_pos2(self, new_pos_var, direction, i):
        self._genes[i] = direction
        self._nbr_move = len(self._genes)
        self._set_pos_x1(int(new_pos_var[0]))
        self._set_pos_y1(int(new_pos_var[1]))
        self._set_pos_x2(int(new_pos_var[2]))
        self._set_pos_y2(int(new_pos_var[3]))
        self._check_is_alive()
        self.get_is_alive()

    def get_directions(self):
        return self._genes

    def get_nbr_moves(self):
        return self._nbr_move

    def _set_pos_x1(self, x1):
        self._pos_x_1 = x1

    def _set_pos_y1(self, y1):
        self._pos_y_1 = y1

    def _set_pos_x2(self, x2):
        self._pos_x_2 = x2

    def _set_pos_y2(self, y2):
        self._pos_y_2 = y2

    def set_last_value(self):
        nbr = random.randint(0, 3)
        print("nombre : " + str(nbr))
        while nbr == self._genes[len(self._genes) - 1]:
            print("c'était le même qu'avant zebi : ")
            nbr = random.randint(0, 3)
        self._genes[len(self._genes) - 1] = nbr

    def is_arrived(self):
        # on enlève 10 en x car le point spawn aux coords 10 10
        x1 = int(self._pos_x_1) - 10
        y1 = int(self._pos_y_1) - 10
        x2 = int(self._pos_x_2) + 10
        y2 = int(self._pos_y_2) + 10
        if x1 == self._end[0] and y1 == self._end[1] and x2 == self._end[2] and y2 == self._end[3]:
            return True
        else:
            return False

    def get_fitness(self):
        move = self._nbr_move
        diff_x = self._pos_x_2 - self._pos_x_1
        diff_y = self._pos_y_2 - self._pos_y_1

        pos_x = diff_x + self._pos_x_1
        pos_y = diff_y + self._pos_y_1

        diff_x_end =  self._end[2] - self._end[0]
        diff_y_end = self._end[3] - self._end[1]

        pos_x_end = diff_x_end + self._end[0]
        pos_y_end = diff_y_end + self._end[3]

        distance = round(((pos_x - pos_x_end) ** 2 + (pos_y - pos_y_end) ** 2) / 100)
        print("pos x : " + str(pos_x) + " pos y : " + str(pos_y) + " pos_x_end : " + str(pos_x_end) + " pos_y_end : " + str(pos_y_end))
        print("distance : " + str(distance))
        print("nombre moves : " + str(move))
        print("fitness : " + str(distance * move))

        self._fitness = distance * move

    def getter_fitness(self):
        return self._fitness

    def get_distance(self):
        diff_x = self._pos_x_2 - self._pos_x_1
        diff_y = self._pos_y_2 - self._pos_y_1

        pos_x = diff_x + self._pos_x_1
        pos_y = diff_y + self._pos_y_1

        diff_x_end = self._end[2] - self._end[0]
        diff_y_end = self._end[3] - self._end[1]

        pos_x_end = diff_x_end + self._end[0]
        pos_y_end = diff_y_end + self._end[3]

        distance = round(((pos_x - pos_x_end) ** 2 + (pos_y - pos_y_end) ** 2) / 100)
        return distance







