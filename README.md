###test_dict_book_rating_exists 
тестируется метод init, проверяется наличие пустого словаря books_rating

###test_list_favorites_exists
тестируется метод init, проверяется наличие пустого списка favorites

###test_add_new_book_add_one_book
тестируется метод add_new_book, проверяется успешность добавления одной книги 

###test_add_new_book_add_two_books
тестируется метод add_new_book, проверяется успешность добавления двух книг

###test_add_new_book_add_two_same_books_only_one_added
тестируется метод add_new_book, проверяется, что уже добавленная книга не добавится в список еще раз

###test_add_new_book_add_one_book_rating_equals_1
тестируется метод add_new_book, проверяется, что у добавленной книги по умолчанию рейтинг "1"

###test_add_new_book_add_one_book_name_correct
тестируется метод add_new_book, проверяется корректность названия добавленной книги 

###test_set_book_rating_set_5_rating_updated
тестируется метод set_book_rating, проверяется корректность изменения рейтинга 

###test_set_book_rating_book_non_existent_dict_empty
тестируется метод set_book_rating, проверяется, что нельзя изменить рейтинг книге, которой нет в словаре books_rating

###test_set_book_rating_set_11_rating_still_1
тестируется метод set_book_rating, проверяется, что нельзя выставить рейтинг выше 10

###test_set_book_rating_set_negative_rating_still_1
тестируется метод set_book_rating, проверяется, что нельзя выставить рейтинг ниже 1

###test_get_book_rating_book_doesnt_exist
тестируется метод get_book_rating, проверяется, что у книги, которой нет в словаре books_rating нет рейтинга 

###test_get_books_with_specific_rating_1_book
тестируется метод get_books_with_specific_rating, проверяется наличие одной книги в списке 

###test_get_books_with_specific_rating_2_books_with_same_rating_2_books
тестируется метод get_books_with_specific_rating, проверяется наличие нескольких книги в списке с одинаковы рейтингом 

###test_get_books_with_specific_rating_2_of_the_3_books_with_same_rating_2_books
тестируется метод get_books_with_specific_rating, проверяется, что выводятся книги только с переданным рейтингом 

###test_get_books_with_specific_rating_books_with_same_updated_rating_2_books
тестируется метод get_books_with_specific_rating, проверяется наличие нескольких книги в списке с одинаковы рейтингом, после изменения рейтинга

###test_add_book_in_favorites_1_book_added
тестируется метод add_book_in_favorites, проверяется добавления книги в список favorites

###test_add_book_in_favorites_book_not_in_list_list_empty
тестируется метод add_book_in_favorites, проверяется, что нельзя добавить книгу в список favorites, если ее нет в словаре books_rating

###test_delete_book_from_favorites_book_in_list_book_deleted
тестируется метод delete_book_from_favorites, проверяется удаление книги из списка favorites

###test_delete_book_from_favorites_book_not_in_list
тестируется метод delete_book_from_favorites, проверяется, что нельзя удалить книгу которой нет в словаре books_rating