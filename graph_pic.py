from tkinter import Tk, Canvas, Frame, BOTH

# labyrinth2 = ((0, 3), (1, 3), (2, 3), (3, 3),
#               (0, 2), (f, f), (f, f), (3, 2),
#               (0, 1), (f, f), (f, f), (3, 1),
#               (0, 0), (1, 0), (f, f), (3, 0))

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Цвета")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle(
            10, 10, 50, 50,
            outline="#fb0", width=5, fill="#05f" #yellow
        )

        canvas.create_rectangle(
            100, 100, 150, 150,
            outline="#fb0", width=5, fill="#05f" #yellow
        )

        canvas.create_rectangle(
            200, 200, 250, 250,
            outline="#fb0", width=5, fill="#05f" #yellow
        )
        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example()
    root.geometry("1000x600+300+300")
    root.mainloop()



if __name__ == '__main__':
    main()