'''Day 2 - Advent of Code solution'''

import re

#File name where I stored my inputs. Feel free to change the file name if you did something differently.
FILENAME = 'day_two_input.txt'

#For Part 1, the elf gave us upper limits, and they are as follows:
MAX_VALUES = {
    "blue":14,
    "green":13,
    "red":12
}


def solve_day_two(filename=FILENAME,max_v=MAX_VALUES):
    '''We will solve both problems in one fell swoop. The default inputs work on their own.
    The output will be a tuple with the format (Part 1 Solution, Part 2 Solution).
    The items inside the Tuples are integers.'''

    #Pay attention to (\d*) for your notation.
    blue_re = r"(\d*) blue"
    red_re = r"(\d*) red"
    green_re = r"(\d*) green"

    #Storing viable game IDs in this list:
    id_list = []

    #Storing the "powers" in Part 2 in this variable:
    power_cubes = []
    
    with open(filename) as file:

        for line in file:
            #Extracting the Game ID is fast via split() and replace()
            game_id = int(line.split(':')[0].replace('Game ',''))

            #That said, the game's rolls will take some tinkering. We will initialize them at 0.
            #If a dice variety isn't showcased throughout all rounds, the game remains valid.
            game_session_str = line.split(':')[1]
            blue_high = 0
            red_high = 0
            green_high = 0

            #Now, we will extract all blue, green and red cube rolls indiscriminately.
            blue_se = [int(x) for x in re.findall(blue_re, game_session_str)]
            red_se = [int(x) for x in re.findall(red_re, game_session_str)]
            green_se = [int(x) for x in re.findall(green_re, game_session_str)]

            #What matters to us is that, for any game, we don't cross the maximum (Part 1).
            #As for Part 2... we need the maximum value. Two birds, one stone.
            if blue_se != []:
                blue_high = max(blue_se)
            
            if red_se != []:
                red_high = max(red_se)
            
            if green_se != []:
                green_high = max(green_se)
    
            #The elf clearly asks for *any* game in Part 2. Not only valid games.
            power_cubes.append(blue_high*red_high*green_high)
    
            #For Part 1, however, he wanted the game to conform to our max values.
            if (blue_high <= max_v['blue']) and (red_high <= max_v['red']) and (green_high <= max_v['green']):
                id_list.append(game_id)

    #And so it goes.
    return (sum(id_list),sum(power_cubes))

if __name__=='__main__':
    solutions = solve_day_two()
    print(f'''Solutions:
    - Part 1: {solutions[0]}
    - Part 2: {solutions[1]}''')

            
            