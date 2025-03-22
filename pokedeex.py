import ujson
from rapidfuzz import fuzz, process
import pprint
with open(r"dataset.json") as file:
    mylist = ujson.load(file)



MENU = ["Search by Name",
        "Search by ID",
        "Filter by Height, Weight and Speed"
        # "Select Pokemon for your team",
        # "View your team",
        # "Clear the Team",
        # # "Show all move in Pokedex(Across all pokemon)"
        ]

def pretty_print(lst):
    print("\n")
    for i in range(len(lst)):
        print(f"{i+1}. {lst[i]}")

def id_search():
    try:
        user_input = input("Enter the ID of the Pokémon: ")
        for pokemon in mylist:
            if pokemon["Id"] == user_input:
                print("Here is the match:")
                print(pokemon)
                return pokemon
        else:
            print("No Pokémon found with that ID.")
    except ValueError:
        print("Please enter a valid ID.")
'''
Linear search for fuzzy match
'''
def name_search(user_input):
    try:
        matches = []
        for pokemon in mylist:
            if user_input.lower() in (pokemon["Name"].lower()):
                matches.append(pokemon)
        else:
            print("No Pokémon found with that name.")
    except Exception as e:
        print(f"An error occurred: {e}")
# """
# Takes input for a type of pokemon and returns a pokemon matching the type
# """
def filter_by_type(mylist, type_to_filter):
    result = []
    for pokemon in mylist:
        try:
            if pokemon["Type 1"].lower() == type_to_filter.lower() or pokemon["Type 2"].lower() == type_to_filter.lower():
                result.append(pokemon)
            else:
                print("No")
        except ValueError:
            print("valid selection please")
    print(result)
    return result
"""
Retrieves the min max values for all the search criteria for filter_by_range()
"""
def get_min_max():
    try:
        hmin = float(input("Enter minimum Height: "))
        hmax = float(input("Enter maximum Height: "))
        wmin = float(input("Enter minimum Weight: "))
        wmax = float(input("Enter maximum Weight: "))
        smin = float(input("Enter minimum Speed: "))
        smax = float(input("Enter maximum Speed: "))

    except ValueError:
        print("MUst be a valid number")    
    return hmin, hmax, wmin, wmax, smin, smax 
'''
Finds the pokemon that match the min and max values retrived by input through get_min_max().
'''
def filter_by_range(mylist, hmin, hmax, wmin, wmax, smin, smax):
    result = []
    for pokemon in mylist: 
        height = float(pokemon.get("Height (m)", 0))
        weight = float(pokemon.get("Weight (kg)", 0))
        speed = float(pokemon.get("Speed", 0))
        # print(speed, height, weight)
        if (smin <= speed <= smax and hmin <= height <= hmax and wmin <= weight <= wmax): 
            result.append(pokemon)
    pprint.pp(result)
    for i in result:
        print(i["Name"])
        print()
    return result

"""
Main menu
"""
print("Welcome to the Pokédex")
while True:
    try:
        pretty_print(MENU)
        choice = int(input("Please make a selection (0 to quit): "))
        if choice == 1:
            user_input = input("Enter the name of the Pokémon: ")
            name_search(user_input)
        elif choice == 2:
            id_search()
        elif choice == 3:
            hmin, hmax, wmin, wmax, smin, smax = get_min_max()
            filter_by_range(mylist, hmin, hmax, wmin, wmax, smin, smax)
        # elif choice == 4:
        #     pokename = input("Which pokemon would you like to add to your team?: ")
        #     matchlist = name_search(pokename)
        #     want_to_add = add_to_team(matchlist)
        #     if want_to_add == False:
        #         continue
        #     else:        
        #         activemoves = move_display(want_to_add)
        #         json_write(activemoves)
        # elif choice == 5:
        #     team_view()
        # elif choice == 6:
        #     team_clear()
        # elif choice == 7:
        #     move_display(mylist) 
        elif choice == 0:
            print("Goodbye!")            
            break
        else:
            print("Invalid choice. Please choose a number between 0 and 7. 0 to quit")
    except ValueError:
        print("Invalid choice. Please enter a number.")
