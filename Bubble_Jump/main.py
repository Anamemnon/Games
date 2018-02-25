import tkinter
import random
import time
# page 215
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color, outline=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id, 200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
class Count:
    def __init__(self, canvas):
        self.canvas = canvas
        self.count = 0
        self.id = canvas.create_text(460,5,text = f'Очки: {self.count}')
    
    def increase_count(self, ball):
        pos = self.canvas.coords(ball.id)
        if ball.hit_paddle(pos) == True:
            self.count += 1
            self.canvas.itemconfig(self.id, text=f'Очки: {self.count}')

root = tkinter.Tk()
root.title('Game')
root.resizable(0, 0) #фиксированный размер окна по x и y
root.wm_attributes("-topmost", 1) #разместим это окно поверх всех других окон
canvas = tkinter.Canvas(root, width=500, height=400, bd=0, highlightthickness=0)

canvas.pack()

root.update()


paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
count = Count(canvas)

while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        count.increase_count(ball)      
    root.update_idletasks()
    root.update()
    time.sleep(0.01)