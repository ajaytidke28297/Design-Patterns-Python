from abc import ABC


class HotDrink(ABC):

    def consume(self):
        pass


class Tea(HotDrink):
    
    def consume(self):
        print("This tea is delicious")


class Coffee(HotDrink):
    
    def consume(self):
        print("This coffee is delicious")
        
        
class HotDrinkFactory(ABC):
    
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):

    def prepare(self, amount):
        print("Put in tea bag, boil water, enjoy")
        return Tea()


class CoffeeFactory(HotDrinkFactory):

    def prepare(self, amount):
        print("Put in some coffee beans and enjoy")
        return Coffee()


def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


if __name__ == '__main__':
    entry = input("What kind of drink would you like?")
    drink = make_drink(entry)
    drink.consume()

