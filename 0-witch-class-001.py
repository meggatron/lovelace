# Custom Data Type (class)
class Spell:
    def __init__(self, name, incantation, power_level):
        self.name = name
        self.incantation = incantation
        self.power_level = power_level

# Create two more instances of the WitchSpell class
spell1 = Spell("Fireball", "Ignitus Infernalis", 85.5)

# Cast the spell(s)
print(f"The witch casts the {spell1.name} spell: {spell1.incantation}.")


