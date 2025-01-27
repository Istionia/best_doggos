from src.dog import BREEDS


def play_with_dog(dog):
    print(f"{dog.name} is playing with you!")
    dog.happiness += 10 - abs(BREEDS[dog.breed]["happiness_rate"])
    dog.energy -= 5 * (BREEDS[dog.breed]["energy_decay"] / 5)
    dog.hunger -= 3 * (BREEDS[dog.breed]["hunger_rate"] / 5)
    dog.hygiene -= 2
    print(f"{dog.name} is now {dog.get_status().value}")


def feed_dog(dog):
    print(f"{dog.name} is eating!")
    dog.hunger += 10 * (BREEDS[dog.breed]["hunger_rate"] / 5)
    dog.energy -= 5 * (BREEDS[dog.breed]["energy_decay"] / 5)
    dog.happiness += 5 - abs(BREEDS[dog.breed]["happiness_rate"])
    dog.hygiene -= 2
    print(f"{dog.name} is now {dog.get_status().value}")


def groom_dog(dog):
    print(f"{dog.name} is being groomed!")
    dog.hygiene += 10
    dog.energy -= 5 * (BREEDS[dog.breed]["energy_decay"] / 5)
    dog.happiness += 5 - abs(BREEDS[dog.breed]["happiness_rate"])
    dog.hunger -= 3 * (BREEDS[dog.breed]["hunger_rate"] / 5)
    print(f"{dog.name} is now {dog.get_status().value}")


def walk_dog(dog):
    print(f"{dog.name} is going for a walk!")
    dog.energy += 10 * (1 - BREEDS[dog.breed]["energy_decay"] / 10)
    dog.hunger -= 5 * (BREEDS[dog.breed]["hunger_rate"] / 5)
    dog.happiness += 5 - abs(BREEDS[dog.breed]["happiness_rate"])
    dog.hygiene -= 3
    print(f"{dog.name} is now {dog.get_status().value}")


def train_dog(dog):
    print(f"{dog.name} is training!")
    dog.skill += BREEDS[dog.breed]["skill_boost"]
    dog.energy -= 5 * (BREEDS[dog.breed]["energy_decay"] / 5)
    dog.happiness -= 3 - abs(BREEDS[dog.breed]["happiness_rate"])
    dog.hygiene -= 2
    print(f"{dog.name} is now {dog.get_status().value}")


def check_stats(dog):
    print(f"{dog.name} is checking their stats!")
    print(dog)


def save_and_quit(dog):
    print("Saving game and quitting...")
    # TODO: Implement save functionality
    print("Game saved. Goodbye!")


def rest_dog(dog):
    print("\nHow long should your dog rest?")
    print("1. Quick nap (15 energy)")
    print("2. Full sleep (40 energy)")
    
    choice = input("Choose an option (1-2): ")
    
    if choice == "1":
        print(f"{dog.name} is taking a quick nap...")
        dog.energy += 15
        dog.happiness += 5
        dog.hunger -= 2 * (BREEDS[dog.breed]["hunger_rate"] / 5)
    elif choice == "2":
        print(f"{dog.name} is getting a full night's sleep...")
        dog.energy += 40
        dog.happiness += 10
        dog.hunger -= 5 * (BREEDS[dog.breed]["hunger_rate"] / 5)
    else:
        print("Invalid choice. Taking a quick nap instead...")
        dog.energy += 15
        dog.happiness += 5
        dog.hunger -= 2 * (BREEDS[dog.breed]["hunger_rate"] / 5)
    
    print(f"{dog.name} is now {dog.get_status().value}")
