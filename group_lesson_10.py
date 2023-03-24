import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import math

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of a Circle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def populate_main_window(frm_main):

    # A label that displays "Enter the radisu of a circle (1-100): "
    lbl_radius = Label(frm_main, text = "Enter the radius of a circle (1-100): ")

    # An integer box where the user inputs the radius of a circle in centimeters.
    ent_radius = IntEntry(frm_main, width = 4, lower_bound=1, upper_bound=100)

    # A label after the text box that displays what units will be used.
    lbl_radius_units = Label(frm_main, text = "cm")

    # A label showing what the area of the circle is.
    lbl_area = Label(frm_main, text = "The area of the circle is: ")

    txt_area = Label(frm_main, width = 5, anchor ="e")

    #Create the clear button
    btn_clear = Button(frm_main, text = "Clear")

    # Layout of all the labels, entry boxes, and buttons in a grid
    lbl_radius.grid(      row=0, column=0, padx=3, pady=3)
    ent_radius.grid(      row=0, column=1, padx=3, pady=3)
    lbl_radius_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_area.grid(        row=1, column=0, padx=3, pady=3)
    txt_area.grid(        row=1, column=2, padx=3, pady=3, sticky = "w")

    btn_clear.grid(       row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")

    def calculate(event):

        try:
            #User input
            r = ent_radius.get()
            a = (math.pi * r **2)

            #compute area of a circle
            txt_area.config(text = f"{a:.2f}")

        except ValueError:
            txt_area.config(text = "")
    
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_radius.clear()
        ent_radius.config(text="")
        ent_radius.focus()
        
    ent_radius.bind("KeyRelease", calculate)
    
    #Computer calls the clear function once the user presses the clear button
    btn_clear.config(command=clear)

    ent_radius.focus()

if __name__ == "__main__":
    main()