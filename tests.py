from main import BooksCollector

class TestBooksCollector:

    def test_dict_book_rating_exists(self):
        collector = BooksCollector()

        assert collector.get_books_rating() == {}

    def test_list_favorites_exists(self):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []

    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_rating()) == 1

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_two_same_books_only_one_added(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_rating()) == 1

    def test_add_new_book_add_one_book_rating_equals_1(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_add_new_book_add_one_book_name_correct(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        assert 'Гордость и предубеждение и зомби' in collector.get_books_rating()

    def test_set_book_rating_set_5_rating_updated(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.set_book_rating('Гордость и предубеждение и зомби', 5)

        assert collector.get_books_rating() == {'Гордость и предубеждение и зомби': 5}

    def test_set_book_rating_book_non_existent_dict_empty(self):
        collector = BooksCollector()

        collector.set_book_rating('Гордость и предубеждение и зомби', 5)

        assert collector.get_books_rating() == {}

    def test_set_book_rating_set_11_rating_still_1(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.set_book_rating('Гордость и предубеждение и зомби', 11)

        assert collector.get_books_rating() == {'Гордость и предубеждение и зомби': 1}

    def test_set_book_rating_set_negative_rating_still_1(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.set_book_rating('Гордость и предубеждение и зомби', -5)

        assert collector.get_books_rating() == {'Гордость и предубеждение и зомби': 1}

    def test_get_book_rating_book_doesnt_exist(self):
        collector = BooksCollector()

        assert collector.get_book_rating('Гордость и предубеждение и зомби') == None

    def test_get_books_with_specific_rating_1_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_with_specific_rating(1)) == 1

    def test_get_books_with_specific_rating_2_books_with_same_rating_2_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_with_specific_rating(1)) == 2

    def test_get_books_with_specific_rating_2_of_the_3_books_with_same_rating_2_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Фиолетовые тапки')

        collector.set_book_rating('Гордость и предубеждение и зомби', 5)

        assert len(collector.get_books_with_specific_rating(1)) == 2

    def test_get_books_with_specific_rating_books_with_same_updated_rating_2_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 5)

        assert len(collector.get_books_with_specific_rating(5)) == 2

    def test_add_book_in_favorites_1_book_added(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_book_not_in_list_list_empty(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_book_in_list_book_deleted(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_book_not_in_list(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 0