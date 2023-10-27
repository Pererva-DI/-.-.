list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_player = int(len(list_players) // 2)  # индекс игрока посередине
first_team = list_players[:middle_player]
second_team = list_players[middle_player:]

print(first_team)
print(second_team)
