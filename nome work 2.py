def get_zodiac_sign(day, month):
  """Возвращает знак зодиака по дню и месяцу рождения."""

  if month == 1:
    if 20 <= day <= 31:
      return "Водолей"
    else:
      return "Козерог"
  elif month == 2:
    if 1 <= day <= 18:
      return "Водолей"
    else:
      return "Рыбы"
  elif month == 3:
    if 1 <= day <= 20:
      return "Рыбы"
    else:
      return "Овен"
  elif month == 4:
    if 1 <= day <= 20:
      return "Овен"
    else:
      return "Телец"
  elif month == 5:
    if 1 <= day <= 21:
      return "Телец"
    else:
      return "Близнецы"
  elif month == 6:
    if 1 <= day <= 21:
      return "Близнецы"
    else:
      return "Рак"
  elif month == 7:
    if 1 <= day <= 22:
      return "Рак"
    else:
      return "Лев"
  elif month == 8:
    if 1 <= day <= 23:
      return "Лев"
    else:
      return "Дева"
  elif month == 9:
    if 1 <= day <= 23:
      return "Дева"
    else:
      return "Весы"
  elif month == 10:
    if 1 <= day <= 23:
      return "Весы"
    else:
      return "Скорпион"
  elif month == 11:
    if 1 <= day <= 22:
      return "Скорпион"
    else:
      return "Стрелец"
  elif month == 12:
    if 1 <= day <= 21:
      return "Стрелец"
    else:
      return "Козерог"
  else:
    return "Неверный ввод месяца."

while True:
  try:
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    if 1 <= month <= 12:
      if month in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= day <= 31:
          sign = get_zodiac_sign(day, month)
          print("Ваш знак зодиака:", sign)
          break
        else:
          print("Неверный ввод дня. Введите число от 1 до 31.")
      elif month in [4, 6, 9, 11]:
        if 1 <= day <= 30:
          sign = get_zodiac_sign(day, month)
          print("Ваш знак зодиака:", sign)
          break
        else:
          print("Неверный ввод дня. Введите число от 1 до 30.")
      elif month == 2:
        if 1 <= day <= 29:
          sign = get_zodiac_sign(day, month)
          print("Ваш знак зодиака:", sign)
          break
        else:
          print("Неверный ввод дня. Введите число от 1 до 29.")
      else:
        print("Неверный ввод месяца.")
    else:
      print("Неверный ввод месяца. Введите число от 1 до 12.")
  except ValueError:
    print("Неверный формат ввода. Введите числа.")

