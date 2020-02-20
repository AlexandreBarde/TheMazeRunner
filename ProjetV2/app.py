import sys
import threading

from Menu import WindowMaze
from Map import Map
sys.setrecursionlimit(99999999)
threading.stack_size(200000000)

map1 = Map()
map1._load_map("map_test")
data = map1._get_data_map()

# Création de la fenêtre
menu = WindowMaze(data)

# canvas = tk.Canvas(master=None,width=500,height=500)
#    canvas.pack()
#    t = turtle.RawTurtle(canvas)
#    canvas.create_rectangle(500, 500, 0, 0, fill="black")
#    t.forward(50)