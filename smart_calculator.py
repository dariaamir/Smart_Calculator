# write your code here
def clean_input(line):
    while '--' in line:
        line = line.replace('--', '+')
    while '--' in line:
        line = line.replace('++', '+')
    line = line.replace(' ', '')
    line = line.replace('+', ' ')
    line = line.replace('-', ' -')
    return line

def smart_calculator():
    i = input()
    while i != '/exit':
        if i != '':
            if i == '/help':
                print('The program calculates the sum of numbers')
            else:
                i = clean_input(i)
                data_i = [int(x) for x in i.split()]
                print(sum(data_i))
        i = input()

    print('Bye!')

smart_calculator()