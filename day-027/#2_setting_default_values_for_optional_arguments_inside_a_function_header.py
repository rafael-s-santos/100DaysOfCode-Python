import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.pack(side="left")
my_label.pack(expand=True)


import turtle

tim = turtle.Turtle()
tim.write("Some Text", font=("Times New Roman", 30, "bold"))


window.mainloop()