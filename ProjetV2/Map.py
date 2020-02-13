class Map(object):

    def __init__(self):
        return

    def _load_map(self, filename):
        file_object = open("maps/" + filename + ".txt", "r")
        #print(file_object.readlines())
        #self._generate_map(file_object.readlines())
        self._data_map = file_object.readlines()

    def _get_data_map(self):
        return self._data_map


