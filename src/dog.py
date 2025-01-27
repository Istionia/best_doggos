import json
from pathlib import Path
from enum import Enum

# Load breeds from JSON file
with open(Path(__file__).parent.parent / "data" / "breeds.json", "r") as f:
    BREEDS = json.load(f)


class DogStatus(Enum):
    PERFECT = "perfect"
    HAPPY = "happy"
    HUNGRY = "hungry"
    TIRED = "tired"
    DIRTY = "dirty"
    SAD = "sad"


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
        self.status_emojis = {
            DogStatus.PERFECT: "✨",
            DogStatus.HAPPY: "😊",
            DogStatus.HUNGRY: "🍖",
            DogStatus.TIRED: "😴",
            DogStatus.DIRTY: "🛁",
            DogStatus.SAD: "😢"
        }

    def get_status(self) -> DogStatus:
        """Calculate and return the dog's current status."""
        stats = [self.hunger, self.happiness, self.energy, self.hygiene]
        if all(attr >= 80 for attr in stats):
            return DogStatus.PERFECT
        elif self.hunger < 30:
            return DogStatus.HUNGRY
        elif self.energy < 30:
            return DogStatus.TIRED
        elif self.hygiene < 30:
            return DogStatus.DIRTY
        elif self.happiness < 30:
            return DogStatus.SAD
        else:
            return DogStatus.HAPPY

    def get_status_message(self) -> str:
        """Get a message describing the dog's current status."""
        status = self.get_status()
        messages = {
            DogStatus.PERFECT: (
                f"{self.name} is feeling absolutely wonderful!"
            ),
            DogStatus.HAPPY: (
                f"{self.name} is having a great time!"
            ),
            DogStatus.HUNGRY: (
                f"{self.name} could really use a snack..."
            ),
            DogStatus.TIRED: (
                f"{self.name} needs some rest."
            ),
            DogStatus.DIRTY: (
                f"{self.name} could use a bath."
            ),
            DogStatus.SAD: (
                f"{self.name} needs some attention."
            )
        }
        return f"{messages[status]} {self.status_emojis[status]}"

    def __str__(self):
        status = self.get_status().value
        return (f"{self.name} the {self.breed} "
                f"({self.emoji}) - {status}")
