# Прикрутить бота к задачам с предыдущего семинара:
# a. Создать калькулятор для работы с рациональными и
# комплексными числами, организовать меню, 
# добавив в неё систему логирования

def racio_sum(x, y):
    return (f'{x} + {y} = {float(x + y)}')

def racio_sub(x, y):
    return (f'{x} - {y} = {float(x - y)}')

def racio_mult(x, y):
    return (f'{x} * {y} = {float(x * y)}')

def racio_div(x, y):
    return (f'{x} / {y} = {float(x / y)}')


def complex_method(command, z1, z2):
    array = z1.split()
    actual_part = int(array[0])
    sign = array[1]
    imaginary_part_digit = []
    imaginary_part_symbol = '' 
    
    for char in array[2]:
        if char.isdigit():
            imaginary_part_digit.append(char)
        elif char == '-':
            imaginary_part_digit.append(char)
        elif char == '(' or char == ')':
            continue
        else:
            imaginary_part_symbol = imaginary_part_symbol + char

    if len(imaginary_part_digit) != 0: 
        imaginary_part_digit = int(''.join(imaginary_part_digit))
        if imaginary_part_digit < 0 and sign == '-':
            imaginary_part_digit = abs(imaginary_part_digit)
        elif imaginary_part_digit > 0 and sign == '-':
            imaginary_part_digit *= -1
    else:
        imaginary_part_digit.append(sign)
        imaginary_part_digit.append('1')
        imaginary_part_digit = int(''.join(imaginary_part_digit))

    array2 = z2.split()
    actual_part2 = int(array2[0])
    sign2 = array2[1]
    imaginary_part_digit2 = []
    imaginary_part_symbol2 = '' 
    for char in array2[2]:
        if char.isdigit():
            imaginary_part_digit2.append(char)
        elif char == '-':
            imaginary_part_digit2.append(char)
        elif char == '(' or char == ')':
            continue
        else:
            imaginary_part_symbol2 = imaginary_part_symbol2 + char

    if len(imaginary_part_digit2) != 0:
        imaginary_part_digit2 = int(''.join(imaginary_part_digit2))
        if imaginary_part_digit2 < 0 and sign2 == '-':
            imaginary_part_digit2 = abs(imaginary_part_digit2)
        elif imaginary_part_digit2 > 0 and sign2 == '-':
            imaginary_part_digit2 *= -1
    else:
        imaginary_part_digit2.append(sign2)
        imaginary_part_digit2.append('1')
        imaginary_part_digit2 = int(''.join(imaginary_part_digit2))
    
    match command:
        case '/complex_sum':
            return (f'result: ({z1}) + ({z2}) = {actual_part + actual_part2} {sign2} {abs(imaginary_part_digit + imaginary_part_digit2)}{imaginary_part_symbol}')
    # result: (3 + 0i) + (1 + 5i) = 4 + 5i
        case '/complex_sub':
            return (f'result: ({z1}) - ({z2}) = {actual_part - actual_part2} + {abs(imaginary_part_digit - imaginary_part_digit2)}{imaginary_part_symbol}')
    # result: (3 + 2i) - (1 - 2i) = 2 + 4i
    # result: (3 + 9i) - (0 - 7i) = 3 + 16i
        case '/complex_mult':
            return (f'result: ({z1}) * ({z2}) = {(actual_part * actual_part2) - (imaginary_part_digit * imaginary_part_digit2)} + {abs((actual_part * imaginary_part_digit2) + (imaginary_part_digit * actual_part2))}{imaginary_part_symbol}')
    # result: (2 + 3i) * (5 - 7i) = 31 + 1i
    # result: (1 - i) * (3 + 6i) = 9 + 3i
        case '/complex_div':
            return (f'result: ({z1}) / ({z2}) = {(actual_part * actual_part2) + (imaginary_part_digit * imaginary_part_digit2)}/{(actual_part2**2 + imaginary_part_digit2**2)} + {(actual_part2 * imaginary_part_digit) - (actual_part * imaginary_part_digit2)}/{(actual_part2 ** 2 + imaginary_part_digit2 ** 2)}{imaginary_part_symbol}')
    # result: (3 + 4i) / (4 + 5i) = 32/41 + 1/41i
    
