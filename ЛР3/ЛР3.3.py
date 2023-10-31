def count_letters(text):
    dict_letters = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter.isalpha() and letter in dict_letters.keys():
            dict_letters[letter] += 1
        elif letter.isalpha() and letter not in dict_letters.keys():
            dict_letters[letter] = 1
    return dict_letters


def calculate_frequency(dictionary):
    dict_frequency = {}
    letters_amount = sum(dictionary.values())
    for letter_key in dictionary.keys():
        dict_frequency[letter_key] = format(round(dictionary[letter_key] / letters_amount, 2), ".2f")
    return dict_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

frequency_dictionary = calculate_frequency(count_letters(main_str))
for letter_from_text, frequency in frequency_dictionary.items():
    print(f"{letter_from_text}: {frequency}")
