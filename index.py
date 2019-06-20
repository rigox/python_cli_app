from __future__ import print_function, unicode_literals
import argparse;
import requests;
from models.items  import Book
from models.store import Store
from termcolor import cprint
parser = argparse.ArgumentParser()

books_collection =[
{'title':"The count of Monte Cristo",
'author':"Alexander Dummas",
'description':"Vengance is fueld by time",
'price':"4",
'isbn':"3212342455",
"ID":1
},
{'title':'the fountain Head',
'author':"Ayn Rand",
'description':"a mans selfishness is his best  strength",
'price':'5',
'isbn':"223213213",
"ID":2
},
{'title':'anthem',
'author':'ayn rand',
'description':"a socialist destopia",
'price':'5',
'isbn':'4343242342',
"ID":3
},
{'title':'the prince',
'author':'niccolo machiavelli',
'description':'lessons from the past are still relevant today',
'price':'1',
'isbn':'32234545435',
"ID":4
},
]



store =  Store(books_collection)

def getBooks():
    store.listBooks()



def menu():
     print('\n')
     cprint("\t\t\t1--  View Items",'yellow')
     cprint("\t\t\t2--  Purchase Items",'yellow')
     cprint("\t\t\t3--  View Cart","yellow")
     cprint('\t\t\t4--  Checkout',"yellow")
     cprint("\t\t\t5--  Exit",'yellow')
     


         
def main():
    counter  = 0
    cprint("\t\t\tWELCOME TO LIBROS!!!!","magenta")
    while(counter!=4):
        menu()
        counter  =  int(input())
        if(counter==1):
            getBooks()
        elif(counter==2):
            store.make_purchase()
        elif(counter==3):
            store.view_cart()

     
     


if __name__  == "__main__":
    main();