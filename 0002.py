import tkinter as tk

# Create a function to display the phrases
def display_phrases():
    phrases_window = tk.Toplevel(root)
    phrases_window.title("Spell Phrases")

    # Set the size of the second window (width x height)
    phrases_window.geometry("600x400")

    # Create a label for each phrase with circles, lines in between, and spaces after sentences
    circle_symbol = "\u25CF"  # Unicode for a larger circle (●)
    line_symbol = "─"  # Line symbol
    for i, phrase in enumerate(knots, start=1):
        circles_and_lines = f"{line_symbol.join(circle_symbol * i)}"
        if i < 10:
            # Calculate the number of spaces based on the difference between knot number and 10
            spaces = ' ' * (10 - i)
            # Left-align the sentence and add spaces after it
            sentence = f"{phrase} {spaces}"
        else:
            sentence = phrase
        label_text = f"By knot of {i}, {sentence}{circles_and_lines}"
        label = tk.Label(phrases_window, text=label_text)
        label.pack()

# Create the main application window
root = tk.Tk()
root.title("Spell Phrases Viewer")

# Create a button to display the phrases
show_phrases_button = tk.Button(root, text="Show Spell Phrases", command=display_phrases)
show_phrases_button.pack()

# Set the initial window size to be larger (width x height)
root.geometry("400x200")

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

# Start the main application loop
root.mainloop()
