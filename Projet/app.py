from Menu import WindowMaze
from Map import Map

map1 = Map()
map1._load_map("map_test")
data = map1._get_data_map()

menu = WindowMaze(data)

