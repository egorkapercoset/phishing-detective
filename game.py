# game.py
# Логика игры "Фишинг-Детектив"

import random
from data import EMAILS, WEBSITES, RECOMMENDATIONS


class Stats:
    """Класс для хранения статистики игрока."""

    def __init__(self):
        self.email_correct = 0
        self.email_total = 0
        self.web_correct = 0
        self.web_total = 0
        # История раундов для сравнения
        self.email_history = []  # список процентов за каждый раунд
        self.web_history = []
        # Темы, в которых были ошибки
        self.wrong_topics = set()

    def add_email_result(self, correct, signs=None):
        self.email_total += 1
        if correct:
            self.email_correct += 1
        elif signs:
            for sign in signs:
                self.wrong_topics.add(sign)

    def add_web_result(self, correct, signs=None):
        self.web_total += 1
        if correct:
            self.web_correct += 1
        elif signs:
            for sign in signs:
                self.wrong_topics.add(sign)

    def finish_email_round(self, correct, total):
        """Сохраняет результат раунда в историю."""
        percent = correct / total * 100 if total else 0
        self.email_history.append(percent)

    def finish_web_round(self, correct, total):
        percent = correct / total * 100 if total else 0
        self.web_history.append(percent)

    def show(self):
        print("\n=== Статистика ===")
        if self.email_total > 0:
            percent = self.email_correct / self.email_total * 100
            print(f"Режим «Инспектор входящих»: {self.email_correct}/{self.email_total} "
                  f"({percent:.1f}%)")
            if len(self.email_history) >= 2:
                prev = self.email_history[-2]
                curr = self.email_history[-1]
                diff = curr - prev
                arrow = "↑" if diff > 0 else ("↓" if diff < 0 else "=")
                print(f"  Сравнение с прошлым раундом: было {prev:.1f}%, стало {curr:.1f}% {arrow}")
        else:
            print("Режим «Инспектор входящих»: нет попыток.")

        if self.web_total > 0:
            percent = self.web_correct / self.web_total * 100
            print(f"Режим «Найди подделку»: {self.web_correct}/{self.web_total} "
                  f"({percent:.1f}%)")
            if len(self.web_history) >= 2:
                prev = self.web_history[-2]
                curr = self.web_history[-1]
                diff = curr - prev
                arrow = "↑" if diff > 0 else ("↓" if diff < 0 else "=")
                print(f"  Сравнение с прошлым раундом: было {prev:.1f}%, стало {curr:.1f}% {arrow}")
        else:
            print("Режим «Найди подделку»: нет попыток.")

        # Рекомендации по темам
        if self.wrong_topics:
            print("\n--- Рекомендации по темам ---")
            for topic in self.wrong_topics:
                if topic in RECOMMENDATIONS:
                    print(f"• {topic}:")
                    print(f"  {RECOMMENDATIONS[topic]}")
        print("===================\n")


def choose_difficulty():
    """Выбор уровня сложности."""
    print("\nВыберите уровень сложности:")
    print("1. Лёгкий")
    print("2. Средний")
    print("3. Сложный")
    print("4. Все уровни")
    choice = input("Ваш выбор: ").strip()
    if choice == '1':
        return [1]
    elif choice == '2':
        return [2]
    elif choice == '3':
        return [3]
    else:
        return [1, 2, 3]


def email_mode(stats: Stats):
    """Режим «Инспектор входящих»."""
    print("\n--- Инспектор входящих ---")
    levels = choose_difficulty()

    available = [e for e in EMAILS if e['difficulty'] in levels]
    if not available:
        print("Нет писем для выбранного уровня сложности.")
        return

    emails = random.sample(available, min(5, len(available)))
    correct_count = 0

    for i, email in enumerate(emails, 1):
        print(f"\nПисьмо {i} из {len(emails)} (сложность: {email['difficulty']}):")
        print(f"От: {email['sender']}")
        print(f"Тема: {email['subject']}")
        print(f"Текст: {email['body']}")

        # Постепенные подсказки
        hint_level = 0
        while True:
            choice = input("Это фишинг? (y/n/hint): ").strip().lower()
            if choice == 'hint':
                if hint_level < len(email['hints']):
                    print(f"Подсказка {hint_level + 1}: {email['hints'][hint_level]}")
                    hint_level += 1
                else:
                    print("Больше подсказок нет. Попробуйте ответить.")
                continue
            elif choice in ('y', 'n'):
                break
            else:
                print("Введите 'y', 'n' или 'hint'.")

        user_says_phishing = (choice == 'y')
        correct = (user_says_phishing == email['is_phishing'])

        if correct:
            correct_count += 1
            print("✅ Верно!")
        else:
            print("❌ Неверно.")
            # Запоминаем темы, в которых ошиблись
            if email['signs']:
                stats.add_email_result(False, email['signs'])

        print(f"Объяснение: {email['explanation']}")
        if email['signs']:
            print(f"Признаки мошенничества: {', '.join(email['signs'])}")

        stats.add_email_result(correct) if correct else None

    stats.finish_email_round(correct_count, len(emails))
    print(f"\nКонец раунда. Правильных ответов: {correct_count}/{len(emails)}")
    stats.show()


def website_mode(stats: Stats):
    """Режим «Найди подделку»."""
    print("\n--- Найди подделку ---")
    levels = choose_difficulty()

    available = [w for w in WEBSITES if w['difficulty'] in levels]
    if not available:
        print("Нет сайтов для выбранного уровня сложности.")
        return

    site = random.choice(available)
    print(f"\nСайт: {site['name']} (сложность: {site['difficulty']})")
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

    found_signs = 0
    missed_signs = []

    for idx in selected:
        elem = site['elements'][idx - 1]
        if idx in correct_selections:
            found_signs += 1
            print(f"✅ Элемент {idx} действительно подозрительный. {elem['explanation']}")
        else:
            print(f"❌ Элемент {idx} НЕ является подозрительным. {elem['explanation']}")

    for idx in correct_selections:
        if idx not in selected:
            elem = site['elements'][idx - 1]
            print(f"⚠️ Вы пропустили элемент {idx}: {elem['text']}")
            print(f"   Признак: {elem.get('sign', 'подозрительный элемент')}")
            print(f"   Объяснение: {elem['explanation']}")
            if elem.get('sign'):
                missed_signs.append(elem['sign'])

    total_signs = len(correct_selections)
    print(f"\nНайдено признаков: {found_signs} из {total_signs}")

    correct = (selected == correct_selections)
    stats.add_web_result(correct, missed_signs)
    stats.finish_web_round(found_signs, total_signs)

    if correct:
        print("🏆 Отлично! Вы нашли все подозрительные элементы.")
    else:
        print("Некоторые элементы были пропущены или выбраны неверно.")
    stats.show()


def instructions():
    """Краткая инструкция для игрока."""
    print("\n=== Инструкция ===")
    print("Игра помогает научиться распознавать фишинговые письма и поддельные сайты.")
    print("1. В режиме «Инспектор входящих» вы видите письма и решаете: фишинг (y) или нет (n).")
    print("   Можно вводить 'hint' для постепенных подсказок (3 уровня).")
    print("2. В режиме «Найди подделку» вы видите список элементов сайта.")
    print("   Введите через пробел номера подозрительных элементов (например, 1 3 5).")
    print("3. Перед началом каждого режима выбирается уровень сложности.")
    print("4. После раунда показывается статистика, сравнение с прошлым разом и рекомендации.")
    print("===================\n")