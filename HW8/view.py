def new_rec(mode = "new") -> tuple:
    """
    Ввод данных для новой записи в справочнике
    """
    if mode == "new":
        print("Режим ввода новой записи")
    elif mode == "update":
        print("Ввод новых данных для записи {surname}")
        print("Пустая строка означает оставить данные без изменения")
    else:
        raise ValueError(f"Недоустимый флаг mode: {mode}")
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    tel = input("Введите номер телефона: ")
    desc = input("Введите Описание: ")
    return surname, name, tel, desc


def file_name() -> str:
    return input("Введите имя файла:")


def surname():
    return input("Введите фамилию:")


def show_recs(recs: list):
    for rec in recs:
        show_rec(rec)


def show_rec(rec: dict):
    """
    Отображение одной записи в консоли

    """
    # Здесь нарушается MVC мы использяем явно values, значит это словарь
    for val in rec.values():
        print(val, end=" ")
    print("")


def show_all_recs(phone_book: list):
    """
    Отображение всех записей справочника в консоли

    """
    print("Записи в справочнике:")
    for rec in phone_book:
        show_rec(rec)


def show_menu() -> str:
    """
    Отображение меню пользователя
    :return:
    """
    print("-"*20)
    print("МЕНЮ:")
    print("\t 1 - Ввод новой записи:")
    print("\t 2   - Поиск записи по фамилии")
    print("\t 3  - Изменение записи по фамилии")
    print("\t 4 - Удаление записи по фамилии")
    print("\t 5 - Импорт из файла")
    print("\t 6 - Экспорт в файл")
    print("\t 7   - Вывод на экран содержиого справочника")

    return input("Выберите нужный пункт")