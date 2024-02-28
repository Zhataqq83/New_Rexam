class Pizza:

    def __init__(self, name:str, dough:str, sauce:str, filling:list, price:int) -> None:
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.filling = filling
        self.price = price

    def prepare(self):
        print(
            f" Подготовка {self.number} {self.name} с {self.dough} тестом, с {self.sauce} соусом и начинкой(",".join{self.toppings})"
        ) 

    def cut(self):
        return f"Нарезаем {self.name}"

    def bake(self):
        return f"Выпекаем {self.name}"

    def add_to_order(self):
        return f"{self.name} добавлена в заказ."

class PepPizza(Pizza):
    def __init__(self) -> None:
     super.__init__("Пеперони", "тонкое", "томантным", ["пепперони", "сыр"], "3500тенге")


class BBQPizza(Pizza):
    def __init__(self, extra_topinc: list = None) -> None:  
        toppings = ["Курица", "лук", "Сыр"]
        self.extra_toppings = ["Барбекю", "Яйцо"]

        super.__init__("Барбекю", "стандартное", "какой-то", topping, "4500тенге")

    def add_topping(self, topping: str) -> None:
        choice = input(f"Хотите добавить {topping}? (да/нет)")
        if choice.lower() == "нет"
            return
        if choice.lower( ) == "да"
            if topping in self.toppings:
                print(Он уже есть в пицце)
                return
            self.topping.append(topping)
            print("Добавлено")
            return

    def chage_topping(self, new_topping: list) -> None:
        self.toppings = new_topping
        print("Ингредиент удалён")

    def ask_topping(self) -> str:
        return input(
            f"Какой ингредиент добавить ?"
        )

        
    
class SFPizza(Pizza):
    def __init__(self) -> None:
     super.__init__("Дары Моря", "стандартное", "какой-то", ["креветки", "ананасы"], "6500тенге")

class Order:
    """
    Класс, представляющий заказ, содержит список пицц и методы работы с этим списком
    """
    def __init__(self) -> None:
        self.pizzas: list[Pizza] = []

    def add_pizza(self, pizza: Pizza) -> None:
        """
        
        """
        self.pizzas.append(pizza)    
    
    def calculate_total(self) -> None:
        """
        Возвращает итоговую стоимость заказала
        """
        return sum(pizza.price for pizza in self.pizzas)

class Terminal:
    """ 
    Терминал для взаимодействия с меню
    """
    def __init__(self) -> None:
        self.menu: dict[int, Pizza] {
            1: PepPizza(),
            2: BBQPizza(),
            3: SFPizza()
        }
        self.order: Order | None=None

    def display_menu(self) -> None:
        """
        Выводит меню
        """
        print("Menu:", )
        for key, pizza in self.menu.items():
        print(f"{key}. {pizza.name} - {pizza.price} тенге")

    def take_order(self) -> None:
        """
        Принимает заказ от пользователя
        """
        self.order = Order()
        while True:
            self.display_menu()
            choice = input(
                "=" * 80
                + "\nВведите номер пиццы, которую хотите заказать (0 для завершения)"
                + "=" * 80
                + "\n"
            )
            if choice == "0":
                break
            if choice == "2":
                topping = self.mune[int(choice)].ask_topping()
                self.menu[int(choice)].add_topping()
            if int(choice) in self.menu:
                self.order.add_pizza(self.menu[int(choice)])
                print(f"{self.menu[int(choice)].name} добавлена в ваш заказ.")
            else:
                print("Неверный выбор. Выберите меню из пицц.")
                continue

    def confirm_order(self) -> bool:
        """
        Подтверждает заказ, воздвращает True, если заказ подтверждён
        """
        if self.order:
            print(f"Итого к оплате: {self.order.calculate_total()} тенге.")
            cofirmation = input("Вы хотите подтвердить заказ? (да\нет):")
            if cofirmation.lower() == "да":
                print("Заказ подтверждён")
                return True
            else:
                print("Заказ отменён.")
                self.order = None
                return False
        else:
            print(Нет заказа для подтверждения.)
            return False

    def take_payment(self) -> None:

        if self.order:
            print("Оплата принята. Ваш заказ готовится.")
            for pizza in self.order.pizzas:
                pizza.prepare()
                pizza.cut()
                pizza.bake()
            print("Спасибо за ваш заказ!")
        
if __name__ == "__main__":
    
    terminal = Terminal()
    terminal.take_order()
    if terminal.confirm_order():
        terminal.take_payment()