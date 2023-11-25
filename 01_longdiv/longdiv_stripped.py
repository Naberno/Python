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
    number = list(map(int, str(dividend)))
    result = f" _{dividend}│{divider}\n"
    lenofdig = " " * len(number)
    answ = dividend // divider
    result += f"{lenofdig}  │{answ}\r"

    reminder = probel = 0
    while number:
        reminder = reminder * 10 + number.pop(0)
        if reminder >= divider:
            if probel:
                result += f"{'':<{probel}} _{reminder}\n"
            l = len(str(reminder))
            integer, reminder = divmod(reminder, divider)
            result += f"{'':<{probel}}  {integer * divider:>{l}}\n"
            probel += l - len(str(reminder)) + (0 if reminder else 1)
    
    result += f"{'':<{len(str(dividend))-len(str(reminder))}}  {reminder}"
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

if __name__ == '__main__':
    main()