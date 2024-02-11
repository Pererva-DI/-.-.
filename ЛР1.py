import doctest


class Series:
    def __init__(self, name: str, year_start: int, year_finish: int):
        """
        Создание и подготовка к работе объекта 'Сериал'

        :param name: Название сериала
        :param year_start: Год начала сериала
        :param year_finish: Год окончания сериала

        Пример:
        >>> series1 = Series("Breaking Bad", 2008, 2013) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название сериала должно быть типа 'str'")
        self.name = name

        if not isinstance(year_start, int):
            raise TypeError("Год начала сериала должен быть типа 'int'")
        if year_start <= 0:
            raise ValueError("Год начала сериала должен быть положительным числом")
        self.year_start = year_start

        if not isinstance(year_finish, int):
            raise TypeError("Год окончания сериала должен быть типа 'int'")
        if year_finish < year_start:
            raise ValueError("Год окончания сериала должен быть больше года начала")
        self.year_finish = year_finish

    def how_many_years(self) -> int:
        """
        Функция выводит продолжительность сериала

        :return: Длительность сериала

        Пример:
        >>> series = Series("Breaking Bad", 2008, 2013)
        >>> series.how_many_years()
        """
        ...

    def continue_series(self, years: int) -> None:
        """
        Функция продлевает сериал

        :param years: Количество лет, на которое продлевается сериал

        :raise TypeError: Количество лет должно быть типа 'int'
        :raise ValueError: Количество лет должно быть положительным числом

        Пример:
        >>> series = Series("Breaking Bad", 2008, 2013)
        >>> series.continue_series(2)
        """
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть типа 'int'")
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным числом")
        ...


class Street:
    def __init__(self, name: str, material: str, length: int):
        """
        Создание и подготовка к работе объекта 'Улица'

        :param name: Название улицы
        :param material: Материал дорожного полотна
        :param length: Длина улицы в метрах

        Пример:
        >>> street1 = Street("Пушкинская", "Брусчатка", 1500) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название улицы должно быть типа 'str'")
        self.name = name

        if not isinstance(material, str):
            raise TypeError("Материал дорожного полотна должен быть типа 'str'")
        self.material = material

        if not isinstance(length, int):
            raise TypeError("Длина улицы в метрах должна быть типа 'int'")
        if length < 0:
            raise ValueError("Длина улицы в метрах не может быть отрицательной")
        self.lenght = length

    def extension(self, ex_meters: int) -> None:
        """
        Функция удлиняет улицу

        :param ex_meters: Количество метров, на которое удлиняется улица

        :raise TypeError: Количество метров должно быть типа 'int'
        :raise ValueError: Количество метров должно быть положительным числом

        Пример:
        >>> street = Street("Пушкинская", "Брусчатка", 1500)
        >>> street.extension(500)
        """
        if not isinstance(ex_meters, int):
            raise TypeError("Количество метров должно быть типа 'int'")
        if ex_meters <= 0:
            raise ValueError("Количество метров должно быть положительным числом")
        ...

    def trim(self, tr_meters: int) -> None:
        """
        Функция укорачивает улицу

        :param tr_meters: Количество метров, на которое укорачивается улица

        :raise TypeError: Количество метров должно быть типа 'int'
        :raise ValueError: Количество метров должно быть положительным числом

        Пример:
        >>> street = Street("Пушкинская", "Брусчатка", 1500)
        >>> street.trim(500)
        """
        if not isinstance(tr_meters, int):
            raise TypeError("Количество метров должно быть типа 'int'")
        if tr_meters <= 0:
            raise ValueError("Количество метров должно быть положительным числом")
        ...


class Income:
    def __init__(self, source: str, currency: str, value: float):
        """
        Создание и подготовка к работе объекта 'Доход'

        :param source: Источник дохода
        :param currency: Валюта
        :param value: Размер дохода

        Пример:
        >>> income1 = Income("Пенсия", "Рубли", 30000) # инициализация экземпляра класса
        """
        if not isinstance(source, str):
            raise TypeError("Источник дохода должен быть типа 'str'")
        self.source = source

        if not isinstance(currency, str):
            raise TypeError("Валюта должна быть типа 'str'")
        self.currency = currency

        if not isinstance(value, (int, float)):
            raise TypeError("Размер дохода должен быть типа 'int' или 'float'")
        if value < 0:
            raise ValueError("Размер дохода не может быть отрицательным")
        self.value = value

    def exchange(self, new_currency: str, rate: float) -> None:
        """
                Функция переводит валюту в другую согласно курсу

                :param new_currency: Новая валюта
                :param rate: Курс перевода в новую валюту

                :raise TypeError: Валюта должна быть типа 'str'
                :raise TypeError: Курс перевода должен быть типа 'int' или 'float'
                :raise ValueError: Курс перевода должен быть положительным числом

                Пример:
                >>> income = Income("Пенсия", "Рубли", 30000)
                >>> income.exchange("Евро", 0.01)
                """
        if not isinstance(new_currency, str):
            raise TypeError("Валюта должна быть типа 'str'")
        if not isinstance(rate, (int, float)):
            raise TypeError("Курс перевода должен быть типа 'int' или 'float'")
        if rate <= 0:
            raise ValueError("Курс перевода должен быть положительным числом")
        ...

    def increase(self, inc_value: float) -> None:
        """
        Функция увеличивает доход

        :param inc_value: Количество денег, на которое увеличивается доход

        :raise TypeError: Количество денег должно быть типа 'int' или 'float'
        :raise ValueError: Количество денег должно быть положительным числом

        Пример:
        >>> income = Income("Пенсия", "Рубли", 30000)
        >>> income.increase(2000)
        """
        if not isinstance(inc_value, (int, float)):
            raise TypeError("Количество денег должно быть типа 'int' или 'float'")
        if inc_value <= 0:
            raise ValueError("Количество денег должно быть положительным числом")

    def decrease(self, dec_value: float) -> None:
        """
        Функция уменьшает доход

        :param dec_value: Количество денег, на которое уменьшается доход

        :raise TypeError: Количество денег должно быть типа 'int' или 'float'
        :raise ValueError: Количество денег должно быть положительным числом

        Пример:
        >>> income = Income("Пенсия", "Рубли", 30000)
        >>> income.decrease(2000)
        """
        if not isinstance(dec_value, (int, float)):
            raise TypeError("Количество денег должно быть типа 'int' или 'float'")
        if dec_value <= 0:
            raise ValueError("Количество денег должно быть положительным числом")


if __name__ == "__main__":
    doctest.testmod()
