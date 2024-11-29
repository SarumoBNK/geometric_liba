# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a


## Структура проекта:
Проект состоит из четырех файлов:
	_1_. _circle.py
	2. rectangle.py
	3. square.py
	4. triangle.py_
	
В каждом файле содержатся функции по нахождению периметра и площади, каждой соответствующей фигуры, по формулам записанным выше. 
# _[circle.py](../circle.py)_

В данном файле содержаться функции для нахождения площади и периметра **круга**
Используется библиотека _math_, для использования константы $pi$ \
Функция принимает число r - радиус круга, возвращает его площадь.

```python
import math

def area(r):
	return math.pi * r * r
```
Функция возвращает периметр круга.\
Параметры:\
r (int) : Радиус круга.\
Возвращаемое значение:\
per (float) : Периметр круга.
```py
def perimeter(r):
	per = 2 * math.pi * r
	return per
```
### Примеры работы:
```cmd
>> area(5)
>> 78.53981633974483
>> -----------------
>> perimeter(5)
>> 31.41592653589793
```

# _[rectangle.py](../rectangle.py)_

В данном файле содержаться функции для нахождения площади и периметра **прямоугольника**\
Функция вовращает площадь прямоугольника.

Параметры: \
	a (int) : Первая сторона прямоугольника \
	b (int) : Вторая сторона прямоугольника  

Возвращаемое значение: \
	s (int) : Произведение a и b 

```python
def area(a, b):
	s = a * b
	return s
```

Принимает числа a и b, возвращает их удвоенную сумму - периметр прямоугольника
```python
def perimeter(a, b):
	return (a+b) * 2
```
### Пример работы:
```cmd
>> area(10, 7)
>> 70
>> ---------------
>> perimeter(5, 8)
>> 26
```

# _[square.py](../square.py)_

В данном файле содержаться функции для нахождения площади и периметра **квадрата** \
Функция принимает число a - сторона квадрата, возвращает его произведение самого на себя - площадь квадрата 
```python
def area(a):
	return a * a
```
Функция принимает число a(сторона квадрата), возвращает произведение 4 * a (периметр квадрата)`
  
```python
def perimeter(a):
	return 4 * a
```
### Пример работы:
```cmd
>> area(7)
>> 49
>> ---------------
>> perimeter(5)
>> 20
```

# _[triangle.py](../triangle.py)_

В данном файле содержаться функции для нахождения площади и периметра **треугольника**\
Возвращает площадь треугольника\
Параметры:\
a (int) : Сторона треугольника\
h (int) : Высота треугольника

Возвращаемое значение:\
s (float) : Половина произведения a и h
```python
def area(a, h):
	s = a * h / 2
	return s
```
Функция принимает числа a, b, c(строны треугольника), возвращает их сумму (периметр треугольника)
```py
def perimeter(a, b, c):
	return a + b + c
```
## Пример работы
```cmd
>> area(7, 8)
>> 28.0
>> perimeter(5, 3, 4)
>> 12
```

## Tests
Тесты для проверки правильности работы функций **библиотеки** были реализованы  в _[tests.py](../tests.py)_\
Для каждого файла из библиотеки были созданны отдельные _классы_ :

```py
class TEST_TRIANGLE_METHODS(unittest.TestCase)
```
```py
class TEST_RECTANGLE_METHODS(unittest.TestCase)
```
```py
class TEST_SQUARE_METHODS(unittest.TestCase)
```
```py
class TEST_CIRCLE_METHODS(unittest.TestCase)
```

В тестах рассматривалось поведение функций при разных входных данных.
Такие как: *отцательного числа, нуля, строки и т.д*



## Commits

* 44af26f (HEAD -> new_features_465089) Added docs and readme
* 7133360 Documentation for triangle.py
* e316f49 Documentation for: rectangle.py, circle.py, square.py

* f4895e1 (origin/new_feature-465089) final commit
* 97d6ac7 Added new file: triangle.py. Fix error in def perimetr in rectangle.py file
* 1cd5d8d Added new file: rectangel.py
* d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
* 8ba9aeb L-03: Circle and square added
