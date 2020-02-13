from Menu import WindowMaze
from Map import Map

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