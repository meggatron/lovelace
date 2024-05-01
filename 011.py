import random
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk

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
        image = image.resize((200, 300))  # Adjust the size of the displayed image
        photo = ImageTk.PhotoImage(image)
        image_label = Label(root, image=photo)
        image_label.image = photo
        image_label.grid(row=0, column=i, padx=10)
        image_labels.append(image_label)

        # Display the text below the card
        label_text = f"{significance}\n{card}: {cards[card]}"
        label = Label(root, text=label_text, wraplength=200, justify=tk.LEFT, font=("Arial", 12))
        label.grid(row=1, column=i, pady=5)
        card_labels.append(label)

    # Center the entire object on the x axis
    object_width = len(reading_with_significance) * 210  # Total width of the object (image + padding)
    root.update_idletasks()  # Update the window to get the correct dimensions
    screen_width = root.winfo_screenwidth()

    x_position = (screen_width - object_width) // 2

    root.geometry(f"800x400+{x_position}+100")

# Read card data from the file
with open('tarot-cards.txt') as f:
    lines = f.readlines()
    cards = dict(line.strip().split(': ', 1) for line in lines)

# Create the main window
root = tk.Tk()
root.title("Tarot Card Reading")

# Create lists to store the card labels and image labels
card_labels = []
image_labels = []

# Create a button to draw cards
draw_button = Button(root, text="Draw Cards", command=draw_cards, font=("Arial", 14))
draw_button.grid(row=2, column=0, columnspan=3, pady=10)

# Set a fixed size for the window
root.geometry("800x400")

# Start the Tkinter event loop
root.mainloop()
