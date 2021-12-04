def part_1():
    one_counter = [0]*12
    line_counter = 0
    linelist = []
    with open('input.txt', 'r') as f:
        for line in f:
            line_counter, one_counter = pretty_little_helper_function(line, linelist, one_counter, line_counter)
    gamma_rate = ''
    epsilon_rate = ''
    line_counter = line_counter/2
    for character in one_counter:
        if character >= line_counter:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'    
    print(one_counter)
    print(gamma_rate)
    print(epsilon_rate)
    print(int(epsilon_rate, 2)*int(gamma_rate,2))
    return linelist

def pretty_little_helper_function(line, linelist, one_counter, line_counter):
    """Useless helper function"""
    char_list = [int(character) for character in line.split('\n')[0]]
    one_counter = [one_counter[x] + char_list[x] for x in range(len(one_counter))]
    line_counter += 1
    linelist.append(char_list)
    return line_counter, one_counter


def pretty_little_helper_function_2(line, linelist, one_counter, line_counter):
    """That feel when you thought a secondary function would help but no, your brain was doing too many things at once"""
    one_counter = [one_counter[x] + line[x] for x in range(len(one_counter))]
    line_counter += 1
    linelist.append(line)
    return line_counter, one_counter

def part_2(input_list):
    """So I misinterpreted the task hence this absolute mess of a code."""
    oxygen_generator = []
    temp_list = input_list.copy()
    counter = 0
    #why do modularity amirite xP
    while len(temp_list) != 1 and counter < 12:
        temp_list_2 = []
        one_counter = [0]*12
        line_counter = 0
        linelist = []
        #print(temp_list)
        for a in temp_list:
            line_counter, one_counter = pretty_little_helper_function_2(temp_list[line_counter], linelist, one_counter, line_counter)
        most_common = 1 if len(temp_list)/2 <= one_counter[counter] else 0
        print(temp_list)
        for a in temp_list:
            if a[counter] == most_common:
                temp_list_2.append(a)
        counter += 1
        if temp_list_2 is not None:
                temp_list = temp_list_2
    oxygen_generator = temp_list[0].copy()
    print(oxygen_generator)

    co2_scrubber = []
    temp_list = input_list.copy()
    counter = 0
    while len(temp_list) != 1 and counter < 12:
        temp_list_2 = []
        one_counter = [0]*12
        line_counter = 0
        linelist = []
        #print(temp_list)
        for a in temp_list:
            line_counter, one_counter = pretty_little_helper_function_2(temp_list[line_counter], linelist, one_counter, line_counter)
        most_common = 0 if len(temp_list)/2 <= one_counter[counter] else 1
        print(temp_list)
        for a in temp_list:
            if a[counter] == most_common:
                temp_list_2.append(a)
        counter += 1
        if temp_list_2 is not None:
                temp_list = temp_list_2
    co2_scrubber = temp_list[0].copy()

    print(co2_scrubber)

    o2 = ''
    co2 = ''
    for character in oxygen_generator:
        o2 += str(character)
    for character in co2_scrubber:
        co2 += str(character)
    #oh well I don't give a fuck any more. This was terrible xD
    print(int(o2,2)*int(co2,2))
    
    
        
                

if __name__ == '__main__':
    part_2(part_1())

    