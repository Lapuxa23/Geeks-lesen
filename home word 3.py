while True:
    word = input("Введите любое слово (на русском и английском): ")
    word = word.lower()
    vowels = "аеёиоуыэюяaeiouy"
    consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"
    total_letters = 0
    vowel_count = 0
    consonant_count = 0
    for letter in word:
        if letter in vowels:
            vowel_count += 1
        elif letter in consonants:
            consonant_count += 1
        total_letters += 1
    print(f"Общее количество букв в слове '{word}': {total_letters}")
    print(f"Количество гласных букв: {vowel_count}")
    print(f"Количество согласных букв: {consonant_count}")
    if total_letters > 0:
        vowel_percentage = round(vowel_count / total_letters * 100, 2)
        consonant_percentage = round(consonant_count / total_letters * 100, 2)
        print(f"Процентное соотношение гласных: {vowel_percentage}%")
        print(f"Процентное соотношение согласных: {consonant_percentage}%")
    else:
        print("В слове нет букв.")
    continue_choice = input("Хотите продолжить? (да/нет): ")
    if continue_choice.lower() != "да":
        break
print("Завершено.")