books = [
    {
        "id": 1,
        "title": "Мастер и Маргарита",
        "author": "Михаил Булгаков",
        "year": 1967,
        "status": "Доступна"
    },
    {
        "id": 2,
        "title": "Преступление и наказание",
        "author": "Фёдор Достоевский",
        "year": 1866,
        "status": "Выдана"
    },
    {
        "id": 3,
        "title": "Война и мир",
        "author": "Лев Толстой",
        "year": 1869,
        "status": "Доступна"
    }
]


def show_books(book_list):
    print("\nКаталог книг:")

    if not book_list:
        print("Книги не найдены.")
        return

    for book in book_list:
        print(
            f"ID: {book['id']} | "
            f"{book['title']} — {book['author']} | "
            f"{book['year']} | "
            f"Статус: {book['status']}"
        )


def search_books(book_list, query):
    result = []

    for book in book_list:
        if (
            query.lower() in book["title"].lower()
            or query.lower() in book["author"].lower()
        ):
            result.append(book)

    return result


def add_book(book_list, title, author, year):
    new_id = max([book["id"] for book in book_list], default=0) + 1

    book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year,
        "status": "Доступна"
    }

    book_list.append(book)
    print("Книга успешно добавлена.")


def delete_book(book_list, book_id):
    for book in book_list:
        if book["id"] == book_id:
            book_list.remove(book)
            print("Книга удалена.")
            return True

    print("Книга с таким ID не найдена.")
    return False


def change_status(book_list, book_id, new_status):
    for book in book_list:
        if book["id"] == book_id:
            book["status"] = new_status
            print("Статус книги изменён.")
            return True

    print("Книга с таким ID не найдена.")
    return False


def reader_menu():
    while True:
        print("\n===== Меню читателя =====")
        print("1. Показать каталог")
        print("2. Найти книгу")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_books(books)

        elif choice == "2":
            query = input("Введите название или автора: ").strip()

            if not query:
                print("Ошибка: поисковый запрос не может быть пустым.")
                continue

            result = search_books(books, query)
            show_books(result)

        elif choice == "0":
            print("Выход из меню читателя.")
            break

        else:
            print("Ошибка: такого пункта меню нет.")


def librarian_menu():
    while True:
        print("\n===== Меню библиотекаря =====")
        print("1. Показать каталог")
        print("2. Найти книгу")
        print("3. Добавить книгу")
        print("4. Удалить книгу")
        print("5. Изменить статус книги")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_books(books)

        elif choice == "2":
            query = input("Введите название или автора: ").strip()

            if not query:
                print("Ошибка: поисковый запрос не может быть пустым.")
                continue

            result = search_books(books, query)
            show_books(result)

        elif choice == "3":
            title = input("Введите название книги: ").strip()
            author = input("Введите автора: ").strip()
            year_input = input("Введите год издания: ").strip()

            if not title or not author:
                print("Ошибка: название и автор не могут быть пустыми.")
                continue

            if not year_input.isdigit():
                print("Ошибка: год должен быть числом.")
                continue

            year = int(year_input)
            add_book(books, title, author, year)

        elif choice == "4":
            book_id_input = input("Введите ID книги: ").strip()

            if not book_id_input.isdigit():
                print("Ошибка: ID должен быть числом.")
                continue

            book_id = int(book_id_input)
            delete_book(books, book_id)

        elif choice == "5":
            book_id_input = input("Введите ID книги: ").strip()

            if not book_id_input.isdigit():
                print("Ошибка: ID должен быть числом.")
                continue

            book_id = int(book_id_input)

            print("1. Доступна")
            print("2. Выдана")

            status_choice = input("Выберите новый статус: ")

            if status_choice == "1":
                change_status(books, book_id, "Доступна")

            elif status_choice == "2":
                change_status(books, book_id, "Выдана")

            else:
                print("Ошибка: такого статуса нет.")

        elif choice == "0":
            print("Выход из меню библиотекаря.")
            break

        else:
            print("Ошибка: такого пункта меню нет.")


print("Каталог книг в библиотеке")
print("Проект программной инженерии")

while True:
    print("\n===== Выбор роли =====")
    print("1. Читатель")
    print("2. Библиотекарь")
    print("0. Выход")

    role = input("Выберите роль: ")

    if role == "1":
        reader_menu()

    elif role == "2":
        librarian_menu()

    elif role == "0":
        print("Программа завершена.")
        break

    else:
        print("Ошибка: необходимо выбрать 1, 2 или 0.")