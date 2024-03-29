# PokemonProject
POkedex working with JSON beginner project

: https://www.kaggle.com/datasets/csobral/pokemon-gen-vii-pokedex and allows him to interact with the data in the following ways:
Search for a pokemon by number or name, including partial match and display all information about it in a human readable form
Construct a team of 6 pokemon, each of which has 4 active moves, out of the ones available. After the team has been chosen, it will be output into a similarly formatted JSON file, with only the active moves included
Filter the JSON by any combination of: type, speed range, height range, weight range, HP range and output the result into a JSON file

Take special care to not corrupt the original data file while the application is running, and make sure that any writes are done into a file that isn't the original one. The application should have no hardcoded data, and all data should come from reading the original JSON file.
Also, I recommend working with a smaller dataset as you are building the application, there is no reason to waste time loading all 800+ pokemon every time you are doing a test run. The full file should be loaded and tested with only as you are getting closer to finishing the full application.
Best of luck!
