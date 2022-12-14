import csv

COL_ID = 0
COL_NAME = "Name"
COL_FORM = "Form"
COL_TYPE1 = "Type1"
COL_TYPE2 = "Type2"
COL_TOTAL = "Total"
COL_HP = "HP"
COL_ATTACK = "Attack"
COL_DEFENSE = "Defense"
COL_SPATK = "Sp. Atk"
COL_SPDEF = "Sp. Def"
COL_SPEED = "Speed"
COL_GEN = "Generation"
COL_BANNED = 13

file = open("paldea_dex.csv")
# Abrimos cualquier archivo

csvreader = csv.reader(file)
# Leemos el archivo .csv

data = []
data = next(csvreader)

# paldea_dex = {}
# for pokemon in csvreader:
#     paldea_dex[str(pokemon[COL_ID])] = {}
#     for i in range(1, len(data)):
#         paldea_dex[str(pokemon[COL_ID])][data[i]] = pokemon[i]
# Diccionario de la Pokédex de Paldea

unbanned_pokemon_list = {}
for pokemon in csvreader:
    if pokemon[COL_BANNED] == 'true':
        continue

    unbanned_pokemon_list[str(pokemon[COL_ID])] = {}
    for i in range(1, len(data)):
        unbanned_pokemon_list[str(pokemon[COL_ID])][data[i]] = pokemon[i]
# Diccionario de la Pokédex de Paldea (excepto baneados)

# main -----------------------------------------------------------------------------------------------

def main():

    cmd = None
    filtered_pkm_list = unbanned_pokemon_list.copy()
    filtered_team_list = unbanned_pokemon_list.copy()
    search_pkm_list = unbanned_pokemon_list.copy()
    team_list_provisional = {}
    team_list = {}

    print("")
    print("Welcome to the Paldea Dex filter!")
    print("Made by Bertus :)")
    print("")
    print("Use the commands 'filter', 'search', 'team' or 'save'.")
    print("You can filter by stats and/or types.")
    print("You can search by name.")
    print("You can build a team, adding and removing Pokemon.")
    print("You can also save the filter list or the team.")
    print("Enjoy.")
    print("")

    while cmd != "exit":

        cmd = input(">")
        cmd_list = list(cmd.split(" "))

        if cmd_list[0] != "filter" and cmd_list[0] != "search" and cmd_list[0] != "team" and cmd_list[0] != "save" and cmd_list[0] != "reset":
            print("")
            print("There is no such command.") 
            print("Try again.")
            print("")

        if cmd_list[0] == "filter":  
            if cmd_list[1] == "total_stats":
                filtered_pkm_list = pkm_total_stats(filtered_pkm_list, int(cmd_list[2]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "hp":
                filtered_pkm_list = pkm_hp(filtered_pkm_list, int(cmd_list[2]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "attack":
                filtered_pkm_list = pkm_attack(filtered_pkm_list, int(cmd_list[2]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "spattack":
                filtered_pkm_list = pkm_spattack(filtered_pkm_list, int(cmd_list[2]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "spdefense":
                filtered_pkm_list = pkm_spdefense(filtered_pkm_list, int(cmd_list[2]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "defense":
                filtered_pkm_list = pkm_defense(filtered_pkm_list, int(cmd_list[2]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "speed":
                filtered_pkm_list = pkm_speed(filtered_pkm_list, int(cmd_list[2]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "spatk_speed":
                filtered_pkm_list = pkm_speed(filtered_pkm_list, int(cmd_list[2]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "atk_speed":
                filtered_pkm_list = pkm_atk_speed(filtered_pkm_list, int(cmd_list[2]), int(cmd_list[3]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "spdef_hp":
                filtered_pkm_list = pkm_spdef_hp(filtered_pkm_list, int(cmd_list[2]), int(cmd_list[3]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "def_hp":
                filtered_pkm_list = pkm_def_hp(filtered_pkm_list, int(cmd_list[2]), int(cmd_list[3]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "type":
                filtered_pkm_list = pkm_type(filtered_pkm_list, cmd_list[2])
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "types":
                filtered_pkm_list = pkm_types(filtered_pkm_list, cmd_list[2], cmd_list[3])
                print_pokemon(filtered_pkm_list)
                print("")

        if cmd_list[0] == "search":
            pkm_namefilter(search_pkm_list, cmd_list[1])

        if cmd_list[0] == "team":
            if cmd_list[1] == "add":
                team_list = pkm_teambuilder_add(filtered_team_list, team_list_provisional, team_list, cmd_list[2])

            if cmd_list[1] == "remove":
                team_list = pkm_teambuilder_remove(team_list, cmd_list[2])

            if cmd_list[1] == "show":
                if team_list:
                    print("")
                    print_pokemon(team_list)
                    print("")
                else:
                    print("")
                    print("Team is empty.")
                    print("")

            if cmd_list[1] == "reset":
                team_list = {}
                print("")
                print("Team is successfully reseted.")
                print("")

        if cmd_list[0] == "reset":
            filtered_pkm_list = unbanned_pokemon_list.copy()
            print("")
            print("Pokemon list reseted, you can filter/search again.")
            print("")
            
        if cmd_list[0] == "save":
            if cmd_list[1] == "filter":
                with open(f"{cmd_list[2]}.csv", "w+") as f:
                    for id, attributes in filtered_pkm_list.items():
                        f.write("%s:%s\n" % (id, attributes))

                print("")
                print(f"List successfully saved as {cmd_list[2]}.csv")
                print("")
            if cmd_list[1] == "team":
                with open(f"{cmd_list[2]}.csv", "w+") as f:
                    for id, attributes in team_list.items():
                        f.write("%s:%s\n" % (id, attributes))

                print("")
                print(f"Team successfully saved as {cmd_list[2]}.csv")
                print("")


# print -----------------------------------------------------------------------------------------------

def print_pokemon(pkm_list):
    for id, attributes in pkm_list.items():
        print(attributes[COL_NAME] + " | Form: " + attributes["Form"] + " | Types: " + attributes["Type1"] + ", " + attributes["Type2"] + " | Total stats: " +  attributes["Total"] + " | HP: " + attributes["HP"] + " | Sp. Atk: " +  attributes["Sp. Atk"] + " | Attack: " +  attributes["Attack"] + " | Sp. Def: " +  attributes["Sp. Def"] + " | Defense: " +  attributes["Defense"] + " | Speed: " +  attributes["Speed"])

# team builder -----------------------------------------------------------------------------------------------

def pkm_teambuilder_add(pkm_list, team_list_provisional, team_list, added_pokemon):
    to_delete = []
    team_list_provisional = pkm_list.copy()

    if len(team_list) < 6:
        for id, attributes in pkm_list.items():
            if added_pokemon.lower() in attributes["Name"].lower():
                print("")
                print(f"Added {added_pokemon.capitalize()}.")
                print("")
                continue
            else:
                to_delete.append(id)

        for id in to_delete:
            team_list_provisional.pop(id)

        if len(team_list_provisional) == 0:
            print("")
            print(f"{added_pokemon.capitalize()} does not exist in Paldea.")
            print("")

        team_list.update(team_list_provisional)

    else:
        print("")
        print("Team is full.")
        print("")

    return team_list

def pkm_teambuilder_remove(team_list, removed_pokemon):
    to_delete = []
    if len(team_list) != 0:
        for id, attributes in team_list.items():
            if removed_pokemon.lower() in attributes["Name"].lower():
                to_delete.append(id)

        for id in to_delete:
            team_list.pop(id)

        print("")
        print(f"Removed {removed_pokemon.capitalize()}.")
        print("")

    else:
        print("")
        print("There is no team yet.")
        print("")

    return team_list

def pkm_teambuilder_reset(team_list):
    team_list = {}

    return team_list

# total stats -----------------------------------------------------------------------------------------------

def pkm_total_stats(pkm_list, total):
    print("")
    print(f"Pokemon Total stats >= {total}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Total"]) < total:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)
    
    return pkm_list

# single stats -----------------------------------------------------------------------------------------------

def pkm_hp(pkm_list, hp):
    print("")
    print(f"Pokemon HP >= {hp}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["HP"]) < hp:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)
    
    return pkm_list

def pkm_attack(pkm_list, attack):
    print("")
    print(f"Pokemon Attack >= {attack}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Attack"]) < attack:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)
    
    return pkm_list

def pkm_spattack(pkm_list, spattack):
    print("")
    print(f"Pokemon Sp. Attack >= {spattack}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Sp. Atk"]) < spattack:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)
    
    return pkm_list
    
def pkm_defense(pkm_list, defense):
    print("")
    print(f"Pokemon Defense >= {defense}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Defense"]) < defense:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)
    
    return pkm_list

def pkm_spdefense(pkm_list, spdefense):
    print("")
    print(f"Pokemon Sp. Defense >= {spdefense}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Sp. Def"]) < spdefense:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)
    
    return pkm_list

def pkm_speed(pkm_list, speed):
    print("")
    print(f"Pokemon Speed >= {speed}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Speed"]) < speed:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)
    
    return pkm_list

# double stats -----------------------------------------------------------------------------------------------

def pkm_spatk_speed(pkm_list, spatk, speed):
    print("")
    print(f"Pokemon with Sp. Attack >= {spatk} and Speed >= {speed}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Sp. Atk"]) < spatk or int(attributes["Speed"]) < speed:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)

    return pkm_list

def pkm_atk_speed(pkm_list, attack, speed):
    print("")
    print(f"Pokemon with Attack >= {attack} and Speed >= {speed}: ")
    print("")

    to_delete=[]
    for id, attributes in pkm_list.items():
        if int(attributes["Attack"]) < attack and int(attributes["Speed"]) < speed:
            to_delete.append(id)

    for id in to_delete:
        pkm_list.pop(id)

    return pkm_list

def pkm_spdef_hp(pkm_list, spdef, hp):
    print("")
    print(f"Pokemon with Sp. Defense >= {spdef} and HP >= {hp}: ")
    print("")

    to_delete = []
    for id, attributes in unbanned_pokemon_list.items():
        if int(attributes["Sp. Def"]) < spdef and int(attributes["HP"]) < hp:
            to_delete.append(id)

    for id in to_delete:
        pkm_list.pop(id)

    return pkm_list

def pkm_def_hp(pkm_list, defense, hp):
    print("")
    print(f"Pokemon with Defense >= {defense} and HP >= {hp}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Defense"]) < defense and int(attributes["HP"]) < hp:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)

    return pkm_list

# types -----------------------------------------------------------------------------------------------

def pkm_type(pkm_list, type1):
    print("")
    print(f"Pokemon with type {type1}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if attributes["Type1"].lower() != type1.lower():
            to_delete.append(id)

    for id in to_delete:
        pkm_list.pop(id)

    return pkm_list

def pkm_types(pkm_list, type1, type2):
    print("")
    print(f"Pokemon with types {type1} {type2}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if attributes["Type1"].lower() != type1.lower() or attributes["Type2"].lower() != type2.lower():
            to_delete.append(id)

    for id in to_delete:
        pkm_list.pop(id)

    return pkm_list

# search -----------------------------------------------------------------------------------------------

def pkm_namefilter(pkm_list, name):
    print("")

    search_list = pkm_list.copy()

    to_delete = []
    for id, attributes in search_list.items():
        if name.lower() in attributes["Name"].lower():
            continue
        else:
            to_delete.append(id)

    for id in to_delete:
        search_list.pop(id)

    if len(search_list) > 0:
        for id, attributes in search_list.items():
            print(attributes["Name"] + " | Form: " + attributes["Form"] + " | Types: " + attributes["Type1"] + ", " + attributes["Type2"] + " | Total stats: " +  attributes["Total"] + " | HP: " + attributes["HP"] + " | Sp. Atk: " +  attributes["Sp. Atk"] + " | Attack: " +  attributes["Attack"] + " | Sp. Def: " +  attributes["Sp. Def"] + " | Defense: " +  attributes["Defense"] + " | Speed: " +  attributes["Speed"])

    else:
        print(f"{name.capitalize()} not found.")

    print("")

    return search_list

# end -----------------------------------------------------------------------------------------------

main()