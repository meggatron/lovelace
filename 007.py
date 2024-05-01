import random
import tkinter as tk
from tkinter import Label, Button

def draw_cards():
    card_names = list(cards.keys())
    random.shuffle(card_names)
    reading = card_names[:3]

    # Assign significance to each card
    significances = ["Signifying Your Past", "Signifying Your Present", "Signifying Your Future"]
    reading_with_significance = list(zip(significances, reading))

    # Clear the previous result
    for label in card_labels:
        label.destroy()

    # Display the drawn cards with their meanings and significance in the GUI
    for i, (significance, card) in enumerate(reading_with_significance):
        label_text = f"{significance}: {card}: {cards[card]}"
        label = Label(root, text=label_text, wraplength=400, justify=tk.LEFT)
        label.pack(pady=5)
        card_labels.append(label)

# Read card data from the file
with open('tarot-cards.txt') as f:
    lines = f.readlines()
    cards = dict(line.strip().split(': ', 1) for line in lines)

# Create the main window
root = tk.Tk()
root.title("Tarot Card Reading")

# Set a fixed size for the window
# root.geometry("500x200")

# Create a list to store the card labels
card_labels = []

# Create a button to draw cards
draw_button = Button(root, text="Draw Cards", command=draw_cards)
draw_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
