# mylist = json.loads("Prettypokedex.json")

#Figured out the length of the list is 3 dictionaries???
# size = len(mylist)
# print(size)
import pprint #-> this does work!
pp = pprint.PrettyPrinter(indent=0)  #read the documentation for pretty print extension
# pp.pprint(dictp)

import json

mylist = [
    {"Id": "001", "Name": "Bulbasaur", "Type 1": "Grass", "Type 2": "Poison", "Abilities": ["Overgrow", "Chlorophyll"], "Category": "Seed Pok\u00e9mon", "Height (ft)": "2'04\"", "Height (m)": "0.7", "Weight (lbs)": "15.2", "Weight (kg)": "6.9", "Capture Rate": "45", "Egg Steps": "5120", "Exp Group": "Medium Slow", "Total": "318", "HP": "45", "Attack": "49", "Defense": "49", "Sp. Attack": "65", "Sp. Defense": "65", "Speed": "45", "Moves": {"Tackle": {"Type": "Normal", "Level": "\u2014", "Power": "40", "Accuracy": "100", "PP": "35", "Effect %": "--", "Description": "A physical attack in which the user charges and slams into the target with its whole body."}, "Growl": {"Type": "Normal", "Level": "3", "Power": "--", "Accuracy": "100", "PP": "40", "Effect %": "--", "Description": "The user growls in an endearing way, making opposing Pok\u00e9mon less wary. This lowers their Attack stat."}, "Vine Whip": {"Type": "Grass", "Level": "9", "Power": "45", "Accuracy": "100", "PP": "25", "Effect %": "--", "Description": "The target is struck with slender, whiplike vines to inflict damage."}, "Poison Powder": {"Type": "Poison", "Level": "13", "Power": "--", "Accuracy": "75", "PP": "35", "Effect %": "--", "Description": "The user scatters a cloud of poisonous dust that poisons the target."}, "Sleep Powder": {"Type": "Grass", "Level": "13", "Power": "--", "Accuracy": "75", "PP": "15", "Effect %": "--", "Description": "The user scatters a big cloud of sleep-inducing dust around the target."}, "Take Down": {"Type": "Normal", "Level": "15", "Power": "90", "Accuracy": "85", "PP": "20", "Effect %": "--", "Description": "A reckless, full-body charge attack for slamming into the target. This also damages the user a little."}, "Razor Leaf": {"Type": "Grass", "Level": "19", "Power": "55", "Accuracy": "95", "PP": "25", "Effect %": "--", "Description": "Sharp-edged leaves are launched to slash at the opposing Pok\u00e9mon. Critical hits land more easily."}, "Sweet Scent": {"Type": "Normal", "Level": "21", "Power": "--", "Accuracy": "100", "PP": "20", "Effect %": "--", "Description": "A sweet scent that harshly lowers opposing Pok\u00e9mon's evasiveness."}, "Growth": {"Type": "Normal", "Level": "25", "Power": "--", "Accuracy": "--", "PP": "20", "Effect %": "--", "Description": "The user's body grows all at once, raising the Attack and Sp. Atk stats."}, "Double-Edge": {"Type": "Normal", "Level": "27", "Power": "120", "Accuracy": "100", "PP": "15", "Effect %": "--", "Description": "A reckless, life-risking tackle. This also damages the user quite a lot."}, "Worry Seed": {"Type": "Grass", "Level": "31", "Power": "--", "Accuracy": "100", "PP": "10", "Effect %": "--", "Description": "A seed that causes worry is planted on the target. It prevents sleep by making the target's Ability Insomnia."}, "Synthesis": {"Type": "Grass", "Level": "33", "Power": "--", "Accuracy": "--", "PP": "5", "Effect %": "--", "Description": "The user restores its own HP. The amount of HP regained varies with the weather."}, "Seed Bomb": {"Type": "Grass", "Level": "37", "Power": "80", "Accuracy": "100", "PP": "15", "Effect %": "--", "Description": "The user slams a barrage of hard-shelled seeds down on the target from above."}}},
    {"Id": "002", "Name": "Ivysaur", "Type 1": "Grass", "Type 2": "Poison", "Abilities": ["Overgrow", "Chlorophyll"], "Category": "Seed Pok\u00e9mon", "Height (ft)": "3'03\"", "Height (m)": "1", "Weight (lbs)": "28.7", "Weight (kg)": "13", "Capture Rate": "45", "Egg Steps": "5120", "Exp Group": "Medium Slow", "Total": "405", "HP": "60", "Attack": "62", "Defense": "63", "Sp. Attack": "80", "Sp. Defense": "80", "Speed": "60", "Moves": {"Tackle": {"Type": "Normal", "Level": "\u2014", "Power": "40", "Accuracy": "100", "PP": "35", "Effect %": "--", "Description": "A physical attack in which the user charges and slams into the target with its whole body."}, "Growl": {"Type": "Normal", "Level": "3", "Power": "--", "Accuracy": "100", "PP": "40", "Effect %": "--", "Description": "The user growls in an endearing way, making opposing Pok\u00e9mon less wary. This lowers their Attack stat."}, "Leech Seed": {"Type": "Grass", "Level": "7", "Power": "--", "Accuracy": "90", "PP": "10", "Effect %": "--", "Description": "A seed is planted on the target. It steals some HP from the target every turn."}, "Vine Whip": {"Type": "Grass", "Level": "9", "Power": "45", "Accuracy": "100", "PP": "25", "Effect %": "--", "Description": "The target is struck with slender, whiplike vines to inflict damage."}, "Poison Powder": {"Type": "Poison", "Level": "13", "Power": "--", "Accuracy": "75", "PP": "35", "Effect %": "--", "Description": "The user scatters a cloud of poisonous dust that poisons the target."}, "Sleep Powder": {"Type": "Grass", "Level": "13", "Power": "--", "Accuracy": "75", "PP": "15", "Effect %": "--", "Description": "The user scatters a big cloud of sleep-inducing dust around the target."}, "Take Down": {"Type": "Normal", "Level": "15", "Power": "90", "Accuracy": "85", "PP": "20", "Effect %": "--", "Description": "A reckless, full-body charge attack for slamming into the target. This also damages the user a little."}, "Razor Leaf": {"Type": "Grass", "Level": "20", "Power": "55", "Accuracy": "95", "PP": "25", "Effect %": "--", "Description": "Sharp-edged leaves are launched to slash at the opposing Pok\u00e9mon. Critical hits land more easily."}, "Sweet Scent": {"Type": "Normal", "Level": "23", "Power": "--", "Accuracy": "100", "PP": "20", "Effect %": "--", "Description": "A sweet scent that harshly lowers opposing Pok\u00e9mon's evasiveness."}, "Growth": {"Type": "Normal", "Level": "28", "Power": "--", "Accuracy": "--", "PP": "20", "Effect %": "--", "Description": "The user's body grows all at once, raising the Attack and Sp. Atk stats."}, "Double-Edge": {"Type": "Normal", "Level": "31", "Power": "120", "Accuracy": "100", "PP": "15", "Effect %": "--", "Description": "A reckless, life-risking tackle. This also damages the user quite a lot."}, "Worry Seed": {"Type": "Grass", "Level": "36", "Power": "--", "Accuracy": "100", "PP": "10", "Effect %": "--", "Description": "A seed that causes worry is planted on the target. It prevents sleep by making the target's Ability Insomnia."}, "Synthesis": {"Type": "Grass", "Level": "39", "Power": "--", "Accuracy": "--", "PP": "5", "Effect %": "--", "Description": "The user restores its own HP. The amount of HP regained varies with the weather."}, "Solar Beam": {"Type": "Grass", "Level": "44", "Power": "120", "Accuracy": "100", "PP": "10", "Effect %": "--", "Description": "In this two-turn attack, the user gathers light, then blasts a bundled beam on the next turn."}}},
    {"Id": "003", "Name": "Venusaur", "Type 1": "Grass", "Type 2": "Poison", "Abilities": ["Overgrow", "Chlorophyll"], "Category": "Seed Pok\u00e9mon", "Height (ft)": "6'07\"", "Height (m)": "2", "Weight (lbs)": "220.5", "Weight (kg)": "100", "Capture Rate": "45", "Egg Steps": "5120", "Exp Group": "Medium Slow", "Total": "525", "HP": "80", "Attack": "82", "Defense": "83", "Sp. Attack": "100", "Sp. Defense": "100", "Speed": "80", "Moves": {"Petal Dance": {"Type": "Grass", "Level": "Evolve", "Power": "120", "Accuracy": "100", "PP": "10", "Effect %": "--", "Description": "The user attacks the target by scattering petals for two to three turns. The user then becomes confused."}, "Tackle": {"Type": "Normal", "Level": "\u2014", "Power": "40", "Accuracy": "100", "PP": "35", "Effect %": "--", "Description": "A physical attack in which the user charges and slams into the target with its whole body."}, "Growl": {"Type": "Normal", "Level": "3", "Power": "--", "Accuracy": "100", "PP": "40", "Effect %": "--", "Description": "The user growls in an endearing way, making opposing Pok\u00e9mon less wary. This lowers their Attack stat."}, "Leech Seed": {"Type": "Grass", "Level": "7", "Power": "--", "Accuracy": "90", "PP": "10", "Effect %": "--", "Description": "A seed is planted on the target. It steals some HP from the target every turn."}, "Vine Whip": {"Type": "Grass", "Level": "9", "Power": "45", "Accuracy": "100", "PP": "25", "Effect %": "--", "Description": "The target is struck with slender, whiplike vines to inflict damage."}, "Poison Powder": {"Type": "Poison", "Level": "13", "Power": "--", "Accuracy": "75", "PP": "35", "Effect %": "--", "Description": "The user scatters a cloud of poisonous dust that poisons the target."}, "Sleep Powder": {"Type": "Grass", "Level": "13", "Power": "--", "Accuracy": "75", "PP": "15", "Effect %": "--", "Description": "The user scatters a big cloud of sleep-inducing dust around the target."}, "Take Down": {"Type": "Normal", "Level": "15", "Power": "90", "Accuracy": "85", "PP": "20", "Effect %": "--", "Description": "A reckless, full-body charge attack for slamming into the target. This also damages the user a little."}, "Razor Leaf": {"Type": "Grass", "Level": "20", "Power": "55", "Accuracy": "95", "PP": "25", "Effect %": "--", "Description": "Sharp-edged leaves are launched to slash at the opposing Pok\u00e9mon. Critical hits land more easily."}, "Sweet Scent": {"Type": "Normal", "Level": "23", "Power": "--", "Accuracy": "100", "PP": "20", "Effect %": "--", "Description": "A sweet scent that harshly lowers opposing Pok\u00e9mon's evasiveness."}, "Growth": {"Type": "Normal", "Level": "28", "Power": "--", "Accuracy": "--", "PP": "20", "Effect %": "--", "Description": "The user's body grows all at once, raising the Attack and Sp. Atk stats."}, "Double-Edge": {"Type": "Normal", "Level": "31", "Power": "120", "Accuracy": "100", "PP": "15", "Effect %": "--", "Description": "A reckless, life-risking tackle. This also damages the user quite a lot."}, "Worry Seed": {"Type": "Grass", "Level": "39", "Power": "--", "Accuracy": "100", "PP": "10", "Effect %": "--", "Description": "A seed that causes worry is planted on the target. It prevents sleep by making the target's Ability Insomnia."}, "Synthesis": {"Type": "Grass", "Level": "45", "Power": "--", "Accuracy": "--", "PP": "5", "Effect %": "--", "Description": "The user restores its own HP. The amount of HP regained varies with the weather."}, "Petal Blizzard": {"Type": "Grass", "Level": "50", "Power": "90", "Accuracy": "100", "PP": "15", "Effect %": "--", "Description": "The user stirs up a violent petal blizzard and attacks everything around it."}, "Solar Beam": {"Type": "Grass", "Level": "53", "Power": "120", "Accuracy": "100", "PP": "10", "Effect %": "--", "Description": "In this two-turn attack, the user gathers light, then blasts a bundled beam on the next turn."}}},
]

MENU = ["Search by name",
        "search by id",]

# name = mylist[0]["Name"] #How to make this into a function that will be universal (?)
# print(name)



def pretty_print(lst):
    print("\n")
    for i in range(len(lst)):
        print(f"{i+1}. {lst[i]}")

def name_search(): #function takes no arguments
    user_input = input("Enter the name of the Pokémon: ") 
    #tried making a placehollder dictionary dictp = {} but didnt work
    for pokemon in mylist: #searching through the list of dictionaries1
        if pokemon["Name"].lower() == user_input.lower(): #matching the correct dictionaries
            print(pokemon)
            # return pokemon
            # dictp.update(pokemon) #!!!This doesn"t work because "Update" command just merges dictionaries!!! #adding the specified pokemons dictionary. Maybe have to wokr the ressult to find the extra info
    print("Here are the matches:")
    print(f"Name:", user_input, " :")
    # print(dictp)
    # pp.pprint(pokemon)
    # return pokemon

print("Welcome to the pokedex")
choice = None

while choice != 0:
    try:
        pretty_print(MENU)
        choice = int(input("Please make a selection: "))
        if choice == 1:
            result = name_search()
            
    except ValueError:
        print(f"Error, '{choice}' is not a valid option")






# for item in mylist:
#     print(item)

# def pokedex_id(pokemon_id):
#     for pokemon in mylist:
#         if pokemon['Id'] == str(pokemon_id):
#             print(pokemon)

# def pokedex_name(pokemon_name):
#     for pokemon in mylist:
#         if pokemon["Name"] == str(pokemon_name): #Trying to find bulbasaur 
#             print(pokemon)


pokemon = input("What is the id of the pokemon?:" )


# def find_pokemon_by_id(pokedex, pokemon_id):
#     for pokemon in pokedex:
#         if pokemon["Name"] == pokemon_id:
#             return pokemon
#     return None

# print(pokedex[1])
# pokemon_id = input("search term")
# print(pokemon)
