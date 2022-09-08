# Практические задания главы 6 «Функции»

## Задание 1

Напишите функцию, которая проверяет, является ли год високосным.

**Решение**


```python
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)


years = [2022, 1000, 1657, 1917, 2021, 2020]
for year in years:
    print(f"Год {year} {'високосный' if is_leap_year(year) else 'не високосный'}")
```

    Год 2022 не високосный
    Год 1000 не високосный
    Год 1657 не високосный
    Год 1917 не високосный
    Год 2021 не високосный
    Год 2020 високосный
    

## Задание 2

Напишите функцию `f(x)`, вовзращающую простые множители любого числа `x` (пример простых множителей: `36` - `[2 2 3 3]`, `30` - `[2 3 5]`).

**Решение**


```python
def f(x: int) -> list:
    factors = []
    d = 2
    
    while d * d <= x:
        if x % d == 0:
            factors.append(d)
            x //= d
        else:
            d += 1
    
    if x > 1:
        factors.append(x)
    
    return factors


print(f(36))
print(f(30))
print(f(63))
```

    [2, 2, 3, 3]
    [2, 3, 5]
    [3, 3, 7]
    

## Задание 3

Напишите функцию для преобразования температуры из градусов Цельсия в градусы Фаренгейта. Напишите еще одну функцию для обратного преобразования.

**Решение**


```python
from functools import wraps


def rounder(func):
    @wraps(func)
    def wrapper(degree, round_to=None):
        result = func(degree)
        
        if isinstance(round_to, int):
            return round(result, round_to)
        return result
    return wrapper


@rounder
def fahrenheit_to_celsius(degree, ):
    return (degree - 32) * (5 / 9)


@rounder
def celsius_to_fahrenheit(degree):
    return degree * (9 / 5) + 32


print(f"0 °C = {celsius_to_fahrenheit(0, 2)} °F")
print(f"0 °F = {fahrenheit_to_celsius(0, 2)} °C")
```

    0 °C = 32.0 °F
    0 °F = -17.78 °C
    

## Задание 4

Напишите функцию для вычисления факториала любого числа.

**Решение**


```python
def factorial(num: int) -> int:
    if num < 0:
        raise ValueError(f"число {num} должно быть больше или равно нулю")
    elif num in (0, 1):
        return 1
    
    result = 1
    for i in range(1, num + 1):
        result *= i
        
    return result


for i in range(11):
    print(factorial(i))
```

    1
    1
    2
    6
    24
    120
    720
    5040
    40320
    362880
    3628800
    

## Задание 5

Напишите функцию преобразования любого числа от 1 до 100 в римское число.

**Решение**


```python
def arabic_to_roman_1_100(num: int) -> str:
    if num < 1 or num > 100:
        raise ValueError(f"число {num} должно быть в диапазоне от 1 до 100 включительно")
        
    # единицы
    digit_num_1 = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    # десятки
    digit_num_10 = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    # сотни
    digit_num_100 = ["C"]
    
    romans = {1: digit_num_1, 10: digit_num_10, 100: digit_num_100}
    
    roman = ""
    i = 1
    while num:
        digit, num = num % 10, num // 10
        
        if digit > 0:
            roman = romans[i][digit - 1] + roman
        
        i *= 10
        
    return roman


for i in range(1, 101):
    print(arabic_to_roman_1_100(i), end=" " * 3)
```

    I   II   III   IV   V   VI   VII   VIII   IX   X   XI   XII   XIII   XIV   XV   XVI   XVII   XVIII   XIX   XX   XXI   XXII   XXIII   XXIV   XXV   XXVI   XXVII   XXVIII   XXIX   XXX   XXXI   XXXII   XXXIII   XXXIV   XXXV   XXXVI   XXXVII   XXXVIII   XXXIX   XL   XLI   XLII   XLIII   XLIV   XLV   XLVI   XLVII   XLVIII   XLIX   L   LI   LII   LIII   LIV   LV   LVI   LVII   LVIII   LIX   LX   LXI   LXII   LXIII   LXIV   LXV   LXVI   LXVII   LXVIII   LXIX   LXX   LXXI   LXXII   LXXIII   LXXIV   LXXV   LXXVI   LXXVII   LXXVIII   LXXIX   LXXX   LXXXI   LXXXII   LXXXIII   LXXXIV   LXXXV   LXXXVI   LXXXVII   LXXXVIII   LXXXIX   XC   XCI   XCII   XCIII   XCIV   XCV   XCVI   XCVII   XCVIII   XCIX   C   

## Задание 6

Напишите функцию `f(x)`, которая возвращает таблицу умножения числа `x`.

**Решение**


```python
def mulpiple_table(num: int) -> str:
    if num < 2 or num > 9:
        raise ValueError("Таблица умножения строится только для чисел в диапазоне [2; 9]")

    table = ""
    for i in range(2, 10):
        if i != 2:
            table += "\n"
        table += f"{num} * {i} = {num * i}"
        
    return table


print(mulpiple_table(9))
```

    9 * 2 = 18
    9 * 3 = 27
    9 * 4 = 36
    9 * 5 = 45
    9 * 6 = 54
    9 * 7 = 63
    9 * 8 = 72
    9 * 9 = 81
    

## Задание 7

Напишите функцию, которая принимает в качестве входных данных список и возвращает его перевернутый вариант.

**Решение**


```python
def reverse_list(lst: list) -> list:
    return list(reversed(lst))


lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst)
print(reverse_list(lst))
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    

## Задание 8

Напишите функцию для расчета сложных процентов.

**Решение**


```python
def calc_hard_percent(x: float, s: float, m: int) -> float:
    """
    Формула:
    
    x * (1 + (s / (12 * 100)))^m
    
    где x - начальная сумма вклада, s - годовая ставка в процентах, m - срок вклада в месяцах.
    """
    return round(x * (1 + (s / (12 * 100))) ** m, 2)


print(calc_hard_percent(20000, 6.5, 6 * 12))
```

    29508.54
    

## Задание 9

Напишите функцию `f(x)`, где `x` - любое 6-значное число, а функция возвращает сумму его цифр.

**Решение**


```python
def digit_sum(num: int) -> int:
    if num == 0:
        return num
    
    sum_ = 0
    while num:
        digit, num = num % 10, num // 10
        sum_ += digit
        
    return sum_


print(digit_sum(0))
print(digit_sum(5))
print(digit_sum(15))
print(digit_sum(343))
print(digit_sum(3534))
print(digit_sum(57848))
```

    0
    5
    6
    10
    15
    32
    

## Задание 10

Напишите функцию, которая проверяет, является ли переданное число простым.

**Решение**


```python
def is_simple_num(num: int) -> bool:
    deviders = 0
    for i in range(1, num + 1):
        if num % i == 0:
            deviders += 1

    return deviders == 2


for i in range(1, 30):
    print(f"{i} {'простое' if is_simple_num(i) else 'не простое'} число")
```

    1 не простое число
    2 простое число
    3 простое число
    4 не простое число
    5 простое число
    6 не простое число
    7 простое число
    8 не простое число
    9 не простое число
    10 не простое число
    11 простое число
    12 не простое число
    13 простое число
    14 не простое число
    15 не простое число
    16 не простое число
    17 простое число
    18 не простое число
    19 простое число
    20 не простое число
    21 не простое число
    22 не простое число
    23 простое число
    24 не простое число
    25 не простое число
    26 не простое число
    27 не простое число
    28 не простое число
    29 простое число
    
