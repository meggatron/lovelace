import random
import tkinter as tk
from tkinter import Label, Button, Frame
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
        image_label = Label(content_frame, image=photo, bg=background_color)
        image_label.image = photo
        image_label.grid(row=0, column=i, padx=10)
        image_labels.append(image_label)

        # Display the text below the card with the significance line bold
        label_significance = Label(content_frame, text=significance, font=("Arial", 12, "bold"), anchor="w", bg=background_color, fg=font_color)
        label_significance.grid(row=1, column=i, pady=2)
        label_card = Label(content_frame, text=card, font=("Arial", 12), anchor="w", bg=background_color, fg=font_color)
        label_card.grid(row=2, column=i, pady=2)
        label_meaning = Label(content_frame, text=cards[card], font=("Arial", 12), anchor="w", bg=background_color, fg=font_color)
        label_meaning.grid(row=3, column=i, pady=2)
        card_labels.extend([label_significance, label_card, label_meaning])

    # Update the content frame to ensure it's properly displayed
    content_frame.update_idletasks()
    content_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Read card data from the file
with open('tarot-cards.txt') as f:
    lines = f.readlines()
    cards = dict(line.strip().split(': ', 1) for line in lines)

# Set colors
background_color = "black"
font_color = "white"

# Create the main window
root = tk.Tk()
root.title("Tarot Card Reading")

# Set background color for the root window
root.configure(bg=background_color)

# Create a frame to hold the content
content_frame = Frame(root, bg=background_color, borderwidth=0, highlightthickness=0)

# Create lists to store the card labels and image labels
card_labels = []
image_labels = []

# Create a button to draw cards
draw_button = Button(root, text="Draw Cards", command=draw_cards, font=("Arial", 14), bg="lightgray",borderwidth=0, highlightthickness=0)
draw_button.pack(side=tk.BOTTOM, pady=(0, 20))  # Increased vertical padding

# Set a fixed size for the window
root.geometry("800x500")

# Start the Tkinter event loop
root.mainloop()
