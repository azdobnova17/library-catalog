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
    """Выводит информацию о книгах."""
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
    """Ищет книги по названию или автору."""
    result = []

    for book in book_list:
        if (
            query.lower() in book["title"].lower()
            or query.lower() in book["author"].lower()
        ):
            result.append(book)

    return result


def add_book(book_list, title, author, year, status="Доступна"):
    """Добавляет новую книгу и возвращает её."""
    new_id = max([book["id"] for book in book_list], default=0) + 1

    book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year,
        "status": status
    }

    book_list.append(book)
    return book


def delete_book(book_list, book_id):
    """Удаляет книгу по ID и возвращает результат."""
    for book in book_list:
        if book["id"] == book_id:
            book_list.remove(book)
            return True

    return False


def change_status(book_list, book_id, new_status):
    """Изменяет статус книги."""
    for book in book_list:
        if book["id"] == book_id:
            book["status"] = new_status
            return True

    return False


def can_perform_action(role, action):
    """Проверяет права пользователя."""
    reader_actions = ["view", "search"]

    if role == "Библиотекарь":
        return True

    if role == "Читатель" and action in reader_actions:
        return True

    return False


print("Каталог книг в библиотеке")
print("Проект программной инженерии")


print("\n===== Набор данных 1: Читатель =====")

reader_role = "Читатель"

if can_perform_action(reader_role, "view"):
    show_books(books)

if can_perform_action(reader_role, "search"):
    found_books = search_books(books, "Толстой")
    print("\nРезультат поиска по запросу «Толстой»:")
    show_books(found_books)

if not can_perform_action(reader_role, "delete"):
    print("\nЧитателю запрещено удалять книги.")


print("\n===== Набор данных 2: Поиск =====")

search_result = search_books(books, "Булгаков")
print("\nРезультат поиска по запросу «Булгаков»:")
show_books(search_result)


print("\n===== Набор данных 3: Библиотекарь =====")

librarian_role = "Библиотекарь"

if can_perform_action(librarian_role, "add"):
    new_book = add_book(
        books,
        "Гарри Поттер",
        "Джоан Роулинг",
        1997
    )
    print(f"Добавлена книга: {new_book['title']}")

if can_perform_action(librarian_role, "status"):
    if change_status(books, 1, "Выдана"):
        print("Статус книги с ID 1 изменён.")

if can_perform_action(librarian_role, "delete"):
    if delete_book(books, 2):
        print("Книга с ID 2 удалена.")


print("\n===== Итоговый каталог =====")
show_books(books)