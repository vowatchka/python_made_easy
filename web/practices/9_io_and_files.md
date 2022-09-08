# Практические задания главы 9 «Ввод-вывод данных и работа с файлами»

## Задание 1

Напишите код, который принимает число от пользователя, а возвращает квадрат введенного числа.

**Решение**


```python
num = int(input("Введите число: "))
print(f"{num} ** 2 = {num ** 2}")
```

    Введите число: 5
    5 ** 2 = 25
    

## Задание 2

Попросите у пользователя ввести его возраст в качестве входных данных. Вычтите его возраст из текущего года, чтобы узнать год рождения пользователя. Результат выведите в формате *«Я родился в ... году»*.

**Решение**


```python
from datetime import datetime


age = int(input("Введите свой возраст: "))
print(f"Ваш год рождения: {datetime.now().year - age}")
```

    Введите свой возраст: 31
    Ваш год рождения: 1991
    

## Задание 3

Напишите функцию, которая принимает три аргумента: входной файл, выходной файл и функцию преобразования. Первый аргумент - это файл, открытый для чтения, второй аргумент - это файл, открытый для записи, а третий аргумент - это функция преобразования, которая принимает строку на вход, выполняет какое-то преобразование по вашему выбору и возвращает измененную строку. Основная функция должна читать строку из входного файла, выполнять над ней функцию преобразования, а затем записывать измененную строку в выходной файл. Преобразование может быть, например, таким: каждое слово в строке должно начинаться с заглавной буквы.

**Решение**


```python
from typing import Callable


def f(in_file: str, out_file: str, conversion_func: Callable):
    with open(in_file, "r", encoding="utf-8") as f1:
        with open(out_file, "w", encoding="utf-8") as f2:
            for line in f1:
                f2.write(conversion_func(line))
                
                
f("files/1.txt", "files/2.txt", str.swapcase)
with open("files/2.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

    я ВИЖУ НА БОЛОТНЫХ КОЧКАХ
    оГРОМНЫХ ФОСФОРНЫХ СОБАК...
    сКАЖИТЕ, хОЛМС, А В ТРУБКЕ ТОЧНО
    тАБАК?
    
    

## Задание 4

Напишите функцию для создания текстового файла, содержащего следующие данные:

```
The 344-sq. km. the periphery of Navi Mimbai starts on the East with Kalundre village, on the West is the hill range that starts from Digha and runs up to Taloja; in the North is Digha village while Chanje village lies in the South, Dronagiri is on the South-East. The area comprised of 95 villages of Thane and Raigad Districts.
```

* Прочитайте все содержимое файла с помощью метода `read()` или `readlines()` и отобразите его на экране.
* Добавьте в файл любой текст на свое усмотрение и выведите содержимое файла с номерами строк.
* Выведите последнюю строку файла.
* Выведите первую строку, начиная с 10-го символа.
* Попросите пользователя указать номер строки из файла, которую нужно прочитать.

**Решение**


```python
def create_file(filename: str):
    """Создание текстового файла с заранее заготовленным содержимым"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(
            "The 344-sq. km. the periphery of Navi Mimbai starts on the East with Kalundre village, on"
            " the West is the hill range that starts from Digha and runs up to Taloja; in the North is"
            " Digha village while Chanje village lies in the South, Dronagiri is on the South-East. The"
            " area comprised of 95 villages of Thane and Raigad Districts."
        )
        
        
def print_content(filename: str):
    """Печать содержимого файла на экран"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
        

def add_content(filename: str, content: str):
    """Добавить любой контент в файл"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(content)
        

def print_content_with_numlines(filename: str):
    """Печать содержимого файла на экран c номерами строк"""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            print(f"{idx}: {line}", end="\n" if idx == len(lines) - 1 else "")
        
        
def print_last_line(filename: str):
    """Вывод последней строки файла"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.readlines()[-1])
        
    
def print_first_line(filename: str, start_from: int = 0):
    """Вывод первой строки файла, начиная с указанного символа"""
    with open(filename, "r", encoding="utf-8") as f:
        if start_from > 0:
            f.seek(start_from)
        print(f.readline())
        
        
def read_line(filename: str, numline: int):
    """Чтение указанной строки"""
    with open(filename, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            if idx + 1 == numline:
                print(line)
                break
                
                
create_file("files/file.txt")
print_content("files/file.txt")
print()

add_content("files/file.txt", " Fun!")
print_content_with_numlines("files/file.txt")
print()

print_last_line("files/file.txt")
print()

print_first_line("files/file.txt", start_from=10)
print()

numline = int(input("Какую строку из файла прочитать? "))
read_line("files/file.txt", numline=numline)
```

    The 344-sq. km. the periphery of Navi Mimbai starts on the East with Kalundre village, on the West is the hill range that starts from Digha and runs up to Taloja; in the North is Digha village while Chanje village lies in the South, Dronagiri is on the South-East. The area comprised of 95 villages of Thane and Raigad Districts.
    
    0: The 344-sq. km. the periphery of Navi Mimbai starts on the East with Kalundre village, on the West is the hill range that starts from Digha and runs up to Taloja; in the North is Digha village while Chanje village lies in the South, Dronagiri is on the South-East. The area comprised of 95 villages of Thane and Raigad Districts. Fun!
    
    The 344-sq. km. the periphery of Navi Mimbai starts on the East with Kalundre village, on the West is the hill range that starts from Digha and runs up to Taloja; in the North is Digha village while Chanje village lies in the South, Dronagiri is on the South-East. The area comprised of 95 villages of Thane and Raigad Districts. Fun!
    
    . km. the periphery of Navi Mimbai starts on the East with Kalundre village, on the West is the hill range that starts from Digha and runs up to Taloja; in the North is Digha village while Chanje village lies in the South, Dronagiri is on the South-East. The area comprised of 95 villages of Thane and Raigad Districts. Fun!
    
    Какую строку из файла прочитать? 1
    The 344-sq. km. the periphery of Navi Mimbai starts on the East with Kalundre village, on the West is the hill range that starts from Digha and runs up to Taloja; in the North is Digha village while Chanje village lies in the South, Dronagiri is on the South-East. The area comprised of 95 villages of Thane and Raigad Districts. Fun!
    

## Задание 5

Напишите программу, которая принимает от пользователя имя файла и отображает все строки из файла, которые содержат символ комментария Python `#`.

**Решение**


```python
def print_lines_with_sharp(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if "#" in line:
                print(line)
                
                
print_lines_with_sharp("files/file1.txt")
```

    Этот файл содержит строки с комментариями Python (#).
    
    # комментарий
    
    

## Задание 6

Читать файл с начала - это просто, но что если вам нужно прочитать файл в обратном направлении, например для чтения файлов с логами. Напишите программу для чтения и отображения содержимого файла от конца до начала.

**Решение**


```python
def rread(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        lines = list(reversed(f.readlines()))
        
        for line in lines:
            yield line
            
            
for line in rread("files/1.txt"):
    print(line, end="")
```

    Табак?
    Скажите, Холмс, а в трубке точно
    Огромных фосфорных собак...
    Я вижу на болотных кочках
    
