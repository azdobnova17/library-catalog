class Book:
    def __init__(self, book_id, title, author, year, status):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def change_status(self, new_status):
        self.status = new_status


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        new_id = max([book.id for book in self.books], default=0) + 1

        book = Book(
            new_id,
            title,
            author,
            year,
            "Доступна"
        )

        self.books.append(book)
        print("Книга успешно добавлена.")

    def show_books(self, book_list=None):
        if book_list is None:
            book_list = self.books

        print("\nКаталог книг:")

        if not book_list:
            print("Книги не найдены.")
            return

        for book in book_list:
            print(
                f"ID: {book.id} | "
                f"{book.title} — {book.author} | "
                f"{book.year} | "
                f"Статус: {book.status}"
            )

    def search_books(self, query):
        result = []

        for book in self.books:
            if (
                query.lower() in book.title.lower()
                or query.lower() in book.author.lower()
            ):
                result.append(book)

        return result

    def delete_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                print("Книга удалена.")
                return True

        print("Книга с таким ID не найдена.")
        return False

    def change_status(self, book_id, new_status):
        for book in self.books:
            if book.id == book_id:
                book.change_status(new_status)
                print("Статус книги изменён.")
                return True

        print("Книга с таким ID не найдена.")
        return False


library = Library()

library.books.append(
    Book(
        1,
        "Мастер и Маргарита",
        "Михаил Булгаков",
        1967,
        "Доступна"
    )
)

library.books.append(
    Book(
        2,
        "Преступление и наказание",
        "Фёдор Достоевский",
        1866,
        "Выдана"
    )
)

library.books.append(
    Book(
        3,
        "Война и мир",
        "Лев Толстой",
        1869,
        "Доступна"
    )
)


def reader_menu():
    while True:
        print("\n===== Меню читателя =====")
        print("1. Показать каталог")
        print("2. Найти книгу")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            library.show_books()

        elif choice == "2":
            query = input("Введите название или автора: ").strip()

            if not query:
                print("Ошибка: поисковый запрос не может быть пустым.")
                continue

            result = library.search_books(query)
            library.show_books(result)

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
            library.show_books()

        elif choice == "2":
            query = input("Введите название или автора: ").strip()

            if not query:
                print("Ошибка: поисковый запрос не может быть пустым.")
                continue

            result = library.search_books(query)
            library.show_books(result)

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
            library.add_book(title, author, year)

        elif choice == "4":
            book_id_input = input("Введите ID книги: ").strip()

            if not book_id_input.isdigit():
                print("Ошибка: ID должен быть числом.")
                continue

            book_id = int(book_id_input)
            library.delete_book(book_id)

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
                library.change_status(book_id, "Доступна")

            elif status_choice == "2":
                library.change_status(book_id, "Выдана")

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