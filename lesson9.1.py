from tkinter import *
import math
import time
import random

class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title('Часы')

        self.canvas = Canvas(root, width=400, height=400, bg='#fff')
        self.canvas.pack()


        self.radius = 190
        self.center_x = 200
        self.center_y = 200


        self.update_clock()

    def draw_line(self, angle, length, width, color):
        x = self.center_x + length * math.sin(math.radians(angle))
        y = self.center_y - length * math.cos(math.radians(angle))
        self.canvas.create_line(self.center_x, self.center_y, x, y, width=width, fill=color)


    def update_clock(self):
        self.canvas.delete('all')
        self.canvas.create_oval(self.center_x - self.radius, self.center_y - self.radius,self.center_x + self.radius, self.center_y + self.radius,fill='black')
        current_time = time.localtime()
        self.canvas.create_text(self.radius + 10, 30, text='12', fill='#fff', font=('Verdana', 18))
        self.canvas.create_text(self.radius + 10, 100, text='Мои первые часы', fill='#f00', font=('Verdana', 18))  # 12
        self.canvas.create_text(self.radius + 10, 360, text='6', fill='#fff', font=('Verdana', 18))  # 6
        self.canvas.create_text(30, self.radius + 10, text='9', fill='#fff', font=('Verdana', 18))  # 9
        self.canvas.create_text(370, self.radius + 10, text='3', fill='#fff', font=('Verdana', 18))  # 3
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec
        print(hours)
        second_angle = 6 * seconds
        minute_angle = 6 * minutes + seconds / 10
        hour_angle = 30 * hours + minutes / 2
        color_random = ['red','green','blue','orange','yellow','indigo','violet','gray','white','lime']
        for i in color_random:
            lencolor = len(color_random) -1
            colorrandom = color_random[random.randint(0,lencolor )]
            colorrandom2 = color_random[random.randint(0, lencolor)]
            colorrandom1 = color_random[random.randint(0, lencolor)]

        self.draw_line(second_angle, self.radius - 20, 1, colorrandom2)
        self.draw_line(minute_angle, self.radius - 40, 3, colorrandom1)
        self.draw_line(hour_angle, self.radius - 60, 5, colorrandom)


        self.root.after(1000, self.update_clock)



root = Tk()
clock = Clock(root)
root.mainloop()
