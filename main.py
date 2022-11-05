from classes import *


def main():
    d = "\033[0m"
    ul = "\033[4m"
    b = "\033[1m"

    print("Программа: Вы можете отправлять запросы о переходе товаров с одних складов в другие")
    print(f"Пример: {b}Доставить{d} {ul}3{d} {ul}печеньки{d} {b}из{d} {ul}склад{d} {b}в{d} {ul}магазин{d}")
    print("На складе хранится:\n")
    print(f"{b}{Store.get_items()}{d}")
    print("В магазине хранится:\n")
    print(f"{b}{Shop.get_items()}{d}")

    while True:
        user_input = input("Пользователь: ")
        data = ExtractingInformation(user_input)
        request = Request(from_=data.from_, to=data.to, amount=data.amount, product=data.product)
        if request.commit():
            print("Запрос прошёл успешно!")
        else:
            print("Что-то пошло не так, проверьте правильность написания")


if __name__ == "__main__":
    main()
