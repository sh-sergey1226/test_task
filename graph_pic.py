from tkinter import *
from maze_templates import *

root = Tk()
pics = Canvas(root, width=500, height=500, bg='white')
pics.pack()

def create_pict(maze, position):
    for i in maze:
        x, y = i[0], i[1]
        x1 = 100+50*x
        y1 = 350-50*y
        x2 = x1+50
        y2 = y1-50
        pics.create_rectangle(x1, y1, x2, y2,
                           fill='gray',
                           outline='black',
                           width=2,
                           activedash=(5, 4))

    x, y = zero_point_b[0],zero_point_b[1]
    x1 = 100 + 50 * x
    y1 = 350 - 50 * y
    x2 = x1 + 50
    y2 = y1 - 50
    pics.create_rectangle(x1, y1, x2, y2,
                       fill='blue',
                       outline='black',
                       width=2,
                       activedash=(5, 4))

    x, y = finish_b[0],finish_b[1]
    x1 = 100 + 50 * x
    y1 = 350 - 50 * y
    x2 = x1 + 50
    y2 = y1 - 50
    pics.create_rectangle(x1, y1, x2, y2,
                       fill='green',
                       outline='black',
                       width=2,
                       activedash=(5, 4))

    label = Label(text=f"Your position {position}")
    label.pack()
    root.mainloop()


if __name__ == '__main__':
    maze = a
    position = 'default'
    create_pict(maze, position)