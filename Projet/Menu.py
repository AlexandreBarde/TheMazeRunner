from tkinter import Tk, Canvas, Button
import time
import random
from Projet.indi import Runner


class WindowMaze(object):

    def __init__(self, data):
        self._window = Tk()
        self._window.wm_title("The Maze Runner")
        self._window.maxsize(width=400, height=400)
        self._window.minsize(width=400, height=400)
        self._window.iconbitmap('')
        self._data = data
        self._walls = []
        self._runner = Runner(90, 50, 110, 70, self._walls)
        print(data)

        def callback():
            nbr = random.randint(0, 3)
            if nbr == 0:  # à droite
                self._canvas.move(self._balle, 40, 0)
                self._runner.new_pos(self._canvas.coords(self._balle))
                #print(self._canvas.coords(self._balle))
            elif nbr == 1:  # en bas
                self._canvas.move(self._balle, 0, -40)
                self._runner.new_pos(self._canvas.coords(self._balle))
                #print(self._canvas.coords(self._balle))
            elif nbr == 2:  # à gauche
                self._canvas.move(self._balle, -40, 0)
                self._runner.new_pos(self._canvas.coords(self._balle))
                #print(self._canvas.coords(self._balle))
            elif nbr == 3:  # en haut
                self._canvas.move(self._balle, 0, 40)
                self._runner.new_pos(self._canvas.coords(self._balle))
                #print(self._canvas.coords(self._balle))

        canvas = Canvas(self._window)
        canvas.config(width=400, height=400)
        b = Button(self._window, text="Play", command=callback)
        b.pack()
        self._canvas = canvas
        self._generate_square(canvas)
        self._create_(2)

    def _generate_square(self, canvas):
        chars = self._data
        for i in range(len(chars)):
            chars[i] = chars[i].replace("\n", "")
            print(chars[i])
            line_tmp = list(chars[i])
            for j in range(len(line_tmp)):
                if line_tmp[j] == "1":  # duplication de code à virer (pos)
                    x_start = 40 * j
                    y_start = 40 * i
                    x_end = (40 * j) + 40
                    y_end = (40 * i) + 40
                    self._walls.append(str(x_start) + ":" + str(y_start) + " " + str(x_end) + ":" + str(y_end))
                    #print("pos : " + str(i) + ":" + str(j) + " => x_start : " + str(x_start) + " x_end : " + str(
                        #x_end) + " y_start : " + str(y_start) + " y_end : " + str(y_end))
                    canvas.create_rectangle(x_start, y_start, x_end, y_end, outline="#474747", fill="#66545e")
                elif line_tmp[j] == "0":
                    x_start = 40 * j
                    y_start = 40 * i
                    x_end = (40 * j) + 40
                    y_end = (40 * i) + 40
                    canvas.create_rectangle(x_start, y_start, x_end, y_end, outline="#474747", fill="#a39193")
                elif line_tmp[j] == "2":
                    x_start = 40 * j
                    y_start = 40 * i
                    x_end = (40 * j) + 40
                    y_end = (40 * i) + 40
                    canvas.create_rectangle(x_start, y_start, x_end, y_end, outline="#474747", fill="#eea990")
                elif line_tmp[j] == "3":
                    x_start = 40 * j
                    y_start = 40 * i
                    x_end = (40 * j) + 40
                    y_end = (40 * i) + 40
                    canvas.create_rectangle(x_start, y_start, x_end, y_end, outline="#474747", fill="#f6e0b5")

        self._canvas = canvas
        canvas.pack()
        print(self._walls)

    def _generate_app(self):
        self._window.mainloop()


    def _create_(self, number_individus):
        self._balle = balle = self._canvas.create_oval(90, 50, 110, 70, outline="#474747", fill='#aa6f73')
        # self._move_(balle)
        self._generate_app()
