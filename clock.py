import tkinter as tk
win = tk.Tk()
win.title("Digital Clock")
canvas = tk.Canvas(win,height=500,width=500, background="white")
canvas.pack()

class Stick:
    def __init__(self,canvas,x,y,dx,dy,color):
        self.id = canvas.create_rectangle(x,y,x+dx,y+dy,fill=color)
        self.canvas = canvas

    def on(self):
        self.canvas.itemconfig(self.id,state="normal")
    def off(self):
        self.canvas.itemconfig(self.id,state="hidden")

class Segment():
    def __init__(self,canvas,x,y,s,b,color):
        self.sticks = []
        self.sticks.append(Stick(canvas,x+s,y,b,s,color)) #TM 0
        self.sticks.append(Stick(canvas,x+s+b,y+s,s,b,color)) #TR 1
        self.sticks.append(Stick(canvas,x+s,y+s+b,b,s,color)) #MM 2
        self.sticks.append(Stick(canvas,x,y+s,s,b,color)) #TL 3
        self.sticks.append(Stick(canvas,x+s+b,y+s+b+s,s,b,color)) #BR 4
        self.sticks.append(Stick(canvas,x+s,y+s+b+s+b,b,s,color)) #BM 5
        self.sticks.append(Stick(canvas,x,y+s+b+s,s,b,color)) #BL 6
        self.canvas = canvas

    def showall(self):
        for s in self.sticks:
            s.on()

    def hideall(self):
        for s in reversed(self.sticks):
            s.off()

    def show(self,number):
        if number == 0:
            self.showall()
            self.sticks[2].off()
        elif number == 1:
            self.hideall()
            self.sticks[1].on()
            self.sticks[4].on()
        elif number == 2:
            self.showall()
            self.sticks[3].off()
            self.sticks[4].off()
        elif number == 3:
            self.showall()
            self.sticks[3].off()
            self.sticks[6].off()
        elif number == 4:
            self.showall()
            self.sticks[0].off()
            self.sticks[6].off()
            self.sticks[5].off()
        elif number == 5:
            self.showall()
            self.sticks[1].off()
            self.sticks[6].off()
        elif number == 6:
            self.showall()
            self.sticks[1].off()
        elif number == 7:
            self.hideall()
            self.sticks[0].on()
            self.sticks[1].on()
            self.sticks[4].on()
        elif number == 8:
            self.showall()
        elif number == 9:
            self.showall()
            self.sticks[5].off()
            self.sticks[6].off()




segment = Segment(canvas,100,100,20,80,"green")
segment.show(5)
#s1 = Stick(canvas,250,250,50,10,"red")
#s2 = Stick(canvas,250,250,10,50,"blue")
#s1.on()
#s2.on()
win.mainloop()