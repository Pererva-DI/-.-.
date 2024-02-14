class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, pages: int, name: str, author: str):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError('Количество страниц должно быть типа "int"')
        if pages <= 0:
            raise ValueError('Количество страниц должно быть положительным числом')
        self.pages = pages

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})'


class AudioBook(Book):
    def __init__(self, duration: float, name: str, author: str):
        super().__init__(name, author)
        if not isinstance(duration, (float, int)):
            raise TypeError('Продолжительность должна быть типа "float" или "int"')
        if duration <= 0:
            raise ValueError('Продолжительность должна быть положительным числом')
        self.duration = duration

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})'

