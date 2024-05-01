#This line imports the "tkinter" library in Python and aliases it as "tk" for convenience, providing a toolkit for creating graphical user interfaces.
import tkinter as tk

# Create the main window
root = tk.Tk()


# Add a label to the main window
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)  # Add some vertical padding to the label

# Start the main event loop
root.mainloop()


#ASSIGNMENT

#1. using .geometry, make the main window 400 x 600 
#2. change the location of the label in the main window

