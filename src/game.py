from src.constants import (
    MESSAGES,
    DOG_ART,
    TEXT_COLORS
)
from src.dog import VirtualDog, BREEDS
from src.interactions import (
    play_with_dog,
    feed_dog,
    groom_dog,
    walk_dog,
    train_dog,
    rest_dog,
    check_stats,
    save_and_quit
)


def display_breed_options():
    print("\nAvailable breeds:")
    for i, (breed_id, breed_info) in enumerate(BREEDS.items(), 1):
        print(f"{i}. {breed_info['name']} {breed_info['emoji']}")
        print(f"   {breed_info['description']}\n")


def get_breed_choice():
    while True:
        display_breed_options()
        choice = input(f"\nChoose a breed (1-{len(BREEDS)}): ")
        
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(BREEDS):
                return list(BREEDS.keys())[choice_num - 1]
            print(f"{TEXT_COLORS['warning']}"
                  f"Please choose a valid number (1-{len(BREEDS)})"
                  f"{TEXT_COLORS['reset']}")
        except ValueError:
            print(f"{TEXT_COLORS['warning']}"
                  f"Please enter a valid number (1-{len(BREEDS)})"
                  f"{TEXT_COLORS['reset']}")


def start_game():
    print(MESSAGES["welcome"])
    print(DOG_ART["happy"])
    
    # Get dog's name from user
    dog_name = input("\nWhat would you like to name your dog? ")
    
    # Get breed choice
    breed = get_breed_choice()
    
    # Create the dog
    dog = VirtualDog(dog_name, breed)
    
    print(
        f"\n{TEXT_COLORS['success']}Meet {dog_name}, "
        f"your new {dog.breed}! {dog.emoji}"
        f"{TEXT_COLORS['reset']}"
    )
    print(f"Description: {dog.description}")
    
    return dog


def main_game_loop(dog):
    while True:
        # Display status and warnings
        print_status(dog)
        check_warnings(dog)

        # Main menu
        print(f"\n{TEXT_COLORS['status']}HOME{TEXT_COLORS['reset']}")
        print(f"What would you like to do?")
        print("1. Interact\n"
              "2. Feed\n"
              "3. Groom\n"
              "4. Walk\n"
              "5. Train\n"
              "6. Rest\n"
              "7. Check Stats\n"
              "8. Save & Quit")
        choice = input("Choose an action: ")
        
        if choice == "1":
            play_with_dog(dog)
        elif choice == "2":
            feed_dog(dog)
        elif choice == "3":
            groom_dog(dog)
        elif choice == "4":
            walk_dog(dog)
        elif choice == "5":
            train_dog(dog)
        elif choice == "6":
            rest_dog(dog)
        elif choice == "7":
            check_stats(dog)
        elif choice == "8":
            save_and_quit(dog)
        else:
            print(f"{TEXT_COLORS['warning']}"
                  f"Please choose a valid option (1-8)"
                  f"{TEXT_COLORS['reset']}")


def print_status(dog):
    """Display the current status of the dog with colored formatting."""
    print(f"\n{TEXT_COLORS['status']}Status for {dog.name}:")
    print(f"🍖 Hunger: {dog.hunger}/100")
    print(f"😊 Happiness: {dog.happiness}/100")
    print(f"⚡ Energy: {dog.energy}/100")
    print(f"✨ Hygiene: {dog.hygiene}/100")
    print(f"🎯 Skill Level: {dog.skill}/100{TEXT_COLORS['reset']}")


def check_warnings(dog):
    """Check and display warnings for low stats."""
    warnings = []

    if dog.hunger <= 20:
        warnings.append(f"🚨 {dog.name} is very hungry!")
    elif dog.hunger <= 40:
        warnings.append(f"⚠️ {dog.name} could use a snack.")

    if dog.happiness <= 20:
        warnings.append(f"🚨 {dog.name} is very unhappy!")
    elif dog.happiness <= 40:
        warnings.append(f"⚠️ {dog.name} would like some attention.")

    if dog.energy <= 20:
        warnings.append(f"🚨 {dog.name} is exhausted!")
    elif dog.energy <= 40:
        warnings.append(f"⚠️ {dog.name} is getting tired.")

    if dog.hygiene <= 20:
        warnings.append(f"🚨 {dog.name} really needs a bath!")
    elif dog.hygiene <= 40:
        warnings.append(f"⚠️ {dog.name} is getting dirty.")

    if warnings:
        print(f"\n{TEXT_COLORS['warning']}")
        for warning in warnings:
            print(warning)
        print(TEXT_COLORS['reset'])

