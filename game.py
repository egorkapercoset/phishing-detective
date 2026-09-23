# game.py
# Логика игры "Фишинг-Детектив"

import random
from data import EMAILS, WEBSITES


class Stats:
    """Класс для хранения статистики игрока."""

    def __init__(self):
        self.email_correct = 0
        self.email_total = 0
        self.web_correct = 0
        self.web_total = 0

    def add_email_result(self, correct):
        self.email_total += 1
        if correct:
            self.email_correct += 1

    def add_web_result(self, correct):
        self.web_total += 1
        if correct:
            self.web_correct += 1

    def show(self):
        print("\n=== Статистика ===")
        if self.email_total > 0:
            percent = self.email_correct / self.email_total * 100
            print(f"Режим «Инспектор входящих»: {self.email_correct}/{self.email_total} "
                  f"({percent:.1f}%)")
        else:
            print("Режим «Инспектор входящих»: нет попыток.")

        if self.web_total > 0:
            percent = self.web_correct / self.web_total * 100
            print(f"Режим «Найди подделку»: {self.web_correct}/{self.web_total} "
                  f"({percent:.1f}%)")
        else:
            print("Режим «Найди подделку»: нет попыток.")
        print("===================\n")


def email_mode(stats: Stats):
    """Режим «Инспектор входящих»."""
    print("\n--- Инспектор входящих ---")
    emails = random.sample(EMAILS, min(5, len(EMAILS)))

    for i, email in enumerate(emails, 1):
        print(f"\nПисьмо {i} из {len(emails)}:")
        print(f"От: {email['sender']}")
        print(f"Тема: {email['subject']}")
        print(f"Текст: {email['body']}")

        while True:
            choice = input("Это фишинг? (y/n/hint): ").strip().lower()
            if choice == 'hint':
                if email['hints']:
                    print("Подсказки:")
                    for hint in email['hints']:
                        print(f"  - {hint}")
                else:
                    print("Для этого письма подсказок нет.")
                continue
            elif choice in ('y', 'n'):
                break
            else:
                print("Введите 'y', 'n' или 'hint'.")

        user_says_phishing = (choice == 'y')
        correct = (user_says_phishing == email['is_phishing'])
        stats.add_email_result(correct)

        if correct:
            print("Верно!")
        else:
            print("Неверно.")
        print(f"Объяснение: {email['explanation']}")

    print("\nКонец режима «Инспектор входящих».")
    stats.show()


def website_mode(stats: Stats):
    """Режим «Найди подделку»."""
    print("\n--- Найди подделку ---")
    site = random.choice(WEBSITES)
    print(f"\nСайт: {site['name']}")
    print(site['description'])
    print("\nЭлементы на странице:")
    for idx, elem in enumerate(site['elements'], 1):
        print(f"{idx}. {elem['text']}")

    print("\nВведите номера подозрительных элементов через пробел (например, 1 3 5):")
    user_input = input("> ").strip()

    try:
        selected = set(int(x) for x in user_input.split())
    except ValueError:
        print("Некорректный ввод. Выбор не сделан.")
        selected = set()

    correct_selections = set()
    for idx, elem in enumerate(site['elements'], 1):
        if elem['is_suspicious']:
            correct_selections.add(idx)

    for idx in selected:
        elem = site['elements'][idx - 1]
        if idx in correct_selections:
            print(f"Элемент {idx} действительно подозрительный. {elem['explanation']}")
        else:
            print(f"Элемент {idx} НЕ является подозрительным. {elem['explanation']}")

    for idx in correct_selections:
        if idx not in selected:
            elem = site['elements'][idx - 1]
            print(f"Вы пропустили подозрительный элемент {idx}: {elem['text']}")
            print(f"   Объяснение: {elem['explanation']}")

    correct = (selected == correct_selections)
    stats.add_web_result(correct)

    if correct:
        print("\nОтлично! Вы нашли все подозрительные элементы.")
    else:
        print("\nНекоторые элементы были пропущены или выбраны неверно.")
    stats.show()


def instructions():
    """Краткая инструкция для игрока."""
    print("\n=== Инструкция ===")
    print("Игра помогает научиться распознавать фишинговые письма и поддельные сайты.")
    print("1. В режиме «Инспектор входящих» вы видите письма и решаете: фишинг (y) или нет (n).")
    print("2. В режиме «Найди подделку» вы видите список элементов сайта.")
    print("   Введите через пробел номера тех элементов, которые считаете подозрительными.")
    print("3. Во время проверки писем можно ввести 'hint' для подсказки.")
    print("===================\n")