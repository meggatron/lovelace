# Create a label for each phrase with circles, lines in between, and spaces after sentences
circle_symbol = "\u25CF"  # Unicode for a larger circle (●)
line_symbol = "─"  # Line symbol

# List of phrases
knots = ["This is phrase 1", "This is phrase 2", "This is phrase 3", "This is phrase 4", "This is phrase 5",
         "This is phrase 6", "This is phrase 7", "This is phrase 8", "This is phrase 9", "This is phrase 10",
         "This is phrase 11", "This is phrase 12"]

# Loop through phrases and create the visual representation
for i, phrase in enumerate(knots, start=1):
    # Create a label for each phrase with circles, lines in between, and spaces after sentences
    circles_and_lines = f"{line_symbol.join(circle_symbol * i)}"
    
    if i < 10:
        # Calculate the number of spaces based on the difference between knot number and 10
        spaces = ' ' * (10 - i)
        # Left-align the sentence and add spaces after it
        sentence = f"{phrase} {spaces}"
    else:
        sentence = phrase
    
    # Print the visual representation and sentence
    print(f"{circles_and_lines} {sentence}")
