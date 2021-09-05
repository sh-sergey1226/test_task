from tkinter import Tk, Canvas, Frame, BOTH

from maze_templates import *

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Цвета")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        for i in c:

            x, y = i[0], i[1]
            x1 = 100+50*x
            y1 = 350-50*y
            x2 = x1+50
            y2 = y1-50
            canvas.create_rectangle(
                x1, y1, x2, y2,
                outline="#fb0", width=1, fill="#05f" #yellow
            )
            canvas.pack(fill=BOTH, expand=1)




def main():
    root = Tk()
    ex = Example()
    root.geometry("500x500+300+300")
    root.mainloop()

if __name__ == '__main__':
    main()