total_volume = 1.44
pages = 100
lines_at_page = 50
chars_at_line = 25
weight_of_char = 4

total_volume *= 1024 ** 2  # Объем дискеты в байтах
weight_of_book = weight_of_char * chars_at_line * lines_at_page * pages
number_of_books = total_volume // weight_of_book

print("Количество книг, помещающихся на дискету:", int(number_of_books))
