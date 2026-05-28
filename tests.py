from main import BooksCollector
import pytest
class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_with_long_name_not_added(self):
        collector = BooksCollector()

        long_name = 'Возможное название какой-то книги, в котором больше 40 символов'

        collector.add_new_book(long_name)

        assert long_name not in collector.get_books_genre()

    def test_add_new_book_with_empty_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Чапаев и пустота')

        assert collector.get_book_genre('Чапаев и пустота') == ''   

    @pytest.mark.parametrize('name, genre', [('Ампир V','Ужасы'),('Шерлок Холмс','Детективы'),('Котопёс','Мультфильмы')])
    def test_set_book_genre(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        
        assert collector.get_book_genre(name) == genre

    def test_get_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Алиса в стране Чудес')

        collector.set_book_genre('Алиса в стране Чудес','Фантастика')

        assert collector.get_book_genre('Алиса в стране Чудес') == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Некрономиком')
        collector.add_new_book('Алиса в стране Чудес')

        collector.set_book_genre('Некрономиком', 'Ужасы')
        collector.set_book_genre('Алиса в стране Чудес', 'Фантастика')

        fantasy_books = collector.get_books_with_specific_genre('Фантастика')

        assert 'Алиса в стране Чудес' in fantasy_books
        assert len(fantasy_books) == 1

    def test_get_books_genre_returns_dictionaty(self):
        collector = BooksCollector()

        collector.add_new_book('Превращение')

        assert collector.get_books_genre() == {'Превращение':''}

    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Превращение')
        collector.add_new_book('Капитал')

        collector.set_book_genre('Превращение', 'Ужасы')
        collector.set_book_genre('Капитал', 'Мультфильмы')

        children_books = collector.get_books_for_children()

        assert 'Капитал' in children_books
        assert 'Превращение' not in children_books

    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Generation П')

        collector.add_book_in_favorites('Generation П')

        assert 'Generation П' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_only_one_time(self):
        collector = BooksCollector()
        
        collector.add_new_book('Generation П')

        collector.add_book_in_favorites('Generation П')
        collector.add_book_in_favorites('Generation П')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Generation П')

        collector.add_book_in_favorites('Generation П')
        collector.delete_book_from_favorites('Generation П')

        assert 'Generation П' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Generation П')

        collector.add_book_in_favorites('Generation П')

        assert collector.get_list_of_favorites_books() == ['Generation П']