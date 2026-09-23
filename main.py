# main.py
# Точка входа в игру "Фишинг-Детектив"

from game import Stats, email_mode, website_mode, instructions


def main():
    stats = Stats()

    while True:
        print("\n=== Фишинг-Детектив ===")
        print("1. Инспектор входящих (письма)")
        print("2. Найди подделку (сайты)")
        print("3. Инструкция")
        print("4. Статистика")
        print("5. Выход")

        choice = input("Выберите пункт: ").strip()

        if choice == '1':
            email_mode(stats)
        elif choice == '2':
            website_mode(stats)
        elif choice == '3':
            instructions()
        elif choice == '4':
            stats.show()
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()