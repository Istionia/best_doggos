import json
from pathlib import Path

# Load breeds from JSON file
with open(Path(__file__).parent.parent / "data" / "breeds.json", "r") as f:
    BREEDS = json.load(f)

class VirtualDog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.hygiene = 50
        self.skill = 0
        self.hunger_rate = BREEDS[breed]["hunger_rate"]
        self.skill_boost = BREEDS[breed]["skill_boost"]
        self.energy_decay = BREEDS[breed]["energy_decay"]
        self.emoji = BREEDS[breed]["emoji"]
        self.description = BREEDS[breed]["description"]

    def __str__(self):
        return f"{self.name} the {self.breed} ({self.emoji})"
