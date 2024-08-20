# Перше завдання
#
# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
#
# Вимоги до завдання:
#
# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python.

import datetime


def get_days_from_today(date):
    try:
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.datetime.today().date()
        days_delta = current_date - date
        # if days_delta.days > 0:
        #     print(f"Від {date} до сьогоднішні пройшло {days_delta.days} днів")
        # elif days_delta.days == 0:
        #     print("Ви ввели сьогоднішню дату.")
        # else:
        #     print(f"Від сьогодні до {date} потрібно почекати "
        #           f"{days_delta.days * (-1)} днів")
        return days_delta.days
    except ValueError:
        print("Дату введено некоректно.")

get_days_from_today("2020-10-09")
# print(get_days_from_today("2020-10-09"))