# Create a list of different "knots."
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

# Use a for loop to iterate through the list of knots. Enumerate is a built in function.
for knot_number, knot_text in enumerate(knots, start=1):
    print(f"By knot of {knot_number}, {knot_text}")

#bonus points if you can find & fix the error!
