
days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
expenses = []

for day in days_of_week:
    expense = int(input(f"Введите расходы на {day}: "))
    expenses.append(expense)
total_expenses = sum(expenses)
average_expenses = round(total_expenses / 7, 1)
print("Общие расходы за неделю:", total_expenses)
print("Средние расходы за неделю:", average_expenses)
