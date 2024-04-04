import json

with open(r"C:\Users\Bradl\Documents\GitHub\PokemonProject\pokemonproject\shrtpokedex.json") as file:
    json_data = file.read()
    mylist = json.loads(json_data)

MENU = ["Search by Name",
        "Search by Id",
        "Filter by Type",
        "Filter by Speed Range",
        "Filter by Weight Range",
        "Filter by Height Range",
        "Filter by HP Range"]

SUBMENU = ["Would you like to filter further?",
           "Filter by Type",
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

def valid_types():
    values = []
    for pokemon in mylist:
        values.append(pokemon["Type 1"]) and values.append(pokemon["Type 2"])
    pretty_print(values)

def id_search(): 
    user_input = input("Enter the id of the Pokémon: ")
    id_out = [] 
    for pokemon in mylist: 
        if pokemon["Id"] == user_input:
            id_out.append(pokemon["Name"])
    pretty_print(id_out)

def filter_by_type(type_to_filter):
    filtered_pokemon = []
    for pokemon in mylist:
        try:
            if pokemon["Type 1"].lower() == type_to_filter.lower() or pokemon["Type 2"].lower() == type_to_filter.lower():
                filtered_pokemon.append(pokemon["Name"])
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
            if min_val <= float(pokemon[f"{unit}"]) <= max_val: #there is a speical case here for feet because the feet and inches cannot be converted to a float
                filtered_pokemon.append(pokemon["Name"])
        pretty_print(filtered_pokemon)
    except ValueError:
        print("Must be an integer")

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
        elif choice == 3: #TypE Filter
            user_input = input("What type do you want to filter by?: ")
            filter_by_type(user_input)
        elif choice == 4: #speed
            filter_range("speed", "Speed")
        elif choice == 5: #weight
            selection = input("Search by:\n"
                            "1. Kilograms\n"
                            "2. Pounds\n"
                            "Your choice: ")
            try: 
                selection = int(selection)
                if selection == 1:
                    filter_range("Weight", "Weight (kg)")
                if selection == 2:
                    filter_range("Weight", "Weight (lbs)")
            except ValueError:
                print("You must select a number")
        elif choice == 6: #height
            selection = input("Search by:\n"
                              "1. Meters\n"
                              "2. feet\n"
                              "Your choice: ")
            try: 
                selection = int(selection)
                if selection == 1:
                    filter_range("Height", "Height (m)")
                if selection == 2:
                    filter_range("Height", "Height (ft)")
            except ValueError:
                print("You must select a number")
        elif choice == 7: #HP
            filter_range("HP", "HP")
        elif choice == 8:
            print("Exiting...")    
            break     
    except ValueError:
        print(f"Error, '{choice}' is not a valid option")
