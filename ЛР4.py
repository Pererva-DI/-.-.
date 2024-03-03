class Worker:
    """ Базовый класс работника. """
    def __init__(self, name: str, age: int, salary: int):
        """
        Создание и подготовка к работе объекта "Работник"

        :param name: Имя работника
        :param age: Возраст работника в годах
        :param salary: Зарплата работника в рублях

        :raise TypeError: Имя работника должно быть типа 'str'
        :raise TypeError: Возраст работника должен быть типа 'int'
        :raise ValueError: Возраст работника должен быть положительным числом
        :raise TypeError: Зарплата работника должна быть типа 'int'
        :мraise ValueError: Зарплата работника должен быть положительным числом

        Пример:
        >>> worker = Worker("Иванов Иван Иванович", 30, 60000) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя работника должно быть типа 'str'")

        if not isinstance(age, int):
            raise TypeError("Возраст работника должен быть типа 'int'")
        if age <= 0:
            raise ValueError("Возраст работника должен быть положительным числом")

        if not isinstance(salary, int):
            raise TypeError("Зарплата работника должна быть типа 'int'")
        if salary <= 0:
            raise ValueError("Зарплата работника должен быть положительным числом")

        self._name = name
        self._age = age
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def salary(self):
        return self._salary

    def __str__(self):
        return f"Работник: {self.name}; Зарплата: {self.salary}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}, salary={self.salary!r})"

    def salary_change(self, raise_or_cut: bool, amount: int) -> None:
        """
        Функция увеличивает или уменьшает зарплату

        :param raise_or_cut: Изменение зарплаты (Если True, то увеличивается, если False, то уменьшается)
        :param amount: Размер, на который изменяется зарплата

        :raise TypeError: Изменение зарплаты должно быть типа 'bool'
        :raise TypeError: Размер изменения зарплаты должно быть типа 'int'
        :raise ValueError: Размер изменения зарплаты должен быть положительным числом

        Пример:
        >>> worker = Worker("Иванов Иван Иванович", 30, 60000)
        >>> worker.salary_change(True, 5000)
        """
        ...

    def birthday(self) -> None:
        """
        Функция увеличивает возраст работника в день рождения

        Пример:
        >>> worker = Worker("Иванов Иван Иванович", 30, 60000)
        >>> worker.birthday()
        """
        ...


class LocalWorker(Worker):
    """ Дочерний класс местного работника """
    def __init__(self, name: str, age: int, salary: int, home_address: str):
        """
        Создание и подготовка к работе объекта Местный работник

        :param home_address: Домашний адрес работника

        :raise TypeError: Домашний адрес работника должен быть типа 'str'

        Пример:
        >>> local_worker1 = LocalWorker("Иванов Иван Иванович", 30, 60000, "ул.Пушкина, д.9, кв.9")
        """
        super().__init__(name, age, salary)
        self.home_address = home_address

        if not isinstance(home_address, str):
            raise TypeError("Домашний адрес работника должен быть типа 'str'")

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, age={self.age!r}, salary={self.salary!r}, ' \
                f'home_address={self.home_address!r})'

    def birthday(self) -> None:
        """
        Функция увеличивает возраст работника в день рождения. Местным работникам в день рождения увеличивает
        также зарплату на 3000 рублей.

        Пример:
        >>> local_worker1 = LocalWorker("Иванов Иван Иванович", 30, 60000, "ул.Пушкина, д.9, кв.9")
        >>> local_worker1.birthday()
        """
        ...


class ForeignWorker(Worker):
    """ Дочерний класс иностранного работника """
    def __init__(self, name: str, age: int, salary: int, citizenship: str):
        """
        Создание и подготовка к работе объекта Иностранный работник

        :param citizenship: Гражданство работника

        :raise TypeError: Гражданство работника должно быть типа 'str'

        Пример:
        >>> foreign_worker1 = ForeignWorker("Иванов Иван Иванович", 30, 60000, "Республика Беларусь")
        """
        super().__init__(name, age, salary)
        self.citizenship = citizenship

        if not isinstance(citizenship, str):
            raise TypeError("Гражданство работника должно быть типа 'str'")

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, age={self.age!r}, salary={self.salary!r}, ' \
                f'citizenship={self.citizenship!r})'


local_worker = LocalWorker(name="Иванов Иван Иванович", age=30, salary=60000, home_address="ул.Пушкина, д.9, кв.9")
print(str(local_worker))
print(repr(local_worker))

foreign_worker = ForeignWorker(name="Иванов Иван Иванович", age=30, salary=60000, citizenship="Республика Беларусь")
print(str(foreign_worker))
print(repr(foreign_worker))
