# -*- coding: utf-8 -*-

import Tkinter as tk
import tkMessageBox

window = tk.Tk()
window.title('triangle')
window.geometry('500x300')


l1 = tk.Label(window, text='first edge:',font=('Arial', 12),width=20, height=2)
t1 = tk.Entry(window,show = None)
l2 = tk.Label(window, text='second edge:',font=('Arial', 12),width=20, height=2)
t2 = tk.Entry(window,show = None)
l3 = tk.Label(window, text='third edge:',font=('Arial', 12),width=20, height=2)
t3 = tk.Entry(window,show = None)

l1.place(x=10,y=10)
t1.place(x=300,y=10)
l2.place(x=10,y=90)
t2.place(x=300,y=90)
l3.place(x=10,y=170)
t3.place(x=300,y=170)

def finish():
   notEmpty=t1.get() and t2.get() and t3.get()
   if not notEmpty:
       tkMessageBox.showerror(title='Error', message='Please input three edges!')
   else:
       edge1=int(t1.get())
       edge2=int(t2.get())
       edge3=int(t3.get())
   if edge1+edge2>edge3 and edge1+edge3>edge2 and edge2+edge3>edge1:
       #√[s(s-a)(s-b)(s-c)
       perimeter=edge1+edge2+edge3
       s=perimeter/2
       area=(s*(s-edge1)*(s-edge2)*(s-edge3)) ** 0.5
       tkMessageBox.showinfo(title='triangle', message='This is a triangle!\n\nArea is '+str(area)+'\n\nPerimeter is ' + str(perimeter))
   else:
       tkMessageBox.showwarning(title='Warning', message='This is not a triangle!')


b = tk.Button(window, text='finish',width=15, height=2, command=finish)
b.place(x=190,y=230)


window.mainloop()

        
    
        
