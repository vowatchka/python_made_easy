# Практические задания главы 7 «ПРОЕКТ 1: Рисунки из символов с помощью циклов и функций»

## Рисунок 1

```
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
```

**Решение**


```python
def pic1(height):
    for i in range(height, 0, -1):
        # отступы
        print(" " * (height - i), end="")
        # звездочки
        print(" ".join(list("*" * i)))
        
        
pic1(6)
```

    * * * * * *
     * * * * *
      * * * *
       * * *
        * *
         *
    

## Рисунок 2

```
*
* *
* * *
* * * *
* * * * *
* * * * * *

* * * * * *
* * * * *
* * * *
* * *
* *
*
```

**Решение**


```python
def print_stars(count):
    print(" ".join(list("*" * count)))


def triangle(height):
    for i in range(1, height + 1):
        print_stars(i)
        
        
def triangle_reversed(height):
    for i in range(height, 0, -1):
        print_stars(i)
        
        
def pic2(height):
    triangle(height)
    print()
    triangle_reversed(height)
    
    
pic2(6)
```

    *
    * *
    * * *
    * * * *
    * * * * *
    * * * * * *
    
    * * * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
    

## Рисунок 3

```
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
```

**Решение**


```python
def print_stars(count, space_count):
    # отступы
    print(" " * space_count, end="")
    # звездочки
    print(" ".join(list("*" * count)))

def pic3(half_height):
    for i in range(1, half_height + 1):
        print_stars(i, half_height - i)
        
    for i in range(half_height - 1, 0, -1):
        print_stars(i, half_height - i)
        
        
pic3(5)
```

        *
       * *
      * * *
     * * * *
    * * * * *
     * * * *
      * * *
       * *
        *
    

## Рисунок 4

```
****************
*******__*******
******____******
*****______*****
****________****
***__________***
**____________**
*______________*
```

**Решение**


```python
def print_chars(char, count):
    print(char * count, end="")


def pic4(height):
    for i in range(0, height):
        print_chars("*", height - i)
        print_chars("_", i * 2)
        print_chars("*", height - i)
        print()
        

pic4(8)
```

    ****************
    *******__*******
    ******____******
    *****______*****
    ****________****
    ***__________***
    **____________**
    *______________*
    

## Рисунок 5

```
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
     *
    * *
   * * *
  * * * *
 * * * * *
* * * * * *
```

**Решение**


```python
def print_stars(count, space_count):
    # отступы
    print(" " * space_count, end="")
    # звездочки
    print(" ".join(list("*" * count)))
        
        
def pic5(height):
    for i in range(height, 0, -1):
        print_stars(i, height - i)
    for i in range(1, height + 1):
        print_stars(i, height - i)
    
    
pic5(6)
```

    * * * * * *
     * * * * *
      * * * *
       * * *
        * *
         *
         *
        * *
       * * *
      * * * *
     * * * * *
    * * * * * *
    

## Рисунок 6

```
6 6 6 6 6 6
6 6 6 6 6
6 6 6 6
6 6 6
6 6
6
```

**Решение**


```python
def print_digits(digit, count):
    print(" ".join([str(digit)] * count))


def pic6(height):
    for i in range(height, 0, -1):
        print_digits(6, i)
    
    
pic6(6)
```

    6 6 6 6 6 6
    6 6 6 6 6
    6 6 6 6
    6 6 6
    6 6
    6
    

## Рисунок 7

```
6 6 6 6 6 6
5 5 5 5 5
5 5 5 5
5 5 5
5 5
5
```

**Решение**


```python
def print_digits(digit, count):
    print(" ".join([str(digit)] * count))


def pic7(height):
    for i in range(height, 0, -1):
        if i == height:
            print_digits(height, i)
        else:
            print_digits(height - 1, i)
    
    
pic7(6)
```

    6 6 6 6 6 6
    5 5 5 5 5
    5 5 5 5
    5 5 5
    5 5
    5
    

## Рисунок 8

```
1
2 3
4 5 6
7 8 9 10
```

**Решение**


```python
def pic8(height):
    last_digit = 1
    for row_num in range(1, height + 1):
        # числа в строке идут от последнего числа в предыдущей строке
        # и до (последнее число в предыдущей строке + номер строки)
        digits = list(range(last_digit, last_digit + row_num))
        last_digit = digits[-1] + 1
        
        print(" ".join(str(x) for x in digits))
        
        
pic8(4)
```

    1
    2 3
    4 5 6
    7 8 9 10
    

## Рисунок 9

```
  1
  2     1
  4     2     1
  8     4     2     1
 16     8     4     2    1
 32    16     8     4    2    1
 64    32    16     8    4    2    1
128    64    32    16    8    4    2    1
```

**Решение**


```python
def pic9(height):
    power_of_two = height - 1
    
    # вычисляем длину для выравнивания
    rjust_len = len(str(2 ** power_of_two))
    
    # цикл по строкам
    for i in range(0, power_of_two + 1):
        # цикл по степеням
        for j in range(i, -1, -1):
            print(str(2 ** j).rjust(rjust_len), end=" " * 4)
        print()
        
        
pic9(8)
```

      1    
      2      1    
      4      2      1    
      8      4      2      1    
     16      8      4      2      1    
     32     16      8      4      2      1    
     64     32     16      8      4      2      1    
    128     64     32     16      8      4      2      1    
    

## Рисунок 10

```
6 5 4 3 2 1 1 2 3 4 5 6

6 5 4 3 2     2 3 4 5 6

6 5 4 3         3 4 5 6

6 5 4             4 5 6

6 5                 5 6

6                     6
```

**Решение**


```python
def pic10(height):
    for i in range(0, height):
        # цифры в обратном порядке
        print(" ".join(str(x) for x in range(height, i, -1)), end="")
        
        # пропущенные числа
        missed_digits = list(range(1, i + 1)) * 2
        # space_count = x + y
        # где x - длина строки, состоящей из пропущенных чисел, а y - количество пробелов, которыми
        # должны разделяться пропущенные числа (оно равно количестыу пропущенных чисел + 1)
        space_count = len("".join(str(x) for x in missed_digits)) + len(missed_digits) + 1
        print(" " * space_count, end="")
        
        # цифры в прямом порядке
        print(" ".join(str(x) for x in range(i + 1, height + 1)))
        
        if i != height - 1:
            # пустая строка
            print()
        
        
pic10(6)
```

    6 5 4 3 2 1 1 2 3 4 5 6
    
    6 5 4 3 2     2 3 4 5 6
    
    6 5 4 3         3 4 5 6
    
    6 5 4             4 5 6
    
    6 5                 5 6
    
    6                     6
    
