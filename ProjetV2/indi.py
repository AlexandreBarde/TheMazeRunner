class Runner(object):

    def __init__(self, x1, y1, x2, y2, walls):
        self._pos_x_1 = x1
        self._pos_y_1 = y1
        self._pos_x_2 = x2
        self._pos_y_2 = y2
        self._is_alive = True
        self._walls = walls
        self._nbr_move = 0
        self._genes = []

    def get_is_alive(self):
        return self._is_alive

    def _check_is_alive(self):
        walls = self._walls
        # on elève 10 en x car le point spawn aux coords 10 10
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



