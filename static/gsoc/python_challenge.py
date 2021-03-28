from tkinter import *
import json

rectangles = []
grid = []
begin_id =0

root = Tk()
root.title("Conway's Game of Life")
frame = Frame(root, width=630, height=630)
canvas = Canvas(frame, width=630, height=630)
frame.pack()
canvas.pack(side = RIGHT)

class Cell:
    def __init__(self, x, y, i, j):
        self.isAlive = False
        self.nextStatus = None
        self.pos_screen = (x, y)
        self.pos_matrix = (i, j)

    def _str_(self):
        return str(self.isAlive)

    def _repr_(self):
        return str(self.isAlive)

    def switchStatus(self):
        self.isAlive = not self.isAlive


def create_grid(x,y):
    global grid                              
    global rectangles                           
    for i in range(40):
        grid.append([])
        rectangles.append([])
        for j in range(45):
            rect = canvas.create_rectangle(x, y, x+15, y+15, fill="white")
            rectangles[i].append(rect)
            grid[i].append(Cell(x, y, i, j))
            x += 15
        x = 15
        y += 15


def input_data(val):
    for i in range(len(data[val])):
        for j in range(len(data[val][0])):
            if data[val][i][j]==1:
                grid[i+3][j+4].switchStatus()
                canvas.itemconfig(rectangles[i+3][j+4], fill="red")
            
def paint_grid():
    for i in grid:
        for j in i:
            if j.nextStatus != j.isAlive:
                x, y = j.pos_matrix
                print(x, y)
                if j.nextStatus :
                    canvas.itemconfig(rectangles[x][y], fill="green")
                    print("changed", j.pos_matrix, "from dead to alive")
                else:
                    canvas.itemconfig(rectangles[x][y], fill="white")
                    print("changed", j.pos_matrix, "from alive to dead")
                j.switchStatus()
                print("Current status of", j.pos_matrix, j.isAlive)


def life_rules(cell):
    num_alive = 0
    x, y = cell.pos_matrix
    for i in (x-1, x, x+1):
        for j in (y-1, y, y+1):
            if i == x and j == y:
                continue
            if i == -1 or j == -1:
                continue
            try:
                if grid[i][j].isAlive:
                    num_alive += 1
            except IndexError:
                pass
    if cell.isAlive:
        return not( num_alive == 2 or num_alive == 3 )
    else:
        return num_alive == 3


def begin_game():
    for i in grid:
        for j in i:
            if life_rules(j):
                j.nextStatus = not j.isAlive
                print("change in", j.pos_matrix, "from", j.isAlive, "to", j.nextStatus)

            else:
                j.nextStatus = j.isAlive
    paint_grid()
    global begin_id
    begin_id = root.after(150, begin_game)


def pause_game():
    root.after_cancel(begin_id)

def clear():
    pause_game()
    for i in range(len(grid)):
        for j in range(len(grid[0])):    
            if grid[i][j].isAlive :
               grid[i][j].switchStatus
               canvas.itemconfig(rectangles[i][j], fill="white")
    

create_grid(15,15)
with open("config.json") as f:      # file path goes here
            data=json.load(f)
            f.close 
start0 = Button(root, text="Glider!", command=lambda : input_data("glider"))
start0.pack(side = LEFT)
start1 = Button(root, text="hwss!", command=lambda : input_data("hwss"))
start1.pack(side = LEFT)
start2 = Button(root, text="TOAD!", command=lambda : input_data("toad"))
start2.pack(side = LEFT)
start3 = Button(root, text="BEACON", command=lambda : input_data("beacon"))
start3.pack(side = LEFT)
start4 = Button(root, text="start!", command= lambda : begin_game())
start4.pack(side = LEFT)
start5 = Button(root, text="pause!", command=lambda : pause_game())
start5.pack(side = LEFT)
start6 = Button(root, text="Clear!", command=lambda : clear())
start6.pack(side = LEFT)
stop = Button(root, text="exit!", command = exit)
stop.pack(side = LEFT)
root.mainloop()