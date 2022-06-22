#!/usr/bin/env python

import tkinter as tk
from datetime import datetime
from time import sleep
from Timer import Timer

from spinning_wheel_objs import Spinning_Wheel, WheelItem,Exam
#print(Exam.next_exam())


root = tk.Tk()
tim = tk.Toplevel()

width = 900
height = 900
#root.geometry('{}x{}'.format(width, height))
root.title("Bac Pratique")
root.configure(background='grey25')

used_items = []
pie_items = []
def redraw(pie_items):
     
    
    for i in range(Exam.get_num_eleves()):
        if (i+1) not in used_items:
            pie_items.append(WheelItem("Poste "+str(i+1), 1/(Exam.get_num_eleves()-len(used_items))))
redraw(pie_items)
def reset():
    used_items = []
    pie_items = []
    wheel.items.clear()
    for i in range(Exam.get_num_eleves()):
        if (i+1) not in used_items:
            wheel.items.append(WheelItem("Poste "+str(i+1), 1/(Exam.get_num_eleves()-len(used_items))))
    wheel.draw()
    lb.delete(0, "end")



canvas_frame = tk.Frame(root,height=1)
list_frame = tk.Frame(canvas_frame,height=1)
global wheel
wheel = Spinning_Wheel(canvas_frame, 400, pie_items, width=str(width), height=str(height-100))
wheel.pack(padx=0, pady=0, side="left", fill="y", expand=True)
list_frame.pack(padx=0, pady=0, side="right", fill="y", expand=True)
lb = tk.Listbox(list_frame,width =20,  height=15, background="purple2", foreground="white", font=('Times 13'), selectbackground="black")
lb.pack()
canvas_frame.pack(side="top", padx=0, pady=5, fill="both", expand=True)

# frame for user controls
user_controls = tk.Frame(root)
user_controls.configure(background='grey25')
lbl0  = tk.Label( user_controls,height= 1,width=20, text= "Nom élève")
lbl0.pack(side='left')
name_eleve = tk.Text( user_controls,height= 1,width=20)
name_eleve.pack(side='left')

def spinner():
    if name_eleve.get("1.0","end")==chr(10):
        return
    global wheel
    res = wheel.spin()
    nb_poste = int(res[5:])
    print (nb_poste)
    used_items.append(nb_poste)
    
    #print(res)
    lb.insert( "end",res +" : "+ name_eleve.get("1.0","end"))
    
    
    wheel.items.clear()
    for i in range(Exam.get_num_eleves()):
        if (i+1) not in used_items:
            wheel.items.append(WheelItem("Poste "+str(i+1), 1/(Exam.get_num_eleves()-len(used_items))))
    
    sleep(2)
    wheel.draw()
    

def counter_launcher():
    if    Exam.curr_exam()[0] < datetime.now():
            tim = tk.Toplevel()
            cdown  = Timer(tim,  ( 60 * Exam.curr_exam()[1] - (datetime.now() - Exam.curr_exam()[0] ).seconds))
            cdown.pack()
            cdown.focus_force()
            cdown.go_stop()
            





reset_button = tk.Button(user_controls, text="R A Z", command=reset)
reset_button.pack(side='right')
counter_button = tk.Button(user_controls, text="compteur", command=counter_launcher)
counter_button.pack(side='right')
user_controls.pack(side='bottom')
spin_button = tk.Button(user_controls, text="Tourner", command=spinner)
spin_button.pack(side='right')








wheel.draw(offset=0)
tim.mainloop()
root.mainloop()
