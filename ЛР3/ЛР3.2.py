def find_common_participants(first_group, second_group, separator=","):
    first_group = set(first_group.split(separator))
    second_group = set(second_group.split(separator))
    common_participants = list(first_group.intersection(second_group))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
