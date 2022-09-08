# Практические задания главы 11 «Классы»

## Задание 1

Рассмотрим следующее определение класса:

```python
class Yourclass:
    marks = 10
    name = "ABC"
    
    def __init__(self, marks, name):
        self.marks = marks
        self.name = name
        
    def display(self):
        print(self.marks)
        print(self.name)
```

Напишите команду для создания объекта класса `Yourclass`.

**Решение**


```python
class Yourclass:
    marks = 10
    name = "ABC"

    def __init__(self, marks, name):
        self.marks = marks
        self.name = name

    def display(self):
        print(self.marks)
        print(self.name)
        
        
inst = Yourclass(5, "Владимир")
inst.display()
```

    5
    Владимир
    

## Задание 2

Напишите класс с именем `Rectangle`, состоящий из длины и ширины, и метода, который будет вычислять площать прямоугольника.

**Решение**


```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.width}, {self.height})"
    
    
rect = Rectangle(10, 5)
print(f"Площадь прямоугольника: {rect.area()}")
```

    Площадь прямоугольника: 50
    

## Задание 3

Напишите класс, который имеет два метода `get_string()` и `print_string()`. Метод `get_string()` принимает строку от пользователя, а `print_string()` выводит строку в верхнем регистре.

**Решение**


```python
class Stringer:
    def __init__(self):
        self._str = ""
        
    def get_string(self):
        self._str = input("Введите любую строку: ")
        
    def print_string(self):
        print(self._str.upper())
        
        
stringer = Stringer()
stringer.get_string()
stringer.print_string()
```

    Введите любую строку: hello world
    HELLO WORLD
    

## Задание 4

Напишите класс, который меняет порядок слов в строке. Строка `"hello world"` превращается в `"world hello"`.

**Решение**


```python
class Reverser:
    def reverse_words(self, str_: str):
        return " ".join(list(reversed(str_.split())))
    
    
reverser = Reverser()
str_ = "hello world"
reversed_str = reverser.reverse_words(str_)

print(f"Строка {str_!r} в обратном порядке {reversed_str!r}")
```

    Строка 'hello world' в обратном порядке 'world hello'
    

## Задание 5

Напишите класс для преобразования целого числа в римские цифры.

**Решение**


```python
class RomanDigit:
    @staticmethod
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
    print(RomanDigit.arabic_to_roman_1_100(i), end=" " * 3)
```

    I   II   III   IV   V   VI   VII   VIII   IX   X   XI   XII   XIII   XIV   XV   XVI   XVII   XVIII   XIX   XX   XXI   XXII   XXIII   XXIV   XXV   XXVI   XXVII   XXVIII   XXIX   XXX   XXXI   XXXII   XXXIII   XXXIV   XXXV   XXXVI   XXXVII   XXXVIII   XXXIX   XL   XLI   XLII   XLIII   XLIV   XLV   XLVI   XLVII   XLVIII   XLIX   L   LI   LII   LIII   LIV   LV   LVI   LVII   LVIII   LIX   LX   LXI   LXII   LXIII   LXIV   LXV   LXVI   LXVII   LXVIII   LXIX   LXX   LXXI   LXXII   LXXIII   LXXIV   LXXV   LXXVI   LXXVII   LXXVIII   LXXIX   LXXX   LXXXI   LXXXII   LXXXIII   LXXXIV   LXXXV   LXXXVI   LXXXVII   LXXXVIII   LXXXIX   XC   XCI   XCII   XCIII   XCIV   XCV   XCVI   XCVII   XCVIII   XCIX   C   

## Задание 6

Определите класс с именем `Shape` (фигура) и его дочерний класс `Square` (квадрат). Класс `Square` имеет метод инициализации, который принимает в качестве аргумента сторону квадрата. Оба класса имеют метод вычисления площади, который может выводить площадь на экран. Площадь фигуры `Shape` по умолчанию равна 0.

**Решение**


```python
import abc


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass
    
    
class Square(Shape):
    def __init__(self, width):
        self.width = width
        
    def area(self):
        return self.width ** 2
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.width})"
    
    
square = Square(5)
print(f"Площадь квадрата: {square.area()}")
```

    Площадь квадрата: 25
    

## Задание 7

Определите класс `Student` с заданными характеристиками.

Атрибуты экземпляра:

* номер курса;
* имя.

Методы:

* `getdata()` - для получения номера курса и имени;
* `printdata()` - для вывода номера курса и имени.

**Решение**


```python
class Student:
    def __init__(self):
        self._name = ""
        self._course_num = 1
        
    def getdata(self, name: str, course_num: int):
        self._name, self._course_num = name, course_num
    
    def printdata(self):
        print(f"Студент {self._name} учится на {self._course_num} курсе")
        
        
vasya = Student()
vasya.getdata("Вася", 3)
vasya.printdata()
```

    Студент Вася учится на 3 курсе
    

## Задание 8

Определите класс `Marks`, производный от класса `Student`.

Переменная экземпляра:

* Оценки по пяти предметам.

Методы:

* `inputdata()` - вызов `getdata()` и ввод 5 оценок;
* `outdata()` - вызов `printdata()` и отображение 5 оценок.

Реализуйте классы на Python.

**Решение**


```python
class Marks(Student):
    def __init__(self):
        super().__init__()
        
        self._marks = []
        
    def inputdata(self):
        super().getdata(
            input("Введите имя студента: "),
            int(input("Введите номер курса студента: "))
        )
        self._marks = input("Введите 5 оценок студента через пробел: ").split()
        
    def outdata(self):
        super().printdata()
        print("И имеет оценки: {}".format(", ".join(self._marks)))


marks = Marks()
marks.inputdata()
print()
marks.outdata()
```

    Введите имя студента: Петя
    Введите номер курса студента: 2
    Введите 5 оценок студента через пробел: 3 4 4 5 5
    
    Студент Петя учится на 2 курсе
    И имеет оценки: 3, 4, 4, 5, 5
    

## Задание 9

Гостиница `XYZ` предлагает проживание, питание.

* Создайте класс `Accomodation` с номером комнаты, типом комнаты, ценой аренды и т.д.
* Создайте класс `Meal`, содержащий код обеда, название, цену и т.д.
* Создайте класс `Customer`, содержащий номер клиента, его имя, адрес и т.д.
* Класс `Customer` должен наследоваться от `Accomodation` и `Meal`.

**Решение**


```python
class Accomodation:
    def __init__(self, room_num: str, room_type: str, price: float):
        self.room_num = room_num
        self.room_type = room_type
        self.room_price = price
        
        
class Meal:
    def __init__(self, dean_code: str, name: str, price: float):
        self.dean_code = dean_code
        self.dean_name = name
        self.dean_price = price
        
        
class Customer(Accomodation, Meal):
    def __init__(self, client_num: str, name: str, address: str, 
                 room_num: str, room_type: str, room_price: float,
                 dean_code: str, dean_name: str, dean_price: float):
        self.client_num = client_num
        self.name = name
        self.address = address
        
        super(Customer, self).__init__(room_num, room_type, room_price)
        super(Accomodation, self).__init__(dean_code, dean_name, dean_price)
        
        
cust = Customer("123", "Вася", "г. Калуга", "1", "A", 1000, "dean123", "Обед", 200.50)
print("Клиент", cust.client_num, cust.name, cust.address)
print("Комната", cust.room_num, cust.room_type, cust.room_price)
print("Обед", cust.dean_code, cust.dean_name, cust.dean_price)
```

    Клиент 123 Вася г. Калуга
    Комната 1 A 1000
    Обед dean123 Обед 200.5
    
