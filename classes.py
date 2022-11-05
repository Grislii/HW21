class Storage:
    _items = {}
    _capacity = 0

    def __init__(self, items: dict, capacity: int):
        self._items = items
        self._capacity = capacity

    @classmethod
    def add(cls, name, count):
        if count > cls.get_free_space():
            print("На складе недостаточно места")
            return False
        else:
            try:
                cls._items[name] += count
            except KeyError:
                cls._items[name] = count
            return True

    @classmethod
    def remove(cls, name, count):
        try:
            if count > cls._items[name]:
                print("Невозможно забрать товар, т.к. его меньше")
                return False
            else:
                cls._items[name] -= count
                return True
        except KeyError:
            print(f"{name} такого товара нет")
            return False


    @classmethod
    def get_free_space(cls):
        items_count = 0
        for value in cls._items.values():
            items_count += value
        result = cls._capacity - items_count
        return result

    @classmethod
    def get_items(cls):
        result = ""
        for key, val in cls._items.items():
            result += f"{val} {key}\n"
        return result

    @classmethod
    def get_unique_items_count(cls):
        return len(cls._items)


class Store(Storage):
    _items = {"печеньки": 3, "арбузы": 8, "собачки": 2, "коробки": 5}
    _capacity = 100
    def __init__(self, items: dict, capacity=100):
        super().__init__(items, capacity)


class Shop(Storage):
    _items = {}
    _capacity = 20
    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)


class Request:
    def __init__(self, from_, to, amount, product):
        self._from = from_
        self._to = to
        self._amount = amount
        self._product = product

    def commit(self):
        """ Подтверждение запроса"""
        if self._from == "магазин":
            if not Shop.remove(self._product, self._amount):
                return False
        elif self._from == "склад":
            if not Store.remove(self._product, self._amount):
                return False
        else:
            return False
        if self._to == "магазин":
            if not Shop.add(self._product, self._amount):
                return False
            else:
                print("На складе хранится:\n")
                print(f"{Store.get_items()}")
                print("В магазине хранится:\n")
                print(f"{Shop.get_items()}")
                return True
        elif self._to == "склад":
            if not Store.add(self._product, self._amount):
                return False
            else:
                print("На складе хранится:\n")
                print(f"{Store.get_items()}")
                print("В магазине хранится:\n")
                print(f"{Shop.get_items()}")
                return True
        else:
            return False



    @property
    def from_(self):
        return self._from

    @from_.setter
    def from_(self, value):
        self._from = value

    @property
    def to(self):
        return self._to

    @to.setter
    def to(self, value):
        self._to = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value


class ExtractingInformation:
    def __init__(self, user_input):
        self.user_input = user_input
        self._from = ""
        self._to = ""
        self._amount = 0
        self._product = ""
        self.refresh_information()

    def refresh_information(self):
        """ Обновление информации полученной из строки """
        try:
            data = self.user_input.split()

            for pk, val in enumerate(data):
                val = val.lower()
                if val == "из":
                    self._from = data[pk + 1].lower()
                elif val == "в":
                    self._to = data[pk + 1].lower()
                elif val == "доставить":
                    self._amount = int(data[pk + 1].lower())
                    self._product = data[pk + 2].lower()
            return True
        except:
            print("Что-то пошло не так, проверьте правильность написания")
            return False

    @property
    def from_(self):
        return self._from

    @property
    def to(self):
        return self._to

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product
