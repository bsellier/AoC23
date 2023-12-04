from typing import List, Dict

Constraint = Dict[str, int]
Game = List[Constraint]


def is_game_possible(constraint, game: Game):
    for s in game:
        for k, v in s.items():
            print(f"type de v : {type(v)}, type de constraint[k]: {type(constraint[k])}")
            if int(v) > constraint[k]:
                return False

    return True

def read_input(f_name: str = 'input'):
    with open(f_name) as file:
        return file.read()

def game_to_dict(txt_game):
    print('----------------')
    first_column = txt_game.find(':')
    index = txt_game[5:first_column]
    print(txt_game)
    print(f"game index :{index}")
    colors = txt_game[first_column+1:]
    sets = colors.split(";")
    sets_list = sets_to_dict(sets)
    return [index, sets_list]

def sets_to_dict(sets):
    s_dict_list = []
    for s in sets:
        loljsp = s.split(',')
        print('--')
        print(s)
        s_dict = {}
        for x in loljsp:
            if x[0] == ' ':
                x = x[1:]
            [n, col] = x.split(' ')
            print(f'{col}: {n}')
            s_dict[col] = n
        s_dict_list.append(s_dict)
        print(s_dict_list)

    return s_dict_list

def txt_to_dict(txt):
    games = txt.split('\n')
    del games[len(games)-1]
    games_dict = {}
    for g in games:
       (index, sets_list) = game_to_dict(g)
       games_dict[index] = sets_list
    
    return games_dict
def main():
    txt = read_input()
    constraint = {'red': 12, 'green': 13, 'blue': 14}
    g_dict = txt_to_dict(txt)
    index_sum = 0 
    for k, v in g_dict.items():
        print(f'Game {k}:')
        print(v)
        if is_game_possible(constraint, v):
            print(f"possible à l'index {k}")
            index_sum += int(k)
    print(index_sum)

        
if __name__ == "__main__":
    main()
