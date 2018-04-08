from Tkinter import *
import ttk 
from tkColorChooser import askcolor



class Paint(object):

    DEFAULT_COLOR = 'Blue'

    def __init__(self):
        #SETUP#
        self.root = Tk()
        self.root.title("Control Brazo")
        #LABELS#
        self.titulo = Label(self.root, text='Control de Brazo para Dibujar',font='Helvetica 18 bold')
        self.titulo.grid(row=0, column=1)
        self.grosor = Label(self.root, text='Grosor de Pincel:',justify=RIGHT)
        self.grosor.grid(row=1, column=1)
        #BOTNOES#
        self.b_color = Button(self.root, text='COLOR', command=self.cambiar_color, height = 1, width = 10)
        self.b_color.grid(row=1, column=0)
        self.ayuda = Button(self.root, text='AYUDA',bg='red', command=self.cambiar_color, height = 1, width = 10)
        self.ayuda.grid(row=3, column=3)
        #SLIDERS#
        self.s_x = Scale(self.root, from_=0, to=255, orient=HORIZONTAL, width=30)
        self.s_x.grid(row=3, column=2)
        self.s_x = Scale(self.root, from_=0, to=255, orient=HORIZONTAL, width=30)
        self.s_x.grid(row=3, column=1)
        #COMBO#
        self.c_s_pincel = ttk.Combobox(self.root, width=10,height=2)
        self.c_s_pincel["values"] = [1,2,3,4,5,6,7,8,9,10]
        self.c_s_pincel.current(4)
        self.c_s_pincel.grid(row=1, column=2)
        #CANVAS#
        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=2, columnspan=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.color = "Blue"
        self.eraser_on = False
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def cambiar_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]


    def paint(self, event):
        self.line_width = self.c_s_pincel.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y
        global x,y
        x = event.x
        y = event.y
        print(x,y)
    def reset(self, event):
        self.old_x, self.old_y = None, None

#class Ayuda():


if __name__ == '__main__':
    ge = Paint()
    
