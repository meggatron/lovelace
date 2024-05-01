import tkinter as tk

# Create a function to display the phrases
def display_phrases():
    phrases_window = tk.Tk()
    phrases_window.title("Spell Phrases")

   # List of phrases corresponding to the original spell
    knots = [
    "The spell's begun.",
    "It comes true.",
    "So mote it be.",
    "This power I store.",
    "The spell's alive.",
    "This spell I fix.",
    "Events I'll leaven.",
    "It will be fate.",
    "What's done is mine."
    ]
 

    # Create a label for each phrase
    for i, phrase in enumerate(knots, start=1):
        label = tk.Label(phrases_window, text=f"By knot of {i}, {phrase}")
        label.pack()



# Call the display_phrases function directly
display_phrases()

# Start the main application loop
tk.mainloop()

