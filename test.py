class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # __ означает private атрибут
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

# Использование
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
# account.__balance  # Ошибка - доступ запрещен





class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Звук животного"

class Dog(Animal):  # Наследование от Animal
    def speak(self):  # Переопределение метода
        return f"{self.name} говорит Гав!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит Мяу!"

# Использование
animals = [Dog("Бобик"), Cat("Мурка")]
for animal in animals:
    print(animal.speak())






class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Функция работает с любым объектом, у которого есть метод area()
def print_area(shape):
    print(f"Площадь: {shape.area()}")

# Использование
shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print_area(shape)





from abc import ABC, abstractmethod
class Database(ABC):  # Абстрактный класс
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def query(self, sql):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Подключение к MySQL"
    
    def query(self, sql):
        return f"Выполнение запроса MySQL: {sql}"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Подключение к PostgreSQL"
    
    def query(self, sql):
        return f"Выполнение запроса PostgreSQL: {sql}"
# Использование
def work_with_db(db: Database):
    print(db.connect())
    print(db.query("SELECT * FROM users"))

# Можно работать с любой базой, реализующей интерфейс Database
work_with_db(MySQLDatabase())
work_with_db(PostgreSQLDatabase())











