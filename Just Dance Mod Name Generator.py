import random

def generate_just_dance_mod_name():
    # List of adjectives and nouns
    adjectives = ["Fast","Sunshine", "Party" "Energetic", "Funky", "Bright", "Synchronized", "Electro", "Amazing", "Colorful", "Magical", "Spinny", "Groovy", "Wild", "Spectacular", "Dynamic", "Stylish", "Flashy", "Sensual", "Radical", "Astonishing", "Clever"]
    nouns = ["Dancer", "Movement", "Rhythm", "Choreography", "Step", "Sync", "Show", "Performance", "Floor", "Stage", "Talent", "Shine", "Funk", "Flavor", "Rebellion", "Style", "Melody", "Enchantment", "Beat", "Glare"]

    # Choose a random adjective and noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    # Form the mod name
    mod_name = f"Just Dance {adjective} {noun}"

    return mod_name

# Ask the user to input the word "Just Dance"
input_word = input("To generate a Just Dance mod name, type 'Just Dance': ")
if input_word.lower() == "just dance":
    mod_name = generate_just_dance_mod_name()
    print("Tool Made By SquareJDBR Based in Chat GPT Code")
    print("Just Dance Mod Name:", mod_name)
else:
    print("Incorrect input. Make sure to type 'Just Dance' exactly as shown.")
