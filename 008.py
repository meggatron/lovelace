#Ensure you have PIL installed, run the following in Terminal
#pip install Pillow
#If that doesn't work try the following in Terminal (use the verson of Python you are in)
#python3.12 -m pip install Pillow

import random
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk  # Import necessary modules from Pillow

def draw_cards():
    card_names = list(cards.keys())
    random.shuffle(card_names)
    reading = card_names[:3]

    # Assign significance to each card
    significances = ["Signifying Your Past", "Signifying Your Present", "Signifying Your Future"]
    reading_with_significance = list(zip(significances, reading))

    # Clear the previous result and images
    for label in card_labels:
        label.destroy()
    for image_label in image_labels:
        image_label.destroy()

    # Display the drawn cards with their meanings, significance, and images in the GUI
    for i, (significance, card) in enumerate(reading_with_significance):
        # Load and display the card image
        image = Image.open(f"tarot_cards/{card}.jpg")
        image = image.resize((100, 150))  # Adjust the size of the displayed image
        photo = ImageTk.PhotoImage(image)
        image_label = Label(root, image=photo)
        image_label.image = photo
        image_label.grid(row=0, column=i, padx=10)
        image_labels.append(image_label)

        # Display the text below the card
        label_text = f"{significance}\n{card}: {cards[card]}"
        label = Label(root, text=label_text, wraplength=150, justify=tk.LEFT)
        label.grid(row=1, column=i, pady=5)
        card_labels.append(label)

# Read card data from the file
with open('tarot-cards.txt') as f:
    lines = f.readlines()
    cards = dict(line.strip().split(': ', 1) for line in lines)

# Create the main window
root = tk.Tk()
root.title("Tarot Card Reading")

# Set a fixed size for the window
root.geometry("1000x600")

# Create lists to store the card labels and image labels
card_labels = []
image_labels = []

# Create a button to draw cards
draw_button = Button(root, text="Draw Cards", command=draw_cards)
draw_button.grid(row=2, column=0, columnspan=3, pady=10)

# Start the Tkinter event loop
root.mainloop()

