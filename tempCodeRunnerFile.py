from tkinter import *
beginning=Tk()
beginning.title('TUGAS KELOMPOK PRAKTIKUM ALGORITMA DAN Pemrograman I')
canvas=Canvas(beginning,bg='green', bd=6)
canvas.pack(fill=BOTH, expand=TRUE)
words="Welcome to the garden, we hope you enjoy your stay!"
text=canvas.create_text(0,-4000, text=words, font=('Times New Roman',40,'bold'), fill='white')
x1,y1,x2,y2 = canvas.bbox(text)
width = x2-x1
height = y2-y1
canvas['width']= width
canvas['height']=height
motion=85
def shift():
    x1,y1,x2,y2 = canvas.bbox(text)
    if(y1<0 or x2<0): 
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords(text,x1,y1)
    else:
        canvas.move(text, -17, 0)
    canvas.after(10000//motion, shift)
shift()
beginning.mainloop()
