#!/usr/bin/env python3

class Book:
    
    def __init__(self, title) -> None:
        self.title = title

    def get_pages(self):
        return self._page_count

    def set_pages(self, pages):
        if type(pages) == int:
            self._page_count = pages
        else:
            print("page_count must be an integer")
            self._page_count = None

    page_count = property(get_pages, set_pages)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

book = Book("How to Scrumb")

book.page_count = "fuck"

print(book.page_count)