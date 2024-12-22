import pytest

from book_collector import BooksCollector


class TestBooksCollector1:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

    def test_add_new_book_books_genre_book_in_list(self):
        book = BooksCollector()
        book_name = 'Книга'
        book.add_new_book(book_name)

        assert book.get_books_genre().get(book_name) == '', f"Книга '{book_name}' добавлена"


class TestBooksCollector2:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_with_your_name_passed(self, genre):
        book = BooksCollector()
        book_name = "Книга"
        book.add_new_book(book_name)
        book.set_book_genre(book_name, genre)

        assert book.get_book_genre(book_name) == genre


class TestBooksCollector3:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

    def test_get_book_genre_with_your_name_passed(self):
        book = BooksCollector()
        book.add_new_book("HIMYM")
        book.set_book_genre("HIMYM", "Комедии")
        genre = book.get_book_genre("HIMYM")

        assert genre == "Комедии", f"Ожидаемый результат 'Комедии', получено {genre}"


class TestBooksCollector4:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

    @pytest.mark.parametrize(
        "genre, expected_books",
        [
            ('Фантастика', ['Book 1']),
            ('Ужасы', ['Book 2']),
            ('Детективы', ['Book 3']),
            ('Мультфильмы', ['Book 4']),
            ('Комедии', ['Book 5'])
        ]
    )
    def test_get_books_with_specific_genre_passed(self, genre, expected_books):
        book = BooksCollector()
        book.books_genre = {
            'Book 1': 'Фантастика',
            'Book 2': 'Ужасы',
            'Book 3': 'Детективы',
            'Book 4': 'Мультфильмы',
            'Book 5': 'Комедии'
        }

        result = book.get_books_with_specific_genre(genre)
        assert result == expected_books, f"Ожидалось {expected_books}, получено {result}"


class TestBooksCollector5:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

    def test_get_books_genre_list_books_passed(self):
        book = BooksCollector()
        assert book.get_books_genre() == {}, 'Словарь получен'


class TestBooksCollector6:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

    def test_get_books_for_children_return_for_children(self):
        book = BooksCollector()
        book.books_genre = {
            'Book 1': 'Фантастика',
            'Book 2': 'Ужасы',
            'Book 3': 'Детективы',
            'Book 4': 'Мультфильмы',
            'Book 5': 'Комедии'
        }
        result = book.get_books_for_children()
        assert result == ['Book 1', 'Book 4', 'Book 5']


class TestBooksCollector7:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

    def test_add_book_in_favorites_book_in_list(self):
        book = BooksCollector()
        book.add_new_book('Книга')
        book.add_book_in_favorites('Книга')
        assert 'Книга' in book.get_list_of_favorites_books(), 'Книга должна быть в списке избранного'

    class TestBooksCollector8:

        def __init__(self):
            self.books_genre = {}
            self.favorites = []
            self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
            self.genre_age_rating = ['Ужасы', 'Детективы']

    def test_delete_book_from_favorites_book_in_list(self):
        book = BooksCollector()
        book.add_new_book('Книга')
        book.add_book_in_favorites('Книга')
        book.delete_book_from_favorites('Книга')
        assert 'Книга' not in book.get_list_of_favorites_books(), 'Книга удалена из списка избранного'

    class TestBooksCollector9:

        def __init__(self):
            self.books_genre = {}
            self.favorites = []
            self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
            self.genre_age_rating = ['Ужасы', 'Детективы']

    def test_get_list_of_favorites_books_list_books_passed(self):
        book = BooksCollector()
        book.add_new_book('Book 1')
        book.add_new_book('Book 2')
        book.add_book_in_favorites('Book 1')
        book.add_book_in_favorites('Book 2')
        assert book.get_list_of_favorites_books() == ['Book 1', 'Book 2'], 'Список избранных книг не совпадает с ожидаемым'
