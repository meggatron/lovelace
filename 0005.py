# Create a label for each phrase with circles, lines in between, and spaces after sentences
circle_symbol = "."  # Period as the circle symbol
line_symbol = "─"  # Line symbol

# Different set of phrases
examples = ["Python is powerful", "Lists are versatile", "Coding is fun", "Learn every day"]

# Loop through phrases and create the visual representation
for i, phrase in enumerate(examples, start=1):
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
