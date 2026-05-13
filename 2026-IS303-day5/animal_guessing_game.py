"""

Inputs:
A sting containing an attriubte guess or the guess of the animal's name.

Processes:
- Randomly select an animal.
- Allow the user to guess until they guess the correct animal.
- When they guess, tell them if the animal has the attrubute or not.
- Tell the user whe the guess correctly

Outputs:
- Attribute guess correctness
- Congratulations message

"""

import random   # Teach Python how to do random stuff

ANIMALS = {
    "Lion" :["Mammal", "Four legs", "Predator", "Fur", "Tail", "Mane", "Roar", "Africa"],
    "Hyena":["Mammal", "Four legs", "Predator", "Spots", "Tail", "Laugh", "Africa", "Asia"],
    "Dog" :["Mammal", "Four legs", "Domestic", "Fur", "Tail", "Bark", "Worldwide", "Variety of sizes"],
    "Cat" :["Mammal", "Four legs", "Domestic", "Fur", "Tail", "Meow", "Worldwide", "Variety of sizes"],
    "Eagle" :["Bird", "Two legs", "Predator", "Feathers", "Tail", "Screech", "Worldwide", "Excellent vision"],
    "Shark" :["Fish", "Fins", "Predator", "Scales", "Tail", "Silent", "Worldwide", "Variety of sizes"],
    "Frog" :["Amphibian", "Four legs", "Predator", "Smooth skin", "Tail (as tadpole)", "Croak", "Worldwide", "Variety of sizes"],
    "Snake" :["Reptile", "No legs", "Predator", "Scales", "Tail", "Hiss", "Worldwide", "Variety of sizes"],
    "Elephant" :["Mammal", "Four legs", "Herbivore", "Thick skin", "Tail", "Trumpet", "Africa and Asia", "Large size"],
    "Giraffe" :["Mammal", "Four legs", "Herbivore", "Spots", "Tail", "Silent", "Africa", "Long neck"]
}

WELCOME_MESSAGE = """Animal guessing game
I have picked a random animal. Guess an 
attriubute or the name of the animal."""

CONGRATUALATIONS_MESSAGE = "You won!"

list_of_animal_names = list(ANIMALS.keys())
random_animal = random.choice(list_of_animal_names)
random_animal_attributes = ANIMALS[random_animal]

print(WELCOME_MESSAGE)

guess = ""

while guess != random_animal:
    guess = input("Please guess an attribute or an animal name: ").capitalize()
    if guess in random_animal_attributes:
        print(f"yes, {guess} is an attribute of the animal.")
    elif guess == random_animal:
        print(CONGRATUALATIONS_MESSAGE)
    else:
        print(f"No, {guess} is NOT an attriubte of the animal. ")

