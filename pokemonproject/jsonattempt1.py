import json

with open(r"C:\Users\Bradl\Documents\GitHub\PokemonProject\pokemonproject\shrtpokedex.json") as file:
    json_data = file.read()
    mylist = json.loads(json_data)

MENU = ["Search by name",
        "search by id",
        'Filter by TYPE']



def pretty_print(lst):
    print("\n")
    for i in range(len(lst)):
        print(f"{i+1}. {lst[i]}")

def printkeys():
    all_keys = []
    for pokemon in mylist:
        for key in pokemon.keys():
            if key not in all_keys:
                all_keys.append(key)
    pretty_print(all_keys)

def name_search(): 
    user_input = input("Enter the name of the Pokémon: ") 
    for pokemon in mylist: 
        if pokemon["Name"].lower() == user_input.lower():
            print(pokemon)

def filter_cat(): #i have the filter for the list but don't know how to not hardcode the choice of the category to filter by
    #input
    user_input = input("Enter the type of the Pokémon: ") 
    filterlist = []
    for pokemon in mylist: 
        if pokemon["Type 1"].lower() == user_input.lower():
            mylist.append(pokemon)
def filter_rng():
    
    min_val = int(input("Enter the minimum value of the range: "))
    max_val = int(input("Enter the maximum value of the range: "))
    filtered_pokemon = []
    for pokemon in mylist: 
        if min_val <= pokemon[""] <= max_val:
            mylist.append(pokemon)       
    pretty_print(filtered_pokemon)

# def filter_rang():
#     user_input = input("What range do you want to filter by?")
#     for pokemon in mylist:


# def type_search():
#     user_input = input("Enter the name of the Pokémon: ") 

print("Welcome to the pokedex")
choice = None

while choice != 0:
    try:
        pretty_print(MENU)
        choice = int(input("Please make a selection: "))
        if choice == 1:
            result = name_search()
        if choice == 2:
            pass
        if choice == 3: 
            filter_opt = input(f"What do you want to filter by?", printkeys())
            # if 
            
    except ValueError:
        print(f"Error, '{choice}' is not a valid option")
