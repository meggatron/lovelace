class Alchemist:
    def __init__(self, name):
        self.name = name
        self.potion_inventory = []

    def create_and_display_potion(self, potion_name):
        new_potion = f"{potion_name} Potion"
        self.potion_inventory.append(new_potion)
        return f"{self.name} concocts a {new_potion}! Inventory: {self.potion_inventory}"

# Creating an instance of the Alchemist class
cleopatra = Alchemist("Cleopatra")

# Calling the method to create a potion and display the inventory
result = cleopatra.create_and_display_potion("Invisibility")
print(result)
