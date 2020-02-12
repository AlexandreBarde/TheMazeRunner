from operator import methodcaller, attrgetter
from threading import Timer
from tkinter import Tk, Canvas, Button
import time
import random

from Projet.indi import Runner


class WindowMaze(object):

    def __init__(self, data):
        self._window = Tk()
        self._window.wm_title("The Maze Runner")
        self._window.maxsize(width=450, height=450)
        self._window.minsize(width=450, height=450)
        self._window.iconbitmap('')
        self._data = data
        self._walls = []
        self._runners = []
        self._pop = []
        self._pop_save = []
        self._end = []
        self._num_generation = 0
        self._iteration = 0
        print(data)

        def gestion():

            self._window.update()
            time.sleep(0.2)
            callback()

        def callback():
            individu_mort_pop = []
            individu_mort_runners = []
            print("Nombre d'individus dans la population actuellement : " + str(len(self._pop)))
            if len(self._pop) == 0:
                self._num_generation = self._num_generation + 1
                print("Tous les individus sont morts, calcul de la fitness : ")
                array_sorted = []
                for i in range(len(self._pop_save)):
                    print("Individu n°" + str(i) + " : " + str(self._pop_save[i].get_nbr_moves()))
                    print("Positions du l'individu n°" + str(i) + str(self._pop_save[i].get_directions()))
                    array_sorted = sorted(self._pop_save, key=attrgetter('_nbr_move'), reverse=True)
                print("Liste triée : ")
                for j in range(len(array_sorted)):
                    print("Individu n°" + str(j) + " - Nombre déplacements : " + str(array_sorted[j].get_nbr_moves()) + " : " + str(array_sorted[j].get_directions()))
                new_pop = array_sorted[:round(len(array_sorted) / 2)]
                print("Nouvelle population")
                self._runners = new_pop
                # on a une liste de la moitié de la taille de la population (dans ce cas 25)
                # cette liste contient des individus qui ont avancés de qqls cases (les premiers de la liste qui est trié par nombre de déplacements)

                # il faut donc alors compléter cette liste avec des nouveaux individus (la moitié de la liste donc)
                for i in range(len(self._runners) - 1, self._nbr_pop - 1):
                    self._runners.append(Runner(90, 50, 110, 70, self._walls))

                # reset des tableaux qui contiennent les individus morts au combat #RIP
                individu_mort_pop.clear()
                individu_mort_runners.clear()

                # reset de l'itération
                self._iteration = 0

                print("[] Nouvelle génération ...")
                print("Taille de _pop : " + str(len(self._pop)))
                print("Taille de runners : " + str(len(self._runners)))
                print("Taille de pop_save : " + str(len(self._pop_save)))
                self._generate_square(canvas)
                self._create_()
            else:
                if self._num_generation == 0:
                    for i in range(len(self._pop)):
                        print("Item n°" + str(i))
                        print(self._pop[i])
                        nbr = random.randint(0, 3)
                        if nbr == 0:  # à droite
                            self._canvas.move(self._pop[i], 40, 0)
                            self._runners[i].new_pos(self._canvas.coords(self._pop[i]), 0)
                            if not (self._runners[i]).get_is_alive():
                                individu_mort_pop.append(self._pop[i])
                                individu_mort_runners.append(self._runners[i])
                                # Si on supprime les individus lorsque la boucle tourne on a un out of index => logique
                                # self._pop.remove(self._pop[i])
                                # self._runners.remove(self._runners[i])

                                # print(self._canvas.coords(self._balle))
                        elif nbr == 1:  # en bas
                            self._canvas.move(self._pop[i], 0, -40)
                            self._runners[i].new_pos(self._canvas.coords(self._pop[i]), 1)
                            if not (self._runners[i]).get_is_alive():
                                individu_mort_pop.append(self._pop[i])
                                individu_mort_runners.append(self._runners[i])
                            # print(self._canvas.coords(self._balle))
                        elif nbr == 2:  # à gauche
                            self._canvas.move(self._pop[i], -40, 0)
                            self._runners[i].new_pos(self._canvas.coords(self._pop[i]), 2)
                            if not (self._runners[i]).get_is_alive():
                                individu_mort_pop.append(self._pop[i])
                                individu_mort_runners.append(self._runners[i])
                            # print(self._canvas.coords(self._balle))
                        elif nbr == 3:  # en haut
                            self._canvas.move(self._pop[i], 0, 40)
                            self._runners[i].new_pos(self._canvas.coords(self._pop[i]), 3)
                            if not (self._runners[i]).get_is_alive():
                                individu_mort_pop.append(self._pop[i])
                                individu_mort_runners.append(self._runners[i])
                            # print(self._canvas.coords(self._balle))

                    # Traitements des individus morts
                    for i in range(len(individu_mort_pop)):
                        self._pop.remove(individu_mort_pop[i])

                    for i in range(len(individu_mort_runners)):
                        self._runners.remove(individu_mort_runners[i])
                else:
                    print("Nouvelle génération")
                    self._iteration = self._iteration + 1 # nouvelle itération dans la génération
                    print("Itération n° " + str(self._iteration))
                    for i in range(len(self._pop)):
                        print("Item n°" + str(i))
                        print(self._pop[i])
                        # on vérifie sur le runner possède un gène
                        # si le nombre de directions est plus grande que le nombre d'itérations (pcq on stocke les gènes à chaque itérations)
                        if len(self._runners[i].get_directions()) > self._iteration:
                            nbr = self._runners[i].get_directions()[self._iteration]
                            if nbr == 0:  # à droite
                                self._canvas.move(self._pop[i], 40, 0)
                                if not (self._runners[i]).get_is_alive():
                                    individu_mort_pop.append(self._pop[i])
                                    individu_mort_runners.append(self._runners[i])
                            elif nbr == 1:  # en bas
                                self._canvas.move(self._pop[i], 0, -40)
                                if not (self._runners[i]).get_is_alive():
                                    individu_mort_pop.append(self._pop[i])
                                    individu_mort_runners.append(self._runners[i])
                            elif nbr == 2:  # à gauche
                                self._canvas.move(self._pop[i], -40, 0)
                                if not (self._runners[i]).get_is_alive():
                                    individu_mort_pop.append(self._pop[i])
                                    individu_mort_runners.append(self._runners[i])
                            elif nbr == 3:  # en haut
                                self._canvas.move(self._pop[i], 0, 40)
                                if not (self._runners[i]).get_is_alive():
                                    individu_mort_pop.append(self._pop[i])
                                    individu_mort_runners.append(self._runners[i])
                        else:
                            nbr = random.randint(0, 3)
                            if nbr == 0:  # à droite
                                self._canvas.move(self._pop[i], 40, 0)
                                self._runners[i].new_pos(self._canvas.coords(self._pop[i]), 0)
                                if not (self._runners[i]).get_is_alive():
                                    individu_mort_pop.append(self._pop[i])
                                    individu_mort_runners.append(self._runners[i])
                            elif nbr == 1:  # en bas
                                self._canvas.move(self._pop[i], 0, -40)
                                self._runners[i].new_pos(self._canvas.coords(self._pop[i]), 1)
                                if not (self._runners[i]).get_is_alive():
                                    individu_mort_pop.append(self._pop[i])
                                    individu_mort_runners.append(self._runners[i])
                            elif nbr == 2:  # à gauche
                                self._canvas.move(self._pop[i], -40, 0)
                                self._runners[i].new_pos(self._canvas.coords(self._pop[i]), 2)
                                if not (self._runners[i]).get_is_alive():
                                    individu_mort_pop.append(self._pop[i])
                                    individu_mort_runners.append(self._runners[i])
                            elif nbr == 3:  # en haut
                                self._canvas.move(self._pop[i], 0, 40)
                                self._runners[i].new_pos(self._canvas.coords(self._pop[i]), 3)
                                if not (self._runners[i]).get_is_alive():
                                    individu_mort_pop.append(self._pop[i])
                                    individu_mort_runners.append(self._runners[i])

                    print("gestion des morts :")
                    print("individu_mort_pop")
                    print(individu_mort_pop)
                    print("individu_mort_runners")
                    print(individu_mort_runners)

                    for i in range(len(individu_mort_pop)):
                        self._pop.remove(individu_mort_pop[i])

                    for i in range(len(individu_mort_runners)):
                        self._runners.remove(individu_mort_runners[i])



            gestion()

        canvas = Canvas(self._window)
        canvas.config(width=400, height=400)
        b = Button(self._window, text="Play", command=gestion)
        b.pack()
        self._canvas = canvas
        self._generate_square(canvas)
        self._nbr_pop = 50  # nombre d'individu dans une population
        self._create_()

    def _generate_square(self, canvas):
        chars = self._data
        for i in range(len(chars)):
            chars[i] = chars[i].replace("\n", "")
            print(chars[i])
            line_tmp = list(chars[i])
            for j in range(len(line_tmp)):
                x_start = 40 * j
                y_start = 40 * i
                x_end = (40 * j) + 40
                y_end = (40 * i) + 40
                if line_tmp[j] == "1":  # duplication de code à virer (pos)
                    self._walls.append(str(x_start) + ":" + str(y_start) + " " + str(x_end) + ":" + str(y_end))
                    # print("pos : " + str(i) + ":" + str(j) + " => x_start : " + str(x_start) + " x_end : " + str(
                    # x_end) + " y_start : " + str(y_start) + " y_end : " + str(y_end))
                    canvas.create_rectangle(x_start, y_start, x_end, y_end, outline="#474747", fill="#66545e")
                elif line_tmp[j] == "0":
                    canvas.create_rectangle(x_start, y_start, x_end, y_end, outline="#474747", fill="#a39193")
                elif line_tmp[j] == "2":
                    canvas.create_rectangle(x_start, y_start, x_end, y_end, outline="#474747", fill="#eea990")
                elif line_tmp[j] == "3":
                    canvas.create_rectangle(x_start, y_start, x_end, y_end, outline="#474747", fill="#f6e0b5")
                    self._end = [x_start, y_start, x_end, y_end]

        self._canvas = canvas
        canvas.pack()
        print(self._walls)

    def _generate_app(self):
        self._window.mainloop()

    def _create_(self):
        for i in range(self._nbr_pop):
            self._pop.append(self._canvas.create_oval(90, 50, 110, 70, outline="#474747", fill=self._get_random_color()))
            if not len(self._runners) == self._nbr_pop:
                runner = Runner(90, 50, 110, 70, self._walls)
                self._runners.append(runner)
                self._pop_save.append(runner)
            # self._move_(balle)

        print("Taille de la population : " + str(len(self._pop)))
        self._generate_app()

    def _get_random_color(self):
        colors = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
                  'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
                  'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
                  'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
                  'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue',
                  'dark slate blue',
                  'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue', 'blue',
                  'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
                  'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
                  'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green',
                  'dark olive green',
                  'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
                  'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
                  'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
                  'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
                  'indian red', 'saddle brown', 'sandy brown',
                  'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
                  'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
                  'pale violet red', 'maroon', 'medium violet red', 'violet red',
                  'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
                  'thistle', 'snow2', 'snow3',
                  'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
                  'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
                  'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
                  'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
                  'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
                  'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
                  'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
                  'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
                  'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
                  'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
                  'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
                  'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
                  'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
                  'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
                  'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
                  'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
                  'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
                  'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
                  'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
                  'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
                  'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
                  'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
                  'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
                  'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
                  'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
                  'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
                  'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
                  'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
                  'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
                  'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
                  'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
                  'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
                  'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
                  'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
                  'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
                  'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
                  'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
                  'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
                  'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
                  'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
                  'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
                  'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
                  'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
                  'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
                  'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
                  'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
                  'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
                  'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
                  'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
                  'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
                  'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
                  'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
                  'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
                  'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
                  'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
                  'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
                  'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
        print("nombre couleurs : " + str(len(colors)))
        random_num = random.randint(0, len(colors) - 1)
        print("random : " + str(random_num))
        color_return = colors[random_num]
        print("Couleur : " + color_return)
        colors.remove(colors[random_num])
        return color_return
