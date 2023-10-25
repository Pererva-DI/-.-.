money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 1  # Текущий месяц

# Цикл прекращается, если в следующем месяце накопления будут меньше трат
while money_capital > spend + spend * increase:
    if month > 1:  # Исключаем рост цен в первом месяце
        spend += spend * increase
    money_capital += salary - spend  # Остаток на конец месяца
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
