from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)   

calculate_button = Button(text="Calculate", command=lambda: kilometer_result_label.config(text=int(miles_input.get()) * 1.60934))
calculate_button.grid(column=1, row=2)



window.mainloop()