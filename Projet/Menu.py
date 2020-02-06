from tkinter import Tk, Canvas


class WindowMaze(object):

    def __init__(self, data):
        self._window = Tk()
        self._window.wm_title("The Maze Runner")
        self._window.maxsize(width=400, height=400)
        self._window.minsize(width=400, height=400)
        self._window.iconbitmap('')
        self._data = data
        canvas = Canvas(self._window)
        canvas.config(width=400, height=400)
        self._generate_square(canvas)

        self._generate_app()

    def _generate_square(self, canvas):
        chars = self._data
        for i in range(len(chars)):
            chars[i] = chars[i].replace("\n", "")
            print(chars[i])
            line_tmp = list(chars[i])
            for j in range(len(line_tmp)):
                if line_tmp[j] == "1":
                    x_start = 40 * j
                    y_start = 40 * i
                    x_end = (40 * j) + 40
                    y_end = (40 * i) + 40
                    print("pos : " + str(i) + ":" + str(j) + " => x_start : " + str(x_start) + " x_end : " + str(x_end) + " y_start : " + str(y_start) + " y_end : " + str(y_end))
                    canvas.create_rectangle(x_start, y_start, x_end, y_end, outline="#fb0", fill="#474747")
                else:
                    x_start = 40 * j
                    y_start = 40 * i
                    x_end = (40 * j) + 40
                    y_end = (40 * i) + 40
                    canvas.create_rectangle(x_start, y_start, x_end, y_end, outline="#fb0", fill="#FA24A9")
        canvas.pack()

    def _generate_app(self):
        self._window.mainloop()
