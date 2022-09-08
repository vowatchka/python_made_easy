# Практические задания главы 10 «ПРОЕКТ 2: Автоматизация обработки множества изображений»

## Задание 1

Показать изображения в папке.

**Решение**


```python
import os
from typing import List
from PIL import Image


def get_images(dir_: str, files: List[str]):
    for fname in os.listdir(dir_):
        if fname in files:
            yield fname, Image.open(os.path.join(dir_, fname))
            
            
def show_images(dir_: str, files: List[str]):
    for fname, img in get_images(dir_, files):
        print(fname)
        display(img)
            

dir_ = "images"
files = ["python.jpg", "jupyter.jpg"]
show_images(dir_, files)
```

    jupyter.jpg
    


    
![png](10_project_2_files/10_project_2_2_1.png)
    


    python.jpg
    


    
![png](10_project_2_files/10_project_2_2_3.png)
    


## Задание 2

Изменить расширение файла.

**Решение**


```python
def change_ext(dir_: str, files: List[str], out_dir: str, out_ext: str):
    for fname, img in get_images(dir_, files):
        fn, fext = os.path.splitext(fname)
        
        os.makedirs(out_dir, exist_ok=True)
        
        img.save(os.path.join(out_dir, f"{fn}.{out_ext}"))


png_dir = "images/with_png"
change_ext(dir_, files, png_dir, "png")
show_images(png_dir, ["python.png", "jupyter.png"])
```

    jupyter.png
    


    
![png](10_project_2_files/10_project_2_4_1.png)
    


    python.png
    


    
![png](10_project_2_files/10_project_2_4_3.png)
    


## Задание 3

Изменить размер изображений.

**Решение**


```python
from typing import Tuple


def change_size(dir_: str, files: List[str], out_dir: str, new_size: Tuple[int, int]):
    for fname, img in get_images(dir_, files):
        fn, fext = os.path.splitext(fname)
        
        os.makedirs(out_dir, exist_ok=True)
        
        img.thumbnail(new_size)
        img.save(os.path.join(out_dir, fname))


small_dir = "images/small"
change_size(dir_, files, small_dir, (100, 100))
show_images(small_dir, ["python.jpg", "jupyter.jpg"])
```

    jupyter.jpg
    


    
![png](10_project_2_files/10_project_2_6_1.png)
    


    python.jpg
    


    
![png](10_project_2_files/10_project_2_6_3.png)
    


## Задание 4

Преобразовать изображения в черно-белые.

**Решение**


```python
def to_white_black(dir_: str, files: List[str], out_dir: str):
    for fname, img in get_images(dir_, files):
        fn, fext = os.path.splitext(fname)
        
        os.makedirs(out_dir, exist_ok=True)
        
        img = img.convert(mode="L")
        img.save(os.path.join(out_dir, fname))


wb_dir = "images/white_black"
to_white_black(dir_, files, wb_dir)
show_images(wb_dir, ["python.jpg", "jupyter.jpg"])
```

    jupyter.jpg
    


    
![png](10_project_2_files/10_project_2_8_1.png)
    


    python.jpg
    


    
![png](10_project_2_files/10_project_2_8_3.png)
    


## Задание 5

Повернуть изображения.

**Решение**


```python
def rotate(dir_: str, files: List[str], out_dir: str, angle: int):
    for fname, img in get_images(dir_, files):
        fn, fext = os.path.splitext(fname)
        
        os.makedirs(out_dir, exist_ok=True)
        
        img = img.rotate(angle)
        img.save(os.path.join(out_dir, fname))


rotate_dir = "images/rotate"
rotate(dir_, files, rotate_dir, 45)
show_images(rotate_dir, ["python.jpg", "jupyter.jpg"])
```

    jupyter.jpg
    


    
![png](10_project_2_files/10_project_2_10_1.png)
    


    python.jpg
    


    
![png](10_project_2_files/10_project_2_10_3.png)
    


## Задание 6

Изменить разрешение изображений.

**Решение**


```python
from typing import Tuple


def change_dpi(dir_: str, files: List[str], out_dir: str, new_dpi: Tuple[int, int]):
    for fname, img in get_images(dir_, files):
        fn, fext = os.path.splitext(fname)
        
        os.makedirs(out_dir, exist_ok=True)
        
        img.save(os.path.join(out_dir, fname), dpi=new_dpi)


dpi_dir = "images/dpi"
change_dpi(dir_, files, dpi_dir, (50, 50))
show_images(dpi_dir, ["python.jpg", "jupyter.jpg"])
```

    jupyter.jpg
    


    
![png](10_project_2_files/10_project_2_12_1.png)
    


    python.jpg
    


    
![png](10_project_2_files/10_project_2_12_3.png)
    

