#Alternate of temp.py in spyder directory, using tkinter
import tkinter as tkin

root = tkin.Tk()
canvas = tkin.Canvas(root, width = 900, height = 900, background = "#AAA")
canvas.pack()
img = tkin.PhotoImage(file="DragonFromInternet.png")
canvas.create_image(0,0, anchor=tkin.NW, image=img)
tkin.mainloop()