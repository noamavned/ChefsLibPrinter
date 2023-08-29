from ChefsLibPrinter import print_obj

class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def GetName(self) -> str:
        """Returns the name of the fruit

        Returns:
            str: Name of the fruit
        """
        return self.name
    def GetPrice(self) -> float:
        return self.price

obj1 = Fruit("Banana", 2.45)
obj2 = Fruit("Apple", 5)
print_obj(obj1, 0, 1, 0)
# print("_____________________________")
# print_obj(obj2)
