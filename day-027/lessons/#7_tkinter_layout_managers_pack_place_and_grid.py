import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 14, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

#Button

def button_clicked():
    print("I got clicked")
    new_text = text_input.get()
    my_label.config(text=new_text)

    
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)

new_button = tkinter.Button(text="Click Me", command=button_clicked)
new_button.grid(column=3, row=0)

#Entry

text_input = tkinter.Entry(width=10)
text_input.grid(column=4, row=3)
print(text_input.get())
 
 
 
window.mainloop()