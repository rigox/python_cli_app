from .items import Book
from termcolor import cprint


class Store:
    def __init__(self,books):
        self.books = books

    def listBooks(self):
        temp =  self.books

        for x in books:
            cprint("Title: {}".format(x.title),'magenta')
            cprint("Title: {}".format(x.author),'magenta')
            cprint("Title: {}".format(x.description),'magenta')
            cprint("Title: {}".format(x.price),'magenta')
            print("------------\n")

