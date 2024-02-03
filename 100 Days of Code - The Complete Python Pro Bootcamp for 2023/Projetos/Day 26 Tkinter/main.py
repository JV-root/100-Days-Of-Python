from tkinter import *


window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)



# Label
my_label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))

# Pack

my_label['text'] = "New Text"  
my_label.config(text="New Text")

my_label.pack()


# Entry

input = tk.Entry(width=10)

input.pack()


#Button
buttojn = tk.Button(text="Click Me")


window.mainloop()