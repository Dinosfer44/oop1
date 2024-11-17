class Fruit:
    def __init__(self, name):
        self.name = name
    def get_name (self):
        print (f"Вот это {self.name}")
class Apple(Fruit):
    def __init__(self, name, taste):
        super().__init__(name)
        self.taste = taste
    def get_name(self):
        print (f"{self.name} {self.taste}")
class Banana(Fruit):
    def __init__(self, name, taste):
        super().__init__(name)
        self.taste = taste
    def get_name(self):
        print(f"{self.name} {self.taste}")

fruit = Fruit ("Кокос")
apple = Apple("Яблоко", "Вкусное")
banan = Banana("Банан", "Мягкий")
fruit.get_name()
apple.get_name()
banan.get_name()