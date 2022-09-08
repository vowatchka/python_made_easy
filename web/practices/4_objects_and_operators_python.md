# Практические задания главы 4 «Объекты и операторы в Python»

## Задание 1

Питер получает зарплату 12 000 в месяц. Напишите код для вычисления его сбережений к концу года, если он будет откладывать 20% своей зарплаты каждый месяц.

**Решение**


```python
salary = 12_000
saving_percents_per_month = 20
months_in_year = 12

saving_total = salary * saving_percents_per_month * 0.01 * months_in_year
print(saving_total)
```

    28800.0
    

## Задание 2

Расстояние между Мумбаи и Дели составляет 1422 км. Если Сундар едет на машине со средней скоростью 72 км/ч, сколько времени ему потребуется, чтобы преодолеть это расстояние.

**Решение**


```python
l = 1_422  # км 
v = 72  # км/ч

t = l / v
print(t)
```

    19.75
    

## Задание 3

Температура тела человека находится в диапазоне от 97 до 99 градусов по Фаренгейту. Как этот диапазон будет выглядеть в градусах Цельсия.

**Решение**


```python
def fahrenheit_to_celsius(degree):
    return (degree - 32) * (5 / 9)

human_degree_range_fahrenheit = (97, 99)
human_degree_range_celsius = ()

for degree in human_degree_range_fahrenheit:
    human_degree_range_celsius += (fahrenheit_to_celsius(degree),)
    
print(human_degree_range_celsius)
```

    (36.111111111111114, 37.22222222222222)
    

## Задание 4

Пусть дано шестизначное число. Напишите программу для вычисления суммы всех цифр этого числа.

**Решение**


```python
number = 123456
digits_sum = sum(int(x) for x in str(number))
print(digits_sum)
```

    21
    

## Задание 5

У нас есть данные о месячных продажах 5-ти книжных магазинов в Бруклине:

A = 6500, B = 8000, C = 12 000, D = 4900 и E = 5600.

Предполагая, что в Бруклине всего 5 книжных магазинов, узнайте рыночную долю каждого магазина. Также проверьте, какой будет сумма рыночных долей всех магазинов. (Рыночная доля означает отношение одного участника ко всем остальным.)

**Решение**


```python
def calc_market_share(concrete, others):
    return concrete / sum(others)
    
markets = dict(zip("ABCDE", [6_500, 8_000, 12_000, 4_900, 5_600]))
market_shares = {k: calc_market_share(v, [val for key, val in markets.items() if key != k]) for k, v in markets.items()}

for k, v in market_shares.items():
    print(f"{k} market share is {v}")
    
market_shares_sum = sum(v for v in market_shares.values())
print(f"market shares sum is {market_shares_sum}")
```

    A market share is 0.21311475409836064
    B market share is 0.27586206896551724
    C market share is 0.48
    D market share is 0.1526479750778816
    E market share is 0.17834394904458598
    market shares sum is 1.2999687471863455
    

## Задание 6

Среднее значение 3-х чисел равно 45. Первое число больше среднего значения настолько же, насколько второе число меньше среднего значения. Найдите третье число.

**Решение**


```python
def find_numbers(agv):
    num_sum = agv * 3
    
    for x in range(num_sum + 1):
        for y in range(num_sum + 1):
            for z in range(num_sum + 1):
                if x > agv and y < agv and x - agv == agv - y and (x + y + z) // 3 == agv:
                    return x, y, z
    else:
        return (None,) * 3
    
print(find_numbers(45))
```

    (46, 44, 45)
    

## Задание 7

Джон покупает мобильный телефон за 1800 в Калькутте и продает его в Мумбаи с прибылью 25%. Если его накладные расходы составляют 5% от цены продажи, то какова цена продажи?

**Решение**


```python
buy_price = 1_800
sale_profit = 25 * 0.01
sale_costs = 5 * 0.01

sale_price = (buy_price + buy_price * sale_profit) / (1 - sale_costs)
print(sale_price)
```

    2368.421052631579
    

## Задание 8

Найдите объем и площадь куба с диагональю 5 м.

Подсказка: $V = \frac{d^3}{3\sqrt{3}}$, $S = 2d^2$

**Решение**


```python
d = 5  # метров

v = d ** 3 / (3 * 3 ** 0.5)
s = 2 * d ** 2

print(f"V = {v}")
print(f"S = {s}")
```

    V = 24.056261216234407
    S = 50
    

## Задание 9

Три металлических куба с ребрами длиной 3, 4 и 5 см соответственно переплавляются в один куб. Найдите длину ребра нового куба.

**Решение**


```python
a1 = 3
a2 = 4
a3 = 5

a_new = (a1 ** 3 + a2 ** 3 + a3 ** 3) ** (1 / 3)
print(a_new)
```

    5.999999999999999
    

## Задание 10

Дано шестизначное число. Напишите программу для получения числа с обратным порядком цифр.

**Решение**


```python
x = 123456
x_reversed = int("".join(reversed(str(x))))

print(x_reversed)
```

    654321
    
