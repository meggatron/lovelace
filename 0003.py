import tkinter as tk

# Create a function to display the phrases
def display_phrases():
    phrases_window = tk.Tk()
    phrases_window.title("Spell Phrases")

    # Set the size of the second window (width x height)
    #phrases_window.geometry("600x400")

    # Create a frame to center content
    frame = tk.Frame(phrases_window)
    frame.pack(fill="both", expand=True)
    
    # Create a label for each phrase with circles, lines in between, and spaces after sentences
    #circle_symbol = "\u25CF"  # Unicode for a larger circle (●)
    #line_symbol = "─"  # Line symbol
    for i, phrase in enumerate(knots, start=1):
        #circles_and_lines = f"{line_symbol.join(circle_symbol * i)}"
        if i < 10:
            # Calculate the number of spaces based on the difference between knot number and 10
            spaces = ' ' * (10 - i)
            # Left-align the sentence and add spaces after it
            sentence = f"{phrase} {spaces}"
        else:
            sentence = phrase
        
        # Create a Label for each phrase and center it both horizontally and vertically
        label = tk.Label(frame, text=f"By knot of {i}, {sentence}", anchor="center")
        #label = tk.Label(frame, text=f"By knot of {i}, {sentence}{circles_and_lines}", anchor="center")
        label.pack(fill="both", expand=True)

    # Start the main application loop for the second window
    phrases_window.mainloop()

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

# Call the display_phrases function to open the second window
display_phrases()
