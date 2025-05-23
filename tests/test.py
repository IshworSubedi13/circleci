import pytest
from book.books import Book
def test_book_borrow_success():
    book = Book("Clean Code", "Robert Cecil Martin")
    success = book.borrow()
    assert success is True
    assert book.available is False