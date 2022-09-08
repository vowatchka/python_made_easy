# Практические задания главы 12 «Ошибки и обработка исключений»

## Задание 1

Напишите функцию с именем `oops()`, которая явно вызывает исключение `IndexError` при вызове. Затем напишите другую функцию, которая вызывает `oops()` внутри конструкции `try-except` и перехватывает ошибку. Что произойдет, если в функции `oops()` вместо `IndexError` будет вызываться `KeyError`.

**Решение**


```python
def oops():
    raise IndexError
    
    
def good():
    try:
        oops()
    except IndexError:
        print("good")
        
        
good()
```

    good
    

## Задание 2

Напишите функцию нахождения среднего значения списка чисел. Ваша функция должна иметь возможность обрабатывать пустой список, а также список, содержащий строку.

**Решение**


```python
from typing import List, Union


def avg(iterable: List[Union[int, float, str]]) -> float:
    if not iterable:
        raise ValueError("для вычисления среднего значения нужно хотя бы одно число")
        
    sum_: float = 0
    for item in iterable:
        if isinstance(item, str):
            try:
                sum_ += int(item)
            except ValueError:
                sum_ += float(item)
        else:
            sum_ += item
            
    return sum_ / len(iterable)


try:
    avg([])
except ValueError:
    print("Исключение при пустом списке обработано")
    
lst = [1, 2, 3.4, 5.6, "7.8", "9"]
result = avg(lst)
print(f"Среднее значени для списка {lst}: {result}")
```

    Исключение при пустом списке обработано
    Среднее значени для списка [1, 2, 3.4, 5.6, '7.8', '9']: 4.8
    

## Задание 3

Напишите программу, принимающую дату от пользователя в виде дня, месяца и года и вызывающую соответствующие ошибки, если передано недопустимое значение. Выводите сообщения об ошибке, пока пользователь не введет правильные значения.

**Решение**


```python
def get_year():
    year = int(input("Введите год: "))
    if year < 0:
        raise ValueError("Год не может быть отрицательным")
    return year
        

def get_month():
    month = int(input("Введите месяц: "))
    if month <= 0:
        raise ValueError("Месяц не может быть отрицательным или равным нулю")
    if month > 12:
        raise ValueError("Месяц должен быть в диапазоне 1-12")
    return month
    
    
def get_day(month: int):
    day = int(input("Введите день: "))
    if day <= 0:
        raise ValueError("День не может быть отрицательным или равным нулю")
    if month not in range(1, 13):
        raise ValueError(f"Неизвестный месяц {month}")
    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        raise ValueError(f"Для месяца {month} день должен быть в диапазоне 1-31")
    elif month in [4, 6, 9, 11] and day > 30:
        raise ValueError(f"Для месяца {month} день должен быть в диапазоне 1-30")
    elif month == 2 and day > 28:
        raise ValueError(f"Для месяца 2 день должен быть в диапазоне 1-28")
    return day


def main():
    year, month, day = None, None, None
    while not year or not month or not day:
        if not year:
            try:
                year = get_year()
            except ValueError as ex:
                print(ex)
                continue
            
        if not month:
            try:
                month = get_month()
            except ValueError as ex:
                print(ex)
                continue
            
        if not day:
            try:
                day = get_day(month)
            except ValueError as ex:
                print(ex)
                continue
            
    print(f"Дата: {day:02}.{month:02}.{year:04}")
    
    
main()        
```

    Введите год: -1
    Год не может быть отрицательным
    Введите год: 2022
    Введите месяц: -1
    Месяц не может быть отрицательным или равным нулю
    Введите месяц: 0
    Месяц не может быть отрицательным или равным нулю
    Введите месяц: 14
    Месяц должен быть в диапазоне 1-12
    Введите месяц: 9
    Введите день: -1
    День не может быть отрицательным или равным нулю
    Введите день: 0
    День не может быть отрицательным или равным нулю
    Введите день: 32
    Для месяца 9 день должен быть в диапазоне 1-30
    Введите день: 6
    Дата: 06.09.2022
    

## Задание 4

Создайте класс `Person` для хранения личной информации (по вашему выбору) о человеке. Убедитесь, что ввод некорректных данных обрабатывается должным образом.

**Решение**


```python
class Person:
    def __init__(self, name: str, age: int):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        elif not name:
            raise ValueError("Имя не может быть пустым")
        self.name = name
        
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        self.age = age
        
    def __str__(self):
        return f"Имя: {self.name}, возраст: {self.age}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.age})"
        
        
def main():
    try:
        person = Person(name=123, age=31)
    except TypeError as ex:
        print(ex)
        
    try:
        person = Person(name="", age=31)
    except ValueError as ex:
        print(ex)
        
    try:
        person = Person(name="Владимир", age="31")
    except TypeError as ex:
        print(ex)
        
    person = Person(name="Владимир", age=31)
    print(person)
    print(f"{person!r}")


main()
```

    Имя должно быть строкой
    Имя не может быть пустым
    Возраст должен быть целым числом
    Имя: Владимир, возраст: 31
    Person('Владимир', 31)
    
