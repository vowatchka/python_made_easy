# Практические задания главы 8 «Структуры данных и последовательности»

## Задание 1

Используйте списковые включения для создания следующих списков:

* `['C', 'O', 'U', 'N', 'T', 'R', 'Y']`
* `['C', 'A', 'T', 'CC', 'AA', 'TT', 'CCC', 'AAA', 'TTT']`
* `[[2], [3], [4], [3], [4], [5], [4], [5], [6]]`
* `[[2, 3, 4, 5], [3, 4, 5 ,6], [4, 5, 6, 7], [5, 6, 7, 8]]`
* `[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]`
* `[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`

**Решение**


```python
print(list("country".upper()))
print([char.upper() * i for i in range(1, 4) for char in "cat"])
print([[j] for i in range(3) for j in range(i + 2, i + 2 + 3)])
print([[j for j in range(i + 2, i + 2+ 4)] for i in range(4)])
print([(j, i) for i in range(1, 4) for j in range(1, 4)])
print([i ** 2 for i in range(10)])
```

    ['C', 'O', 'U', 'N', 'T', 'R', 'Y']
    ['C', 'A', 'T', 'CC', 'AA', 'TT', 'CCC', 'AAA', 'TTT']
    [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
    [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
    [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    

## Задание 2

Создайте пустой список. Допустим, он называется `my_list`. Заполните его 50 числами от 1 до 25 (числа могут повторяться).

**Решение**


```python
import random

my_list = [random.randint(1, 25) for _ in range(50)]
print(my_list)
```

    [2, 9, 15, 9, 16, 2, 19, 2, 3, 10, 22, 17, 22, 17, 4, 3, 2, 22, 12, 5, 20, 9, 19, 25, 11, 13, 23, 24, 5, 18, 6, 13, 23, 1, 21, 5, 5, 1, 11, 17, 23, 9, 23, 19, 24, 9, 2, 24, 19, 2]
    

## Задание 3

В списке `my_list`, созданном в предыдущем пункте, выполните поиск и узнайте, есть ли в нем числа 11, 18 и 20. Напишите код для поиска этих чисел. Кроме того, подсчитайте, сколько раз встречаются эти числа в списке.

**Решение**


```python
for num in (11, 18, 20):
    if num in my_list:
        print(f"Число {num} входит в список my_list {my_list.count(num)} раз")
    else:
        print(f"Число {num} не входит в список my_list")
```

    Число 11 входит в список my_list 2 раз
    Число 18 входит в список my_list 1 раз
    Число 20 входит в список my_list 1 раз
    

## Задание 4

Напишите код для вывода информации о том, сколько четных и нечетных чисел в списке `my_list`.

**Решение**


```python
from typing import List


def evens(lst: List[int]) -> int:
    return len(list(x for x in lst if x % 2 == 0))


def odds(lst: List[int]) -> int:
    return len(list(x for x in lst if x % 2 != 0))


print(f"Четных чисел в списке my_list: {evens(my_list)}")
print(f"Нечетных чисел в списке my_list: {odds(my_list)}")
```

    Четных чисел в списке my_list: 19
    Нечетных чисел в списке my_list: 31
    

## Задание 5

Напишите код для создания из `my_list` другого списка, в котором числа равны квадрату чисел в `my_list`, но в обратном порядке.

**Решение**


```python
from typing import List


def reversed_sqrts(lst: List[int]) -> List[int]:
    sqrts = [x ** 2 for x in lst]
    return list(reversed(sqrts))


print(reversed_sqrts(my_list))
```

    [4, 361, 576, 4, 81, 576, 361, 529, 81, 529, 289, 121, 1, 25, 25, 441, 1, 529, 169, 36, 324, 25, 576, 529, 169, 121, 625, 361, 81, 400, 25, 144, 484, 4, 9, 16, 289, 484, 289, 484, 100, 9, 4, 361, 4, 256, 81, 225, 81, 4]
    

## Задание 6

Напишите функцию `sorted_list()`, которая принимает в качестве параметра список и возвращает `True`, если список отсортирован в порядке возрастания, и `False` в противном случае. В качестве дополнительного условия вы можете считать, что элементы списка можно сравнивать с помощью операторов отношения `<`, `>` и т.д.

**Решение**


```python
from typing import List, Any


def is_sorted(lst: List[Any], reverse: bool = False) -> bool:
    return all(lst[i] <= lst[i + 1] if not reverse else lst[i] >= lst[i + 1] for i in range(len(lst) - 1))


lst = [3, 4, 1, 6, 9]
print(is_sorted(lst))
print(is_sorted(list(sorted(lst))))
print(is_sorted(list(sorted(lst, reverse=True)), reverse=True))
```

    False
    True
    True
    

## Задание 7

Напишите программу Python для вывода имен и номеров телефонов 10 ваших друзей, сохранения их в словаре и вывода номера телефона по заданному имени.

**Решение**


```python
from typing import List, Dict
from collections import OrderedDict


class TelBook:
    def __init__(self):
        self._telbook = OrderedDict()
        
    def add(self, name: str, tel: str):
        self._telbook[name] = tel
        
    def show_tel(self, name: str) -> str:
        try:
            return self._telbook[name]
        except KeyError:
            raise KeyError(f"В телефонной книге нет записи с именем {name!r}")
            
    def show_first_entries(self, count: int) -> List[Dict[str, str]]:
        result = []
        
        if count > 0:
            for name, tel in self._telbook.items():
                result.append({"name": name, "tel": tel})

                if len(result) == count:
                    break
                
        return result
    
    def entries(self) -> int:
        return len(self._telbook)
    
    
telbook = TelBook()
telbook.add("Вася", "123")
telbook.add("Петя", "456")
telbook.add("Дима", "789")

print(f"Записей в книжке: {telbook.entries()}")
print(f"Телефон Димы: {telbook.show_tel('Дима')}")
print(f"Первые 0 записей: {telbook.show_first_entries(0)}")
print(f"Первые 2 записи: {telbook.show_first_entries(2)}")
print(f"Первые 10 записей: {telbook.show_first_entries(10)}")
```

    Записей в книжке: 3
    Телефон Димы: 789
    Первые 0 записей: []
    Первые 2 записи: [{'name': 'Вася', 'tel': '123'}, {'name': 'Петя', 'tel': '456'}]
    Первые 10 записей: [{'name': 'Вася', 'tel': '123'}, {'name': 'Петя', 'tel': '456'}, {'name': 'Дима', 'tel': '789'}]
    

## Задание 8

Напишите функцию, `remove_duplicates()`, которая принимает в качестве параметра список и возвращает новый список, содержащий только уникальные элементы из первого списка. Подсказка: они не обязательно должны сохранять порядок.

**Решение**


```python
def remove_duplicates(lst: list, save_order: bool = True) -> list:
    if not save_order:
        return list(set(lst))
    else:
        new_list = []
        for x in lst:
            if x not in new_list:
                new_list.append(x)
        return new_list
    
    
lst = [1, 3, 5, 7, 3, 5, 5, 6, 9, 2, 3, 4, 9]
print(f"Уникальные элементы с сохранением порядка: {remove_duplicates(lst)}")
print(f"Уникальные элементы без сохранения порядка: {remove_duplicates(lst, save_order=False)}")
```

    Уникальные элементы с сохранением порядка: [1, 3, 5, 7, 6, 9, 2, 4]
    Уникальные элементы без сохранения порядка: [1, 2, 3, 4, 5, 6, 7, 9]
    

## Задание 9

Напишите функцию для вычисления произведения элементов списка. Что произойдет, если в функцию передать список строк?

**Решение**


```python
from typing import List


def mult_items(lst: List[int]) -> int:
    if not len(lst):
        return 0
    else:
        acum = lst[0]
        for x in lst[1:]:
            acum *= x
        return acum
    
    
print(f"Произведение элементов списка []: {mult_items([])}")
print(f"Произведение элементов списка [4]: {mult_items([4])}")
print(f"Произведение элементов списка [2, 5, 3]: {mult_items([2, 5, 3])}")

try:
    mult_items(["1", "2", "3"])
except TypeError:
    print("Элементы должны быть числами")
```

    Произведение элементов списка []: 0
    Произведение элементов списка [4]: 4
    Произведение элементов списка [2, 5, 3]: 30
    Элементы должны быть числами
    
