#!/usr/bin/env python3


def long_division(dividend, divider):
    '''
    Вернуть строку с процедурой деления «уголком» чисел dividend и divider.
    Формат вывода приведён на примерах ниже.

    Примеры:
    >>> 12345÷25
    12345|25
    100  |493
    234
    225
    95
    75
    20

    >>> 1234÷1423
    1234|1423
    1234|0

    >>> 24600÷123
    24600|123
    246  |200
      0

    >>> 246001÷123
    246001|123
    246   |2000
         1
    '''
    #INSERT CODE HERE
def long_division(dividend, divider):
    quotient = dividend // divider
    remainder = dividend % divider
    probel = " " * (len(str(dividend)))

    if divider == 0:
        result = "Делить на 0 нельзя"
    elif dividend == 0:
        result = f"{dividend}|{divider}\n |0"
    elif divider > dividend:
        result = f" {dividend}|{divider}\n‾{dividend}|0\n{probel}0"
    elif dividend == divider:
        result = f" {dividend}|{divider}\n‾{dividend}|1\n{probel}0"
    else:
        number = (divider * int(str(quotient)[0]))
        probel2 = " " * (len(str(dividend)) - len(str(number)))
        result = f" {dividend}|{divider}\n‾{number}{probel2}|{quotient}\n"#{probel}{remainder}\n
        for i in range(0,len(str(dividend))-1):
            digit = int(str(quotient)[i]) if i < len(str(quotient)) else 0
            number = (divider * digit) if i < len(str(quotient)) else (remainder * 10)
            if i == 0:
                number_2 = ((int(str(dividend)[i:len(str(number))+i])-number) * 10 + int(str(dividend)[len(str(number))-1:len(str(number))]))
            else:
                number_2 = (number_2 - number) * 10 + int(str(dividend)[len(str(number))-1:len(str(number))])
            # print("1:",number_2, "- number= ",number)
            # print("@2",number_2)
            # print(i)
            result += f"{probel2} {number_2}\n{probel2}‾{number}\n"
        return result
    return result

def main():
    print(long_division(123, 123))
    print()
    print(long_division(1, 1))
    print()
    print(long_division(15, 3))
    print()
    print(long_division(3, 15))
    print()
    print(long_division(12345, 25))
    print()
    print(long_division(1234, 1423))
    print()
    print(long_division(87654532, 1))
    print()
    print(long_division(24600, 123))
    print()
    print(long_division(4567, 1234567))
    print()
    print(long_division(246001, 123))
    print()
    print(long_division(100000, 50))
    print()
    print(long_division(123456789, 531))
    print()
    print(long_division(425934261694251, 12345678))
    input("Press any key to exit...")


if __name__ == '__main__':
    main()
    
