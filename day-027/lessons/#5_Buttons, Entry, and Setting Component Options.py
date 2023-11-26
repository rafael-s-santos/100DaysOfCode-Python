import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button

def button_clicked():
    print("I got clicked")
    new_text = text_input.get()
    my_label.config(text=new_text)

    
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

#Entry

text_input = tkinter.Entry(width=10)
text_input.pack()
print(text_input.get())










window.mainloop()