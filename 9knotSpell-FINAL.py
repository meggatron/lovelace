import tkinter as tk

def display_phrases():
    phrases_window = tk.Tk()
    phrases_window.title("9 KNOT SPELL")
    # 1. SET THE SIZE OF THE WINDOW (WIDTH X HEIGHT) USING .GEOMETRY 
    phrases_window.geometry("600x400")

    frame = tk.Frame(phrases_window)
    frame.pack(fill="both", expand=True)
    
    # 2. CREATE VARIABLES FOR STRINGS THAT ARE A CIRCLE AND A LINE
    circle_symbol = "\u25CF"  # Unicode for a larger circle (●) 
    line_symbol = "─"  
    for i, phrase in enumerate(knots, start=1):
         # 3. CREATE A LABEL FOR EACH PHRASE THAT HAS CIRCLES, LINES IN BETWEEN, AND SPACES AFTER SENTENCES //Hint: the indents of the comments are not random
        circles_and_lines = f"{line_symbol.join(circle_symbol * i)}"
        # 4. ADD AN IF STATEMENT FOR i < 10
        if i < 10:
            # 5. CREATE A VARIABLE CALLED spaces THAT CALCULATES THE NUMBER OF SPACES BASED ON THE DIFFERENCE BETWEEN KNOT NUMBER AND 10
            spaces = ' ' * (10 - i)
            # 6. CREATE A VARIABLE CALLED sentence AND ADD A FORMATTED STRING THAT CALLS phrases AND spaces
            sentence = f"{phrase} {spaces}"
    
        # 7. REPLACE phrase WITH YOUR VARIABLE FOR YOUR LABEL FOR CIRCLES AND LINES
        #label = tk.Label(frame, text=f"By knot of {i}, {phrase}", anchor="center") #original line
        label = tk.Label(frame, text=f"By knot of {i}, {sentence}\n{circles_and_lines}", anchor="center")
        label.pack(fill="both", expand=True)

    phrases_window.mainloop()

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

display_phrases()
