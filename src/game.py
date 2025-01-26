from constants import MESSAGES, DOG_ART


def start_game():
    print("WOOF WOOF!")
    # Initialize game and start loop
    print(MESSAGES["welcome"])
    print(DOG_ART["happy"])
    # Get dog's name from user
    dog_name = input("What would you like to name your dog? ")

    # Show available breeds and get selection
    print("\nAvailable breeds:")
    from dog import BREEDS
    for i, breed in enumerate(BREEDS.keys(), 1):
        print(f"{i}. {BREEDS[breed]['name']} {BREEDS[breed]['emoji']}")
        print(f"   {BREEDS[breed]['description']}\n")

    while True:
        try:
            breed_choice = int(input("Choose a breed (enter number): ")) - 1
            if 0 <= breed_choice < len(BREEDS):
                chosen_breed = list(BREEDS.keys())[breed_choice]
                break
            print("Please enter a valid number!")
        except ValueError:
            print("Please enter a valid number!")

    # Create the virtual dog
    from dog import VirtualDog
    active_dog = VirtualDog(dog_name, chosen_breed)
    print(f"\nSay hello to {active_dog}!")