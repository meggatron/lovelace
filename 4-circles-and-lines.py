# Create a label for each phrase with circles, lines in between, and spaces after sentences
circle_symbol = "."  
line_symbol = "─"  

# Different set of phrases
examples = ["Python is powerful", "Lists are versatile", "Coding is fun", "Learn every day"]

# Loop through phrases and create the visual representation
for i, phrase in enumerate(examples, start=1):
    # Create a label for each phrase with circles, lines in between, and spaces after sentences
    circles_and_lines = f"{line_symbol.join(circle_symbol * i)}"
    
    if i < 5:
        # Calculate the number of spaces based on the difference between line number and 4
        spaces = ' ' * (2*(5 - i)) #see what changes when you remove the hashtag
        sentence = f"{spaces}{phrase} "
  
    
    # Print the visual representation and sentence
    print(f"{circles_and_lines} {sentence}")

#ASSIGNMENTS

#1. create different variables for circle and line, experiment: try symbols or longer strings.
#2. uncomment the second half of spaces in the if statement and modify the integer
