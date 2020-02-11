from tkinter import Tk

from Tk import tkinter
import turtle

def main():
    window = Tk()
    window.wm_title("The Maze Runner")
    window.maxsize(width=400, height=400)
    window.minsize(width=400, height=400)
    window.iconbitmap('')
    data = data
    canvas = Canvas(self._window)
    canvas.config(width=400, height=400)
    self._canvas = self._generate_square(canvas)
    canvas.pack()




    canvas = tkinter.Canvas(master=None,width=500,height=500)
    canvas.pack()
    t = turtle.RawTurtle(canvas)
    canvas.create_rectangle(500, 500, 0, 0, fill="black")
    t.forward(50)
    turtle.done()

main()