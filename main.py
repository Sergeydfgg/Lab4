class Burger:
    def __init__(self):
        self.ingredients = list()

    def default_burger(self):
        self.ingredients = ["Хлеб", "Котлета", "Кетчуп", "Хлеб"]
        return self

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        self.ingredients[-2], self.ingredients[-1] = self.ingredients[-1], self.ingredients[-2]

    def show_burger(self):
        for part in self.ingredients[::-1]:
            print(part)


def extra_cheese(func):
    def wrapper():
        burger = func()
        burger.add_ingredient('Сыр')
    return wrapper


def extra_holopenio(func):
    def wrapper():
        burger = func()
        burger.add_ingredient('Холопеньо')
    return wrapper


def extra_bacon(func):
    def wrapper():
        burger = func()
        burger.add_ingredient('Бекон')
    return wrapper


def main():
    my_burger_1 = Burger()
    my_burger_2 = Burger()
    my_burger_3 = Burger()

    print("Бургер с экстра сыром")
    extra_cheese(my_burger_1.default_burger)()
    my_burger_1.show_burger()
    print("\n")

    print("Бургер с экстра холопеньо")
    extra_holopenio(my_burger_2.default_burger)()
    my_burger_2.show_burger()
    print("\n")

    print("Бургер с экстра беконом")
    extra_bacon(my_burger_3.default_burger)()
    my_burger_3.show_burger()
    print("\n")


if __name__ == "__main__":
    main()

