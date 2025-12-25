def show_menu():
    print("\nВыберите действие:")
    print("1. Добавить привычку")
    print("2. Отметить выполнение")
    print("3. Показать статистику")
    print("4. Выйти")

    def get_user_choice():
        return input("Введите номер действия: ")

    def ask_habit_name():
        return input("Введите название привычки: ")

        