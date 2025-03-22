import json
with open(r"C:\Users\Bradl\OneDrive\Documents\GitHub\PokemonProject\dataset.json") as file:
    mylist = json.load(file)

import pprint

MENU = ["Search by Name",
        "Search by ID",
        "Filter by Height, Weight and Speed",
        "Select Pokemon for your team",
        "View your team",
        "Clear the Team",
        "Show all move in Pokedex(Across all pokemon)"
        ]

def pretty_print(lst):
    print("\n")
    for i in range(len(lst)):
        print(f"{i+1}. {lst[i]}")

