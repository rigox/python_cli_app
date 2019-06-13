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
},
{'title':'the fountain Head',
'author':"Ayn Rand",
'description':"a mans selfishness is his best  strength",
'price':'5',
'isbn':"223213213",
},
{'title':'anthem',
'author':'ayn rand',
'description':"a socialist destopia",
'price':'5',
'isbn':'4343242342',
},
{'title':'the prince',
'author':'niccolo machiavelli',
'description':'lessons from the past are still relevant today',
'price':'1',
'isbn':'32234545435',
},
]



store =  Store(books_collection)

def menu():
     cprint("1--   View Items",'yellow')
     cprint("2-- pruchase Items",'yellow')
     cprint("3-- exit",'yellow')


         
def main():
    counter  = 0
    while(counter!=4):
        menu()
        counter  =  int(input())
        if(counter==1):
            cprint("a: {}".format("hello"),"red") 

     
     


if __name__  == "__main__":
    main();