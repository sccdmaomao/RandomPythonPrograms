import random

# Given Game Constants
SWORDS = ["small", "medium", "large"]
AXES = ["small", "medium", "large"]
MAGICAL_POTIONS = ["red potion", "blue potion", "green potion"]
BOWS = ["crossbow", "shortbow", "longbow"]
LOOT = ["gems", "coins", "artifact"]
STUFF_THAT_KEEP_YOU_ALIVE = ["food", "healing potions"]
MAGICAL_ITEMS = ["wand", "scroll", "ring", "emply"]
CLASSES = ["fighter", "wizard", "thief", "healer", "ranger"]
RACES = ["human", "elf", "dwarf", "halfing", "gnome"]
MISCELLANEOUS_ITEMS = ["torch", "lamp", "key", "map", "empty"]


# Helper Constants

STATS = list(range(1, 21))
WEAPON_OPTIONS = ["swords", "axes", "bows"]
default_file_name = "character.txt"

# Helper to randomly generate results from given options
def randomly_generate(options, count):
    generated_items = []
    while(count > 0):
        index = random.randint(0, len(options)-1)
        generated_items.append(options[index])
        count -= 1
    if len(generated_items) == 1:
        return generated_items[0]
    return generated_items

        
# Ask for filename.
def get_file_name():
    filename = raw_input("File name to generate the character({}): ".format(default_file_name))
    if (filename == ""):
        filename = default_file_name
    return filename


# Ask for character's lastname + firstname
def get_char_names():
    print("Welcome to Dungeon Crawlers, what's your name?")
    first_name = raw_input("first name: ")
    last_name = raw_input("last name: ")
    return (first_name, last_name)

def build_char():
    
    # Randomly generate race + class
    char_race = randomly_generate(RACES, 1)
    char_class = randomly_generate(CLASSES, 1)

    # Randomly geenrate stats from 1-20
    char_stats = randomly_generate(STATS, 6)

    # randomly generate weapon in character's back + belt slot
    char_belt_weapon = randomly_generate(WEAPON_OPTIONS, 1)
    char_back_weapon = randomly_generate(WEAPON_OPTIONS, 1)

    char_belt_weapon_size = ""
    if (char_belt_weapon == "swords"):
        char_belt_weapon_size = randomly_generate(SWORDS, 1)
    elif (char_belt_weapon == "axes"):
        char_belt_weapon_size = randomly_generate(AXES, 1)
    elif (char_belt_weapon == "bows"):
        char_belt_weapon_size = randomly_generate(BOWS, 1)


    char_back_weapon_size = ""
    if (char_back_weapon == "swords"):
        char_back_weapon_size = randomly_generate(SWORDS, 1)
    elif (char_back_weapon == "axes"):
        char_back_weapon_size = randomly_generate(AXES, 1)
    elif (char_back_weapon == "bows"):
        char_back_weapon_size = randomly_generate(BOWS, 1)

    # randomly generate 1 item from [miscellaneous item, magical item] per hand
    combinedd_options = MISCELLANEOUS_ITEMS + MAGICAL_ITEMS
    char_left_hand = randomly_generate(combinedd_options, 1)
    char_right_hand = randomly_generate(combinedd_options, 1)


    # randomly generate 10 item from [miscellaneous, magical potion, loot, stuff, magical item] for the pack
    combined_options = MISCELLANEOUS_ITEMS + MAGICAL_POTIONS + LOOT + \
                       STUFF_THAT_KEEP_YOU_ALIVE + MAGICAL_ITEMS
    char_pack = randomly_generate(combined_options, 10)
    char_pack_text = ""
    for item in char_pack:
        char_pack_text += item + ", "
        
    char_pack_text = char_pack_text[:len(char_pack_text)-2]
    name = get_char_names()
    char_description_text = """
    Adventure's name: {0} {1}
    Class: {2}
    Race: {3}
    Strength: {4}
    Constitution: {5}
    Dexterity: {6}
    Intelligence: {7}
    Wisdom: {8}
    Charisma: {9}
    Back Slot: {10} {11}
    Belt Slot: {12} {13}
    Right Hand: {14}
    Left Hand: {15}
    Pack: {16}
    """.format(name[0], name[1],
               char_class,
               char_race,
               char_stats[0],
               char_stats[1],
               char_stats[2],
               char_stats[3],
               char_stats[4],
               char_stats[5],
               char_back_weapon_size, char_back_weapon,
               char_belt_weapon_size, char_belt_weapon,
               char_right_hand,
               char_left_hand,
               char_pack_text
               )
    return char_description_text

def write_to_file(filename, text):
    file = open(filename, "w+")
    file.write(text)
    file.close()


filename = get_file_name()
text = build_char()
write_to_file(filename, text)
