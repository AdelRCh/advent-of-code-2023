'''Day One Solution - 2023 Advent Code'''

FILEPATH = 'day_one_input.txt'

def fix_spelled_numbers(txt: str) -> str:
    '''This function is used to solve Part 2 as a preprocessing function.'''
    
    corr_txt = txt
    
    dict_spell = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }

    positions = []

    #We want to find out which digit appears first:
    for num, digit in dict_spell.items():
        pos = corr_txt.find(num)
        
        if corr_txt.find(num) != -1:
            positions.append((pos,{num:digit}))

    #Sorting
    positions.sort(key=lambda x:x[0])

    #If we have any spelled number in our text, we tackle the first one, then recursively move on to the rest:
    if positions != []:
        pos_dict = positions[0][1]

        for num, digit in pos_dict.items():
            #After having several "wrong answers" due to the "oneight" scenario that should give 18,
            #I forced the following as a corrective measure: add the last character of a spelled digit.
            #that way, we'll be able to handle "oneight" as "oneeight"
            corr_txt = corr_txt.replace(num,digit+num[-1])
            
        #RECURSIVE HERE: because a spelled digit can reappear a little later, but still before another one.
        corr_txt = fix_spelled_numbers(corr_txt)

    return corr_txt

def solve_day_one(filepath=FILEPATH):
    '''We draft the solution for both parts.'''
    numbers = []
    numbers_two = []

    with open(filepath,'r') as my_file:
        #For each line in our file:
        for line in my_file:
            #We keep the digits for Part 1
            line_digits_part_one = ''.join([x for x in line if x.isdigit()])

            #We preprocess our lines, then extract the resulting digits for Part 2
            proc_line = fix_spelled_numbers(line)
            line_digits_part_two = ''.join([x for x in proc_line if x.isdigit()])
            
            #If there are digits in our resulting string, we apply our conversion.
            #Our string could be '7'; in this case, the resulting number needs to be 77.
            #Sometimes, we could have something like 12456, in which case 16 is our result.
            #Basically, I take the first and last digits (first x 10 + last). I'm doing this for both solutions.
            if line_digits_part_one != '':
                numbers.append(int(line_digits_part_one[0])*10 + int(line_digits_part_one[-1]))

            if line_digits_part_two != '':
                numbers_two.append(int(line_digits_part_two[0])*10 + int(line_digits_part_two[-1]))

    #Using a Tuple to return the solutions. (Part 1, Part 2)
    return (sum(numbers), sum(numbers_two))

if __name__ == '__main__':
    solutions = solve_day_one()
    print(f'''Day One solutions:
    - Part 1: {solutions[0]}
    - Part 2: {solutions[1]}''')