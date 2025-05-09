# Лабораторная работа по ООП в Python

**Тема:** Основы объектно-ориентированного программирования в Python  
**Цель:** Закрепить принципы ООП (инкапсуляция, наследование, полиморфизм) на практике  

## Основные задания (5 задач)

### Задание 1. Класс "Студент"
Реализуйте класс `Student` со следующими характеристиками:
- Атрибуты:
  - `name` (строка)
  - `student_id` (строка/число)
  - `grades` (список чисел)
- Методы:
  - `add_grade(grade)` - добавляет оценку с валидацией (0-10)
  - `get_average()` - возвращает средний балл
  - `display_info()` - красиво выводит информацию о студенте

### Задание 2. Наследование: класс "Преподаватель"
Создайте систему классов:
1. Базовый класс `Person` с атрибутами `name`, `age`
2. Дочерний класс `Teacher` с дополнительными атрибутами:
   - `subject` (преподаваемый предмет)
   - `students` (список объектов Student)
3. Реализуйте методы для работы со списком студентов:
   - `add_student()`
   - `remove_student()`
   - `list_students()`

### Задание 3. Полиморфизм: геометрические фигуры
Создайте иерархию классов:
1. Абстрактный базовый класс `Shape` с методами:
   - `area()`
   - `perimeter()`
2. Реализуйте 3 конкретных класса-наследника:
   - `Rectangle`
   - `Circle` 
   - `Triangle`
3. Напишите функцию `print_shape_info(shape)`, демонстрирующую полиморфизм

### Задание 4. Инкапсуляция: банковский счет
Реализуйте класс `BankAccount` с:
- Приватными атрибутами:
  - `_balance`
  - `_transactions`
- Публичными методами:
  - `deposit()`
  - `withdraw()`
  - Геттер `balance` через `@property`
- Логированием операций в `_transactions`

### Задание 5. Магические методы
Дополните класс `Student` из задания 1:
- `__str__` - строковое представление
- `__eq__` - сравнение по student_id
- `__len__` - количество оценок

## Дополнительные задания (2 задачи)

### Задание 6*. Декораторы свойств
Создайте класс `Temperature` с:
- Приватным атрибутом `_celsius`
- Геттером/сеттером через `@property` с валидацией
- Динамическим свойством `fahrenheit`

### Задание 7*. Множественное наследование
Создайте класс `Assistant`, который:
- Наследует от `Student` и `Teacher`
- Добавляет метод `help_student()`
- Корректно инициализирует атрибуты родительских классов

## Требования к оформлению
1. Каждое задание в отдельном файле `.py`
2. Документация классов и методов (docstrings)
3. Примеры использования (в `if __name__ == "__main__":`)
