import json

with open(r"C:\Users\Bradl\Documents\GitHub\PokemonProject\pokemonproject\shrtpokedex.json") as file:
    json_data = file.read()
    mylist = json.loads(json_data)

MENU = ["Search by Name",
        "Search by Id",
        "Filter by Type 1",
        "Filter by Type 2",
        "Filter by Speed Range",
        "Filter by Weight Range",
        "Filter by Height Range",
        "Filter by HP Range"]

SUBMENU = ["Would you like to filter further?",
           "Filter by Type 1",
           "Filter by Type 2",
           "Filter by Speed Range",
           "Filter by Weight Range",
           "Filter by Height Range",
           "Filter by HP Range",
           "Your choice"
            ]

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

def printKeysLeft():
    all_keys = []
    for pokemon in mylist:
        for key in pokemon.keys():
            if key not in all_keys:
                all_keys.append(key)
    pretty_print(all_keys)

def valid_types():
    values = []
    for pokemon in mylist:
        values.append(pokemon["Type 1"]) and values.append(pokemon["Type 2"])
    pretty_print(values)

def filter_by_type(type_to_filter):
    filtered_pokemon = []
    print("valid types: " )
    for pokemon in mylist:
        try:
            if pokemon["Type 1"].lower() == type_to_filter.lower() or pokemon["Type 2"].lower() == type_to_filter.lower():
                filtered_pokemon.append(pokemon)
        except ValueError:
            print("valid selection please")
    pretty_print(filtered_pokemon)

def name_search(): 
    user_input = input("Enter the name of the Pokémon: ") 
    matches = []
    for pokemon in mylist: 
        if user_input.lower() in pokemon["Name"].lower():
            matches.append(pokemon["Name"])
    print(matches)

def filter_range(attribute_name, unit): #when calling, atribute and unit should be in quptes as they are string    
    min_val = input(f"Enter the minimum {attribute_name}: ") #f and curly brackets lets me print the interchagable variable
    max_val = input(f"Enter the maximum {attribute_name}: ")
    try:
        filtered_pokemon = []
        min_val = float(min_val)
        max_val = float(max_val)
        for pokemon in mylist: 
            if min_val <= int(pokemon[unit]) <= max_val:
                filtered_pokemon.append(pokemon)
        pretty_print(filtered_pokemon)
    except ValueError:
        print("Must be an integer")
def id_search(): 
    user_input = input("Enter the id of the Pokémon: ")
    id_out = [] 
    for pokemon in mylist: 
        if pokemon["Id"] == user_input:
            id_out.append(pokemon["Name"])
    pretty_print(id_out)

def filter_choice(attribute_name, unit1, unit2): #refactored to get any values
    choice = input(f"What do you want to filter {attribute_name} by?\n"
                   f"1. Filter by {unit1}\n"
                   f"2. Filter by {unit2}\n"
                   "Your choice: \n")
    try:
        choice = int(choice)
        if choice == 1:
            filter_range(f"{attribute_name}",f"{unit1}")
            # return 1
        elif choice == 2:
            filter_range(f"{attribute_name}",f"{unit2}")
            # return 2
    except ValueError:
        print("Choice must be a number")

# def filter_type(): #i have the filter for the list but don't know how to not hardcode the choice of the category to filter by
    # user_input = input("Enter the type of the Pokémon: ")    
    # filterlist = []
    # for pokemon in mylist: 
    #     if pokemon["Type 1"].lower() == user_input.lower():
    #         filterlist.append(pokemon)

print("Welcome to the pokedex")
choice = None

while choice != 0:
    try:
        pretty_print(MENU)
        choice = int(input("Please make a selection: "))
        if choice == 1: #NAME SEARCH
            result = name_search()
        elif choice == 2: #ID SEARCH
            id_search()
        elif choice == 3: #Type 1 FILTER
            filter_by_type()
        elif choice == 4: #Type 2 Filter
            filter_by_type()
        elif choice == 5: #speed
            filter_range("speed", "Speed")
        elif choice == 6: #weight
            filter_choice("Weight", "Weight (kg)", "Weight (lbs)")
        elif choice == 7: #height
            filter_choice("Height", "Height (m)", "Height (ft)")
        elif choice == 8: #height
            filter_range("HP", "HP")
        elif choice == 9:
            print("Exiting...")    
            break     
    except ValueError:
        print(f"Error, '{choice}' is not a valid option")
